import os
import http
import logging
from ast import literal_eval

import requests
from flask import Flask, request
from werkzeug.wrappers import Response

from telegram import Bot, Update
from telegram.ext import Dispatcher, Filters, MessageHandler, CommandHandler

BOT_TOKEN = os.environ["BOT_TOKEN"]
PEPE_API_ENDPOINT = os.environ["PEPE_API_ENDPOINT"]


app = Flask(__name__)
bot = Bot(token=BOT_TOKEN)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_giphy_links(text, top_k=3):
    # TODO: make async
    return literal_eval(requests.post(PEPE_API_ENDPOINT, json={"text": text}).json()["result"])[:top_k]


def start(update: Update, context):
    update.message.reply_text(text="I'm a PEPE-Semantics bot to find the best gifs for you")


def reply(update: Update, context):
    links = get_giphy_links(update.message.text)
    # TODO: fix this mess - should not use like that
    [
        update.message.reply_text(
            text=f"Sending you best GIF's to use for reply '{update.message.text}'!")
    ] + \
    [
        update.message.reply_text(
            text=f"GIF number {i}:\n{links[i]}")
        for i in range(len(links))
    ]


dispatcher = Dispatcher(bot=bot, update_queue=None)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

@app.post("/")
def index() -> Response:
    dispatcher.process_update(
        Update.de_json(request.get_json(force=True), bot))

    return "", http.HTTPStatus.NO_CONTENT
