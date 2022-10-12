import gradio as gr
import requests

SERVERLESS_URL = 'https://pepe-semantics-vdn32ryg7q-uc.a.run.app/predict'

gTop = []

def predict(text):
    global gTop
    r = requests.post(SERVERLESS_URL, json = {'text':text})
    dic = r.json()
    links = eval(dic['result'])
    gTop = links[:5]
    return gTop


callback = gr.CSVLogger()

css_bg_img = ".gradio-container {background-image: url('file=memes_images.png'); background-position: right;}"


with gr.Blocks(css=css_bg_img,theme="huggingface") as demo:
    gr.Markdown("""<h1 style='text-align: center;'><span style="background-color:white;">PEPE-Sematics</span></h1>""")
    gr.Markdown("""
        <p style="text-align:center;background-color: #FFFFFF" ><b>The world of GIFs needs saviour. While it has initially thrived on the legacy
        of a few GIFs, the Gifverse is becoming chaotic and it is becoming very difficult to find good Gifs. 
        Swoops in PEPE-Sematic to help those in need.<b></p>

        <center>
            <img src = "file/superman.gif"></img>
        </center>
        <p style="text-align:center;background-color: #FFFFFF"> PEPE-Sematics adopts from the <a href="https://github.com/xingyaoww/gif-reply" style='color:blue'>PEPE model</a>
        and uses MLOps to bring it to your browser. PEPE-Sematics present to you multiple recommendations to choose from.
        As fellow Giffer's we know it is never enough unless you spam your bae or friend or an annoying colleague, thus multiple 
        recommedations is the only way to go about it. To ease your confusion we also provide a top recommendation based on our 
        algorithm.</p>
    """)

    gr.Markdown("""<center><h2><span style="background-color:white;">Test it out</span></h2><center>""")

    text_input = gr.Textbox(label="Input",placeholder="Type something to get cool gifs \N{smile}")
    with gr.Row():
        submit_button = gr.Button("Submit")

    with gr.Row():
        gr.Markdown("""<center><h2><span style="background-color:white;">Top Recommedation</span></h2><center>""")
    with gr.Row():  
        # image0 = gr.Image()
        image0 =gr.HTML(
                f"<div style='width:100%;height:50%;padding-bottom:50%;position:relative;'><iframe src='https://giphy.com/embed/1YeNJK6FptDdq1q59K' width='100%' height='100%' style='position:absolute' frameBorder='0' class='giphy-embed' allowFullScreen></iframe></div>")
        # if len(link0.value) != 0:
        #     link0 = gr.HTML.value().split("/")[3]
        #     image0 = gr.HTML(
        #     f"<div style='width:100%;height:50%;padding-bottom:50%;position:relative;'><iframe src='https://giphy.com/embed/{link0}' width='100%' height='100%' style='position:absolute' frameBorder='0' class='giphy-embed' allowFullScreen></iframe></div>")
        with gr.Row():
            image0_up = gr.Button("\N{thumbs up sign}")
            image0_down = gr.Button("\N{thumbs down sign}")
            image0_flag = gr.Button("Flag")
    gr.Markdown("""<center><h2><span style="background-color:white;">Recommended GIFs</span></h2><center>""")
    with gr.Row():
        with gr.Column(scale=1, min_width=300):
            # image1 = gr.Image()
            image1 =gr.HTML(
                f"<div style='width:100%;height:0;padding-bottom:100%;position:relative;'><iframe src={'https://giphy.com/embed/u31fedwl4J7G0'} width='100%' height='100%' style='position:absolute' frameBorder='0' class='giphy-embed' allowFullScreen></iframe></div>")
            # if len(gTop) != 0:
            #     link1 = gTop[1].split("/")[3]
            #     gr.HTML(
            #         f"<div style='width:100%;height:0;padding-bottom:100%;position:relative;'><iframe src='https://giphy.com/embed/{link1}' width='100%' height='100%' style='position:absolute' frameBorder='0' class='giphy-embed' allowFullScreen></iframe></div>")
            with gr.Row():
                image1_up = gr.Button("\N{thumbs up sign}")
                image1_down = gr.Button("\N{thumbs down sign}")
                image1_flag = gr.Button("Flag")
        with gr.Column(scale=1,min_width=300):
            # image2 = gr.Image()
            image2 =gr.HTML(
                f"<div style='width:100%;height:0;padding-bottom:100%;position:relative;'><iframe src={'https://giphy.com/embed/l41YouCUUcreUabHW'} width='100%' height='100%' style='position:absolute' frameBorder='0' class='giphy-embed' allowFullScreen></iframe></div>")
            # if len(gTop) != 0:
            #     link2 = gTop[2].split("/")[3]
            #     gr.HTML(
            #     f"<div style='width:100%;height:0;padding-bottom:100%;position:relative;'><iframe src='https://giphy.com/embed/{link2}' width='100%' height='100%' style='position:absolute' frameBorder='0' class='giphy-embed' allowFullScreen></iframe></div>")    
            with gr.Row():
                image2_up = gr.Button("\N{thumbs up sign}")
                image2_down = gr.Button("\N{thumbs down sign}")
                image2_flag = gr.Button("Flag")
        with gr.Column(scale=1,min_width=300):
            # image3 = gr.Image()
            image3 = gr.HTML(
                f"<div style='width:100%;height:0;padding-bottom:100%;position:relative;'><iframe src={'https://giphy.com/embed/SJWZDnQfQe46YAvIxj'} width='100%' height='100%' style='position:absolute' frameBorder='0' class='giphy-embed' allowFullScreen></iframe></div>")
            # if len(gTop) != 0:
            #     link3 = gTop[3].split("/")[3]
            #     gr.HTML(
            #     f"<div style='width:100%;height:0;padding-bottom:100%;position:relative;'><iframe src='https://giphy.com/embed/{link3}' width='100%' height='100%' style='position:absolute' frameBorder='0' class='giphy-embed' allowFullScreen></iframe></div>")
            with gr.Row():
                image3_up = gr.Button("\N{thumbs up sign}")
                image3_down = gr.Button("\N{thumbs down sign}")
                image3_flag = gr.Button("Flag")
        with gr.Column(scale=1,min_width=300):
            image4 = gr.HTML()
            gr.HTML(
                """<div style="width:100%;height:0;padding-bottom:85%;position:relative;"><iframe src="https://giphy.com/embed/g7GKcSzwQfugw" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>""")
            # if len(image4.value) > 0:
            #     gr.Markdown("something else")
            #     link4 = image4.value.split("/")[3]
            #     gr.Markdown(
            #      "<div style='width:100%;height:0;padding-bottom:100%;position:relative;'><iframe src='https://giphy.com/embed/{link4}' width='100%' height='100%' style='position:absolute' frameBorder='0' class='giphy-embed' allowFullScreen></iframe></div>""")
            with gr.Row():
                image4_up = gr.Button("\N{thumbs up sign}")
                image4_down = gr.Button("\N{thumbs down sign}")
                image4_flag = gr.Button("Flag")
            
    
    if submit_button.click(predict, inputs=text_input, outputs= [image0,image1,image2,image3,image4], scroll_to_output=True):
        links_list = predict(inputs=text_input)
        
    callback.setup([text_input], "flagged_data")
        

    image1_up.click(lambda *args: callback.flag(args, flag_option="Up", username=gTop[1]), [text_input], None)
    image2_up.click(lambda *args: callback.flag(args, flag_option="Up", username=gTop[2]), [text_input], None)
    image3_up.click(lambda *args: callback.flag(args, flag_option="Up", username=gTop[3]), [text_input], None)
    image4_up.click(lambda *args: callback.flag(args, flag_option="Up", username=gTop[4]), [text_input], None)
    image0_up.click(lambda *args: callback.flag(args, flag_option="Up", username=gTop[0]), [text_input], None)
    image1_down.click(lambda *args: callback.flag(args, flag_option="Down", username=gTop[1]), [text_input], None)
    image2_down.click(lambda *args: callback.flag(args, flag_option="Down", username=gTop[2]), [text_input], None)
    image3_down.click(lambda *args: callback.flag(args, flag_option="Down", username=gTop[3]), [text_input], None)
    image4_down.click(lambda *args: callback.flag(args, flag_option="Down", username=gTop[4]), [text_input], None)
    image0_down.click(lambda *args: callback.flag(args, flag_option="Down", username=gTop[0]), [text_input], None)
    image1_flag.click(lambda *args: callback.flag(args, flag_option="Flag", username=gTop[1]), [text_input], None)
    image2_flag.click(lambda *args: callback.flag(args, flag_option="Flag", username=gTop[2]), [text_input], None) 
    image3_flag.click(lambda *args: callback.flag(args, flag_option="Flag", username=gTop[3]), [text_input], None)
    image4_flag.click(lambda *args: callback.flag(args, flag_option="Flag", username=gTop[4]), [text_input], None)
    image0_flag.click(lambda *args: callback.flag(args, flag_option="Flag", username=gTop[0]), [text_input], None)

demo.launch(debug=False,share=True)
