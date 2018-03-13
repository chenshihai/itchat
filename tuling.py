#coding=utf8
import requests
import itchat
KEY = '8edce3ce905a4c1dbb965e6b35c3834d'


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,# 如果这个Tuling Key不能用，那就换一个
        'info': msg,# 这是我们发出去的消息
        'userid': 'wechat-robot',# 这里你想改什么都可以
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        print(r)
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = u'我收到: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply

itchat.auto_login(hotReload=True)
itchat.run()
