# LINE聊天機器人
# SDK = software development kit

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)
-
line_bot_api = LineBotApi('mhV/tCvDn/hAzG/2cGMQv9GIw18FibfE4Uzasn6B6lcO8MUUGlsiGVFyZJE1S7egHJogkJTzCIhkmx5mlMtAV3+JEzv9uaLoJ4yQwzEXgBeyPhFi5GIi3kkhBxL5J4bv+2pFegCLMlnj8+7koyov/gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f1118d5071742a42b574de679b0d707e')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()