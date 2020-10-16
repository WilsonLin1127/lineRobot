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

line_bot_api = LineBotApi('JxYa21gOuIjs09JFA+adfQ7KCQfm3X4AiBQ0whm6W0Hylj45WvmOLtfLRl04k3vSp4cYBpLAog7bKjgzqgCpxHdCsGdVlMZDy2W6vSDHOCfs0v6W5kG/zhsa7pAZCERvFfCMOgBxcyzMeLSq/QvKogdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('829c5c213b21463ee6dc1018d83eb522')


@app.route("/")
def home():
    return 'home OK'

# 監聽所有來自 /callback 的 Post Request
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


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
    