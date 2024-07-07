### 基于itchat实现批量发送祝福给微信好友

本文主要是实现获取微信好友列表，将备注信息和祝福语写入贺卡内，并加入了随机背景图和文案，让好友接收到新年祝福贺卡。

#### 1. 实现思路

1. 微信后台登录
2. 获取微信好友的备注`friend.RemarkName`
3. 将好友备注用`_`进行分隔，仅保留`_`后的昵称
4. 生成贺卡图片
5. 批量发送图片给对应好友（建议批量发送时加`time.sleep()`避免微信限制）

#### 2. 版本1（鼠年）

```python
from PIL import Image, ImageDraw, ImageFont
import glob
import itchat
import pandas as pd
import numpy as np

# 微信自动登录
itchat.auto_login(hotReload=True)

# 祝福语版本1
def generatePic1(send,name):
    pattern = 'new1.jpg'
    setFont = ImageFont.truetype('simkai.ttf', 190)
    fillColor = "black"
    for img in glob.glob(pattern):
        image = Image.open(img)
        if image.mode == "P":
            image = image.convert('RGB')
        draw = ImageDraw.Draw(image)
        draw.text((900, 920), u' '+send+'祝'+str(name)+'：',font=setFont,fill=fillColor)
        mywidth,myheight,lineheight = 1000,1300,350
        draw.text((mywidth, myheight), u'喜乐平安，诸事顺遂，', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight), u'岁华新至，除夕乐融，', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight*2), u'吉吉利利，百事如意，', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight*3), u'家兴百和，万福骈臻。', font=setFont, fill=fillColor)
        image.save('images\\'+str(name)+".jpg")
# 祝福语版本2
def generatePic2(send,name):
    pattern = 'new2.jpg'
    setFont = ImageFont.truetype('simkai.ttf', 190)
    fillColor = "white"
    for img in glob.glob(pattern):
        image = Image.open(img)
        if image.mode == "P":
            image = image.convert('RGB')
        draw = ImageDraw.Draw(image)
        draw.text((1400, 900), u'新年之际', font=setFont, fill=fillColor)
        draw.text((800, 1200), u' '+send+'祝'+str(name)+'：',font=setFont,fill=fillColor)
        mywidth,myheight,lineheight = 1100,1500,280

        draw.text((mywidth, myheight), u'劝君今夕不须眠。', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight), u'且满满，泛觥船。', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight*2), u'大家沈醉对芳筵。', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight*3), u'愿新年，胜旧年。', font=setFont, fill=fillColor)

        draw.text((mywidth+500, myheight+lineheight*4), u'——《双雁儿(除夕)》', font=setFont, fill=fillColor)
        image.save('images\\'+str(name)+".jpg")
# 祝福语英语版本1
def generatePicEnglish1(name):
    pattern = 'new2.jpg'
    setFont = ImageFont.truetype('simkai.ttf', 130)
    fillColor = "white"
    for img in glob.glob(pattern):
        image = Image.open(img)
        if image.mode == "P":
            image = image.convert('RGB')
        draw = ImageDraw.Draw(image)
        draw.text((1300, 900), u'Happy New Year', font=setFont, fill=fillColor)
        draw.text((500, 1700), u'To '+str(name)+':',font=setFont,fill=fillColor)
        mywidth,myheight,lineheight = 700,1900,200
        draw.text((mywidth, myheight), u'At New Year and always,may peace ', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight), u'and love fill your heart,beauty', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight*2), u'fill your world, and contentment ', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight*3), u'and joy fill your days.', font=setFont, fill=fillColor)

        draw.text((mywidth+1800, myheight+lineheight*4), u'Junming', font=setFont, fill=fillColor)
        image.save('images\\'+str(name)+".jpg")
# 祝福语英语版本2
def generatePicEnglish2(name):
    pattern = 'new1.jpg'
    setFont = ImageFont.truetype('simkai.ttf', 130)
    fillColor = "black"
    for img in glob.glob(pattern):
        image = Image.open(img)
        if image.mode == "P":
            image = image.convert('RGB')
        draw = ImageDraw.Draw(image)
        draw.text((1300, 900), u'Happy New Year', font=setFont, fill=fillColor)
        draw.text((600, 1500), u'Dear '+str(name)+':',font=setFont,fill=fillColor)
        mywidth,myheight,lineheight = 800,1700,200
        draw.text((mywidth, myheight), u'Wishing you a sparkling New Year', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight), u'and bright happy New Year!', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight*2), u'May the season bring much pleasure', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight*3), u'to you! ', font=setFont, fill=fillColor)

        draw.text((mywidth+1600, myheight+lineheight*4.3), u'Junming', font=setFont, fill=fillColor)
        image.save('images\\'+str(name)+".jpg")
# 设置发件人与收件人列表（自定义）
def diyyourcard(send,revlist):
    for i in revlist:
        if np.random.random() > 0.5:
            generatePic1(send,i)
        else:
            generatePic2(send,i)
            
diyyourcard(send,revlist)

# 生成所有好友图片
def gengerateAllPic():
    friends = pd.read_csv('remarkname.csv',encoding='gbk')['name']
    for i in friends:
        if np.random.random()> 0.5:
            generatePic1(i)
        else:
            generatePic2(i)

# 获取所有好友备注信息
def getallinfo():
    friends = itchat.get_friends(update=True)[:]
    namedf = pd.DataFrame()
    namelist = []
    for i in friends:
        if len(i.RemarkName)!=0:
            namelist.append(i.RemarkName)
    namedf['name'] = namelist
    namedf.to_csv('realname.csv',index=None,encoding='gbk')
# getallinfo()

# 查看所有朋友的全部详细信息
# print(friends)

# 获取备注名字
# for i in friends:
#     print(i.RemarkName,'\t')

# 指定发送对象（备注名）
# RemarkNames = ['a1文杰']

# 发送祝福语
# for person in RemarkNames:
#     users=itchat.search_friends(person)
#     userName= users[0]['UserName']
#     picfile = generatePic(person[-2:])
#     # 发送文字
#     try:
#         itchat.send('Hey'+person[-2:]+'~ Happy New Year!', toUserName=userName)
#         print("发送给" + person + "的祝福语文字 成功")
#     except:
#         print("发送给"+person+"的祝福语文字 失败")
#     # 发送图片
#     try:
#         itchat.send_image(picfile,toUserName=userName)
#         print("发送给"+person+"的祝福语图片 成功")
#     except:
#         print("发送给"+person+"的祝福语图片 失败")

```

