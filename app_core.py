from __future__ import unicode_literals
import os
import re
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from imgurpython import ImgurClient
import random
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('Line的Cahannel access token')
handler = WebhookHandler('Line的Channel Secret')


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
   
    if re.search(r"(牛|奶)", event.message.text, re.DOTALL):
        clientTemp= ImgurClient('Imgur的clientid', 'Imgur的clientSecreat')
        images = clientTemp.get_album_images('Imgur Album Hash')
        imageUrls = []
	
        for image in images:
                imageUrls.append(image.link)
        randomNum = random.randint(1, imageUrls.__len__())
        imgUrl = imageUrls[randomNum - 1]
        
        message = ImageSendMessage(
                original_content_url=imgUrl,
                preview_image_url=imgUrl
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0

if __name__ == "__main__":
    app.run()
