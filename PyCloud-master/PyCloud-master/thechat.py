#coding=utf8
import itchat
import cloud
import music
import baike
import os, shutil

users = {}
ifpic = {}
welcome = "<进入词云功能>，目前提供：\n1.输入文本（或传输文件）生成词云\n2.输入歌手，生成网易云热评词云\n3.输入关键词,生成百度百科词云\n\n请输入功能序号获取相应功能(1、2或3)\n\n(在任意阶段输入‘07624’返回初始状态)"
step_1_1 = "<进入输入模式>\n请输入文本或发送txt文档作为词云输入"
step_1_2 = "若需要指定词云轮廓，请发送相应背景图，否则发送'n'"
step_2_1 = "<进入热评模式>\n请输入歌手名"
step_3_1 = "<进入百度模式>\n请输入关键词"
wait = "词云生成中，请稍候"
wrong = "输入错误，请重试"
sorry = "抱歉，词云生成失败，请更换条件"
askChange = "词云生成成功\n是否进入<自定义模式>进行进一步的修改（y/n），进入自定义将提供模板修改对应参数"
model = "轮廓or颜色=轮廓\n轮廓阈值(0~1)=0.5\n屏蔽字=['首歌','其它什么词']\n背景色(0为白色，1为黑色)=0\n"
bye = "感谢您的使用！"

@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def text_reply(msg):
    if msg['ToUserName']=='filehelper':
        msg['FromUserName'] = 'filehelper'
    user = msg['FromUserName']
    cont = msg['Content']
    if (user == "@5447635807faded07343a2469f478ca103caa5e17e0b590d9e044fe3fb955c0a"):
        itchat.send("滚蛋傻逼", toUserName=user)
    if user in users.keys():
        print(user+ " "+cont)
    if ( cont.startswith('07624')):
        if not os.path.exists('data/'+user):
            os.makedirs('data/'+user)
            # shutil.copyfile('data/default.jpg','data/'+user+'/img.jpg') 
        users[user] = 100
        ifpic[user] = 'data/'+user+'/img.jpg'
        print(user+" "+cont)
        itchat.send(welcome,toUserName=user)
    elif (user in users.keys()) and (users[user]==100):
        if cont == '1':
            users[user] = 1
            itchat.send(step_1_1,toUserName=user)
        elif cont == '2':
            users[user] = 2
            itchat.send(step_2_1,toUserName=user)
        elif cont == '3':
            users[user] = 3
            itchat.send(step_3_1,toUserName=user)
        # else:
        #     itchat.send(wrong,toUserName=user)

    elif (user in users.keys()) and (users[user]==1):
        print(user+" "+cont)
        try:
            f = open('data/'+user+'/comment.txt', 'a+')
            f.seek(0)
            f.truncate()
            f.write(cont)
            users[user] = 11
            itchat.send(step_1_2, toUserName=user)
        except:
            itchat.send(wrong, toUserName=user)

    elif (user in users.keys()) and (users[user]==11):
        if cont=='n' or cont=='N':
            ifpic[user] = None
            itchat.send(wait, toUserName=user)
            try:
                print(ifpic[user])
                cloud.draw_wordcloud(file_name='data/'+user+'/comment.txt', usr=user,
                    masker=ifpic[user])
                # itchat.send('@img@data/'+user+'/img.jpg' ,toUserName=user)
                itchat.send('@img@data/'+user+'/result.jpg' ,toUserName=user)
                itchat.send(askChange, toUserName=user)
                users[user] = 99
            except:
                itchat.send('词云生成失败，请检查文本文件...', toUserName=user)
                users[user] = 1


    elif (user in users.keys()) and (users[user]==2):
        itchat.send(wait,toUserName=user)
        if music.singer_craw(cont,usr=user) != 0:
            itchat.send(sorry+'\n未找到歌手',toUserName=user)
        else:
            try:
                cloud.draw_wordcloud(file_name='data/'+user+'/comment.txt', usr=user,
                    masker=ifpic[user])
                itchat.send('@img@data/'+user+'/img.jpg' ,toUserName=user)
                itchat.send('@img@data/'+user+'/result.jpg' ,toUserName=user)
                itchat.send(askChange,toUserName=user)
                users[user] = 99
            except:
                itchat.send(sorry,toUserName=user)

    elif (user in users.keys()) and (users[user]==3):
        itchat.send(wait,toUserName=user)
        if baike.getBaikeText(cont,usr=user) == None:
            itchat.send(sorry+'\n未找到关键词',toUserName=user)
        else:
            pic = baike.getgBaikePhoto(cont,usr=user)
            try:
                cloud.draw_wordcloud(file_name='data/'+user+'/comment.txt', usr=user,
                    masker=pic)
                if pic!=None:
                    itchat.send('@img@'+pic ,toUserName=user)
                itchat.send('@img@data/'+user+'/result.jpg' ,toUserName=user)
                itchat.send(askChange,toUserName=user)
                users[user] = 99
            except:
                itchat.send(sorry,toUserName=user)

    elif (user in users.keys()) and (users[user]==99):
        if (cont.lower().startswith('y')):
            itchat.send(model,toUserName=user)
            users[user] = 199
        elif (cont.lower().startswith('n')):
            itchat.send(bye,toUserName=user)

    elif (user in users.keys()) and (users[user]==199):
        contl = cont.split('\n')
        simple = True
        val = 0.5
        stop = []
        back = 'white'
        ret = ""
        for c in contl:
            if c.startswith('轮廓or颜色='):
                if (c.lstrip('轮廓or颜色').lstrip('=')=='轮廓'):
                    simple = True
                elif (c.lstrip('轮廓or颜色').lstrip('=')=='颜色'):
                    simple = False
                else:
                    ret += c + "： ’轮廓or颜色‘错误参数，使用默认值\n"
            elif c.startswith('轮廓阈值(0~1)='):
                try:
                    val = float(c.lstrip('轮廓阈值(0~1)').lstrip('='))
                except:
                    ret += c + ": '轮廓阈值(0~1)'参数错误，使用默认值\n"
            elif c.startswith('屏蔽字='):
                try:
                    l = eval(c.lstrip('屏蔽字').lstrip('='))
                except:
                    ret += c + ": 参数错误，注意不要用中文逗号、引号、括号\n"
                    l = None
                if (type(l)!=type(stop)):
                    ret += c + ": '屏蔽词'参数错误\n"
                else:
                    stop = l
            elif c.startswith('背景色(0为白色，1为黑色)='):
                if c.lstrip('背景色(0为白色，1为黑色)').lstrip('=')=='1':
                    back = 'black'
            else:
                ret += c + ": 键值错误，忽略\n"
        try:
            cloud.draw_wordcloud(file_name='data/'+user+'/comment.txt', usr=user,
                masker=ifpic[user], background=back,
                simple=simple, masker_val=val, stopword=stop)
            # itchat.send('@img@data/'+user+'/img.jpg' ,toUserName=user)
            itchat.send('@img@data/'+user+'/result.jpg' ,toUserName=user)
            ret += askChange
            users[user] = 99
        except:
            ret += wrong
        finally:
            itchat.send(ret, toUserName=user)


                

