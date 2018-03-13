#coding=utf8
import itchat

'''
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
'''
itchat.auto_login(hotReload=True)
#itchat.run()

#获取公众号发送
mps = itchat.get_mps()
mps = itchat.search_mps(name=u'XX')#XX为公众号所含汉字
print(mps)
publicName = mps[0]['UserName']
itchat.send(u' 新年快乐！', toUserName=publicName)

#获取好友发送
#users = itchat.search_friends(name='')
users = itchat.get_friends()
#获取好友全部信息,返回一个列表,列表内是一个字典
print(users)
#获取`UserName`,用于发送消息
for user in users:
    userName = user['UserName']
    remarkName = user['RemarkName']#昵称
    itchat.send(remarkName+u' 新年快乐！', toUserName=userName)


