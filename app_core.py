from __future__ import unicode_literals
import os
import re
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('YOUR_LineBot_Channel access token')
handler = WebhookHandler('YOUR_LineBot_Channel secret')


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# SEND MESSAGE
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    '''學你講話
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )
    '''
    #給一張圖
    if re.search(r"(牛|厲害|強|猛)", event.message.text, re.DOTALL):
        message = ImageSendMessage(
            original_content_url='https://i.imgur.com/PPJOlv8.jpg',
            preview_image_url='https://i.imgur.com/PPJOlv8.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    
if __name__ == "__main__":
    app.run()
