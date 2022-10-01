import gradio as gr
import requests

# SERVERLESS_URL = 'https://pepe-semantics-vdn32ryg7q-uc.a.run.app/predict' #NON-Continuously Integrated
SERVERLESS_URL = 'https://pepe-semantics-vdn32ryg7q-uc.a.run.app/predict'

gTop = []

def predict(text):
    global gTop
    r = requests.post(SERVERLESS_URL, json = {'text':text})
    dic = r.json()
    links = eval(dic['result'])
    gTop = links[:2]
    return gTop

callback = gr.CSVLogger()

with gr.Blocks() as demo:
    text_input = gr.Textbox(label="Input")
    with gr.Row():
        submit_button = gr.Button("Submit")
    with gr.Row():
        image1 = gr.Image()
    with gr.Row():
        image1_up = gr.Button("\N{thumbs up sign}")
        image1_down = gr.Button("\N{thumbs down sign}")
        image1_flag = gr.Button("Flag")
        
    with gr.Row():
        image2 = gr.Image()
    with gr.Row():
        image2_up = gr.Button("\N{thumbs up sign}")
        image2_down = gr.Button("\N{thumbs down sign}")
        image2_flag = gr.Button("Flag")

    callback.setup([text_input], "flagged_data")

    submit_button.click(predict, inputs=text_input, outputs=[image1, image2])

    image1_up.click(lambda *args: callback.flag(args, flag_option="Up", username=gTop[0]), [text_input], None)
    image2_up.click(lambda *args: callback.flag(args, flag_option="Up", username=gTop[1]), [text_input], None)
    image1_down.click(lambda *args: callback.flag(args, flag_option="Down", username=gTop[0]), [text_input], None)
    image2_down.click(lambda *args: callback.flag(args, flag_option="Down", username=gTop[1]), [text_input], None)
    image1_flag.click(lambda *args: callback.flag(args, flag_option="Flag", username=gTop[0]), [text_input], None)
    image2_flag.click(lambda *args: callback.flag(args, flag_option="Flag", username=gTop[1]), [text_input], None)
    

demo.launch(debug=False, share=True)