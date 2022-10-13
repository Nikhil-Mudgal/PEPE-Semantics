import gradio as gr
import requests

SERVERLESS_URL = 'https://pepe-semantics-vdn32ryg7q-uc.a.run.app/predict'

def predict(text):
    r = requests.post(SERVERLESS_URL, json = {'text':text})
    dic = r.json()
    links = eval(dic['result'])
    top = links[:2]
    return top

with gr.Blocks() as demo:
    text_input = gr.Textbox(label="Input")
    with gr.Row():
        submit_button = gr.Button("Submit")
    with gr.Row():
        image1 = gr.Image()
    with gr.Row():
        image1_up = gr.Button("Up")
        image1_down = gr.Button("Down")
        image1_flag = gr.Button("Flag")
        
    with gr.Row():
        image2 = gr.Image()
    with gr.Row():
        image2_up = gr.Button("Up")
        image2_down = gr.Button("Down")
        image2_flag = gr.Button("Flag")

    submit_button.click(predict, inputs=text_input, outputs=[image1, image2])

demo.launch(debug=False, share=True)