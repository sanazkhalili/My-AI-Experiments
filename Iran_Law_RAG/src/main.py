import sys
from pathlib import Path
import gradio as gr

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from generating_llm import chat_with_model
import os


os.environ["NO_PROXY"] = "127.0.0.1,localhost"
os.environ["no_proxy"] = "127.0.0.1,localhost"

css = """
textarea {
    direction: rtl !important;
    text-align: right !important;
}
"""
with gr.Blocks(title="سامانه پرسش و پاسخ قانون اساسی",
               theme=gr.themes.Soft(),css=css) as demo:

    gr.Markdown(
            """
        <div style="text-align:right; direction:rtl;">

        # سامانه پرسش و پاسخ قانون اساسی

        سوال خود را به زبان فارسی وارد کنید.

        </div>
        """
    )

    with gr.Row():

       
        with gr.Column(scale=6):

            answer = gr.Textbox(
                label="پاسخ",
                lines=18,
                max_lines=25,
                interactive=False,
            )

        with gr.Column(scale=4):

            msg = gr.Textbox(
                label="سوال",
                placeholder="مثلاً: آیا تحصیل در ایران رایگان است؟",
                lines=2
            )

            send_btn = gr.Button(
                "ارسال",
                variant="primary"
            )

    send_btn.click(
        fn=chat_with_model,
        inputs=msg,
        outputs=answer
    )

    msg.submit(
        fn=chat_with_model,
        inputs=msg,
        outputs=answer
    )

demo.launch()