#### 3. 版本2（牛年）

```python
from PIL import Image, ImageDraw, ImageFont
import glob
import itchat
import random
import time
# 微信自动登录
itchat.auto_login(hotReload=True)

# 文字祝福语
blessing_word_list = [
    '牛年快乐！命途风霜尽，乾坤气象和，历添新岁月，福满旧山河。 [福][跳跳][庆祝]',
    '牛年快乐！所念皆如意，未来皆可期，仍有阳光满路，温暖如初。 [福][跳跳][庆祝]',
    '牛年快乐！喜庆期盼，不负爱意，慢品人间烟火，闲看人间岁月长。 [福][跳跳][庆祝]',
    '牛年快乐！多喜乐，长安宁，祈沐暖阳，盼所愿成所得，所遇为知己。 [福][跳跳][庆祝]',
    '牛年快乐！喜乐平安，诸事顺遂，岁华新至，除夕乐融，家兴百和，万福骈臻。 [福][跳跳][庆祝]',
    '牛年快乐！劝君今夕不须眠，且满满，泛觥船，大家沈醉对芳筵，愿新年，胜旧年。——《双雁儿(除夕)》 [福][跳跳][庆祝]',
    '牛年快乐！爆竹声中一岁除，春风送暖入屠苏。千门万户曈曈日，总把新桃换旧符。——王安石《元日》 [福][跳跳][庆祝]'
]


# 自动发送新年快乐消息
def send_happy_new_year_msg():
    friends = itchat.get_friends(update=True)[:]
    pattern = 'card.jpg'
    font_type = ImageFont.truetype('new_year.ttf', 88)
    font_color = 'white'

    for friend in friends:
        if len(friend.RemarkName) != 0:
            remark_name = friend.RemarkName

            if '_' in remark_name:
                real_name = str(remark_name).split('_')[-1]
                to_word = f'祝 {real_name} {random.choice(blessing_word_list)}'
                print(to_word)

                # 生成祝福文字
                users = itchat.search_friends(remark_name)
                userName = users[0]['UserName']

                # 发送祝福文字
                itchat.send(to_word, toUserName=userName)
                itchat.send('[烟花]', toUserName=userName)
                time.sleep(5)
                # 生成祝福图片
                for img in glob.glob(pattern):
                    image = Image.open(img)
                    init_pic_word_loc = 50
                    if image.mode == "P":
                        image = image.convert('RGB')
                    draw = ImageDraw.Draw(image)
                    words = '新的一年丶祝愿' + str(real_name)

                    for word in words:
                        draw.text((125, init_pic_word_loc), u' ' + word, font=font_type, fill=font_color)
                        init_pic_word_loc += 66
                    image.save('images\\' + str(real_name) + ".jpg")

                # 发生祝福图片
                itchat.send_image('images\\' + str(real_name) + ".jpg", toUserName=userName)
                time.sleep(3)


if __name__ == '__main__':
    send_happy_new_year_msg()

```

#### 4. 效果预览

![](https://github.com/jm199504/New-Year-Card/blob/master/images/lawrence.jpg?raw=true)

![](https://github.com/jm199504/New-Year-Card/blob/master/images/axian.jpg?raw=true)
