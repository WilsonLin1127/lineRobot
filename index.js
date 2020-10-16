import { Client, middleware } from '@line/bot-sdk';
import express from 'express';

const lineConfig = {
    channelAccessToken: process.env.CHANNEL_ACCESS_TOKEN || '方便自己開發用的，不然已經設定好heroku condig var 是不用再另外assign的',
    channelSecret: process.env.CHANNEL_SECRET || '同上'
};

const client = new Client(lineConfig);
const app = express();

app.post('/', middleware(lineConfig), async (req, res) => {
    try {
        /*{  req.body長這樣
            "events": [
                {
                    "type": "message",
                    "replyToken": "uuidhere",
                    "source": {
                        "userId": "xxxx"",
                        "type": "user"
                    },
                    "timestamp": 1592813446208,
                    "mode": "active",
                    "message": {
                        "type": "text",
                        "id": "12188948022060",
                        "text": "X"
                    }
                }
            ],
            "destination": "xxx"
        }*/
        let result = await req.body.events.map(handleEvent);
        res.json(result);
    }
    catch (err) {
        console.log(err);
    }
});

const handleEvent = (event) => {
    switch (event.type) {
    case 'join': //這隻機器人加入別人的群組
        break;
    case 'follow': //追蹤這隻機器人
        break;
    case 'message': //傳訊息給機器人
        switch (event.message.type) {
        case 'text':
            textHandler(event.replyToken, event.message.text);   //測試code就不用這行
//             return client.replyMessage(replyToken, {     ---->    測試用code通常就是呼叫client.replyMessage，並依api要求格式回傳
//                 type: 'text',
//                 text: event.message.text  ----> 我們傳給機器人的文字會在這裡面
//             });
            break;
        case 'sticker':
            // do sth with sticker
            return 
        }
    }
}

const textHandler = (replyToken, inputText) => {
    try{
        let resText;
        switch (inputText) {
            case '你好':
                resText = '你好啊';
                break;
            case 'test':
                resText = `測試`;
                break
//             case 'Q&A':
//                 return client.replyMessage(replyToken, imageMap());
//             case 'q&a':
//                 return client.replyMessage(replyToken, carousel());
            default:
                resText = '請親臨院所';
        }
        return client.replyMessage(replyToken, {
            type: 'text',
            text: resText
        });
    } catch (err) {
        console.log(err)
    }

}


const port = process.env.PORT || 3000;  //heroku 會自己隨機給你一個port，所以不能寫死，3000是另外測試用，會在後面提到
app.listen(port, () => {
    console.log(`App now running on port ${port}`);
});