@itchat.msg_register(itchat.content.ATTACHMENT, isFriendChat=True)
def download_files(msg):
    if msg['ToUserName']=='filehelper':
        msg['FromUserName'] = 'filehelper'
    user = msg['FromUserName']
    if (user in users.keys()) and (users[user]==1):
        if not os.path.exists('data/'+user):
            os.makedirs('data/'+user)
        msg['Text']('data/'+user+'/comment.txt')
        itchat.send(step_1_2, toUserName=user)
        users[user] = 11


@itchat.msg_register(itchat.content.PICTURE, isFriendChat=True)
def download_pic(msg):
    if msg['ToUserName']=='filehelper':
        msg['FromUserName'] = 'filehelper'
    user = msg['FromUserName']
    if (user in users.keys()) and (users[user]==11):
        if not os.path.exists('data/'+user):
            os.makedirs('data/'+user)
        msg['Text']('data/'+user+'/img.jpg')
        itchat.send(wait, toUserName=user)
        try:
            cloud.draw_wordcloud(file_name='data/'+user+'/comment.txt', usr=user,
                masker='data/'+user+'/img.jpg')
            # itchat.send('@img@data/'+user+'/img.jpg' ,toUserName=user)
            itchat.send('@img@data/'+user+'/result.jpg' ,toUserName=user)
            itchat.send(askChange, toUserName=user)
            users[user] = 99
        except:
            itchat.send('词云生成失败，请检查文本文件...', toUserName=user)
            users[user] = 1



itchat.auto_login(hotReload=True)

itchat.run()