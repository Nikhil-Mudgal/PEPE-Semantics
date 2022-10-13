import gradio as gr
import requests

SERVERLESS_URL = "https://pepe-semantics-vdn32ryg7q-uc.a.run.app/predict"

gTop = []
linkTop = []


def predict(text):
    global gTop
    global linkTop

    r = requests.post(SERVERLESS_URL, json={"text": text})
    dic = r.json()
    links = eval(dic["result"])
    gTop = links[:5]

    linkTop = []
    for link in gTop:
        path = "![ALT TEXT](" + link + ")"
        linkTop.append(path)

    return linkTop


callback = gr.CSVLogger()

css_bg_img = ".gradio-container {background-image: url('file=https://wallpaperaccess.com/full/2470777.jpg'); background-position: center;}"


with gr.Blocks(css=css_bg_img) as demo:
    gr.Markdown(
        """<h1 style='text-align: center;'><span style="background-color:white;">PEPE-Sematics</span></h1>"""
    )
    gr.Markdown(
        """
        <p style="text-align:center;background-color: #FFFFFF" ><b>The world of GIFs needs saviour. While it has initially thrived on the legacy
        of a few GIFs, the Gifverse is becoming chaotic and it is becoming very difficult to find good Gifs. 
        Swoops in PEPE-Sematic to help those in need.<b></p>

        <center>
            <iframe src="https://giphy.com/embed/rBSB0tULImCv9DJi1P" width="480" height="361" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></p>
        </center>
        <p style="text-align:center;background-color: #FFFFFF"> PEPE-Sematics adopts from the <a href="https://github.com/xingyaoww/gif-reply" style='color:blue'>PEPE model</a>
        and uses MLOps to bring it to your browser. PEPE-Sematics present to you multiple recommendations to choose from.
        As fellow Giffer's we know it is never enough unless you spam your bae or friend or an annoying colleague, thus multiple 
        recommedations is the only way to go about it. To ease your confusion we also provide a top recommendation based on our 
        algorithm.</p>
    """
    )

    gr.Markdown(
        """<center><h2><span style="background-color:white;">Test it out</span></h2><center>"""
    )

    text_input = gr.Textbox(
        label="Input", placeholder="Type something to get cool gifs \N{smile}"
    )
    with gr.Row():
        submit_button = gr.Button("Submit")

    with gr.Row():
        gr.Markdown(
            """<center><h2><span style="background-color:white;">Top Recommedation</span></h2><center>"""
        )
    with gr.Row():
        image0 = gr.Markdown(
            "<iframe src='https://giphy.com/embed/1YeNJK6FptDdq1q59K' width='480' height='280' frameBorder='0' class='giphy-embed' allowFullScreen></iframe>"
        )
        with gr.Row():
            image0_up = gr.Button("\N{thumbs up sign}")
            image0_down = gr.Button("\N{thumbs down sign}")
            image0_flag = gr.Button("Flag")
    gr.Markdown(
        """<center><h2><span style="background-color:white;">Recommended GIFs</span></h2><center>"""
    )
    with gr.Row():
        with gr.Column(scale=1, min_width=300):
            image1 = gr.Markdown(
                "<iframe src='https://giphy.com/embed/enCWEo0vG25Ow' width='300' height='280' frameBorder='0' class='giphy-embed' allowFullScreen></iframe>"
            )
            with gr.Row():
                image1_up = gr.Button("\N{thumbs up sign}")
                image1_down = gr.Button("\N{thumbs down sign}")
                image1_flag = gr.Button("Flag")
        with gr.Column(scale=1, min_width=300):
            image2 = gr.Markdown(
                "<iframe src='https://giphy.com/embed/l41YouCUUcreUabHW' width='300' height='280' frameBorder='0' class='giphy-embed' allowFullScreen></iframe>"
            )
            with gr.Row():
                image2_up = gr.Button("\N{thumbs up sign}")
                image2_down = gr.Button("\N{thumbs down sign}")
                image2_flag = gr.Button("Flag")
        with gr.Column(scale=1, min_width=300):
            image3 = gr.Markdown(
                "<iframe src='https://giphy.com/embed/SJWZDnQfQe46YAvIxj' width='300' height='280' frameBorder='0' class='giphy-embed' allowFullScreen></iframe>"
            )
            with gr.Row():
                image3_up = gr.Button("\N{thumbs up sign}")
                image3_down = gr.Button("\N{thumbs down sign}")
                image3_flag = gr.Button("Flag")
        with gr.Column(scale=1, min_width=300):
            image4 = gr.Markdown(
                "<iframe src='https://giphy.com/embed/g7GKcSzwQfugw' width='300' height='280' frameBorder='0' class='giphy-embed' allowFullScreen></iframe>"
            )
            with gr.Row():
                image4_up = gr.Button("\N{thumbs up sign}")
                image4_down = gr.Button("\N{thumbs down sign}")
                image4_flag = gr.Button("Flag")

    outputs = submit_button.click(
        predict,
        inputs=text_input,
        outputs=[image0, image1, image2, image3, image4],
        scroll_to_output=True,
    )

    print(outputs)

    callback.setup([text_input], "flagged_data")

    image1_up.click(
        lambda *args: callback.flag(args, flag_option="Up", username=gTop[1]),
        [text_input],
        None,
    )
    image2_up.click(
        lambda *args: callback.flag(args, flag_option="Up", username=gTop[2]),
        [text_input],
        None,
    )
    image3_up.click(
        lambda *args: callback.flag(args, flag_option="Up", username=gTop[3]),
        [text_input],
        None,
    )
    image4_up.click(
        lambda *args: callback.flag(args, flag_option="Up", username=gTop[4]),
        [text_input],
        None,
    )
    image0_up.click(
        lambda *args: callback.flag(args, flag_option="Up", username=gTop[0]),
        [text_input],
        None,
    )
    image1_down.click(
        lambda *args: callback.flag(args, flag_option="Down", username=gTop[1]),
        [text_input],
        None,
    )
    image2_down.click(
        lambda *args: callback.flag(args, flag_option="Down", username=gTop[2]),
        [text_input],
        None,
    )
    image3_down.click(
        lambda *args: callback.flag(args, flag_option="Down", username=gTop[3]),
        [text_input],
        None,
    )
    image4_down.click(
        lambda *args: callback.flag(args, flag_option="Down", username=gTop[4]),
        [text_input],
        None,
    )
    image0_down.click(
        lambda *args: callback.flag(args, flag_option="Down", username=gTop[0]),
        [text_input],
        None,
    )
    image1_flag.click(
        lambda *args: callback.flag(args, flag_option="Flag", username=gTop[1]),
        [text_input],
        None,
    )
    image2_flag.click(
        lambda *args: callback.flag(args, flag_option="Flag", username=gTop[2]),
        [text_input],
        None,
    )
    image3_flag.click(
        lambda *args: callback.flag(args, flag_option="Flag", username=gTop[3]),
        [text_input],
        None,
    )
    image4_flag.click(
        lambda *args: callback.flag(args, flag_option="Flag", username=gTop[4]),
        [text_input],
        None,
    )
    image0_flag.click(
        lambda *args: callback.flag(args, flag_option="Flag", username=gTop[0]),
        [text_input],
        None,
    )

demo.launch(debug=False)

