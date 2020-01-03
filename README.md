概述：基于Python自动生成祝福贺卡

<!--more-->

发送邮件无创意，本文将实现自创实现祝福贺卡/祝福语，摆脱手敲收件人名。

备注：背景图片来源 https://www.tukuppt.com/ 

# 实现代码

根据代码指示安装相应的库文件

例如 pip install itchat 等

```python
from PIL import Image, ImageDraw, ImageFont
import glob
import itchat

# 微信自动登录
itchat.auto_login(hotReload=True)

# 写入祝福语
def generatePic(name):
    pattern = 'news.jpg'
    setFont = ImageFont.truetype('simkai.ttf', 35)
    fillColor = "red"
    for img in glob.glob(pattern):
        image = Image.open(img)
        if image.mode == "P":
            image = image.convert('RGB')
        draw = ImageDraw.Draw(image)
        draw.text((200, 370), u'祝愿'+name+'：',font=setFont,fill=fillColor)
        mywidth,myheight,lineheight = 235,460,70
        draw.text((mywidth, myheight), u'岁华新至，除夕乐融，', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight), u'喜乐平安，诸事顺遂，', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight*2), u'吉吉利利，百事如意，', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight*3), u'家兴百和，万福骈臻。', font=setFont, fill=fillColor)
        draw.text((mywidth, myheight+lineheight*5), u'署名', font=setFont, fill=fillColor)
        image.save("mycard2.jpg")
    return "mycard2.jpg"

# 获取好友信息
friends = itchat.get_friends(update=True)[:]

# 查看所有朋友的全部详细信息
# print(friends)

# 获取备注名字
# for i in friends:
#     print(i.RemarkName,'\t')

# 指定发送对象（备注名）
RemarkNames = ['a1文杰']

# 发送祝福语
for person in RemarkNames:
    users=itchat.search_friends(person)
    userName= users[0]['UserName']
    picfile = generatePic(person[-2:])

    # 发送文字
    try:
        itchat.send('Hey'+person[-2:]+'~ Happy New Year!', toUserName=userName)
        print("发送给" + person + "的祝福语文字 成功")
    except:
        print("发送给"+person+"的祝福语文字 失败")

    # 发送图片
    try:
        itchat.send_image(picfile,toUserName=userName)
        print("发送给"+person+"的祝福语图片 成功")
    except:
        print("发送给"+person+"的祝福语图片 失败")
```

# 效果图

![](/images/card1.png)

<img src="/images/card2.jpg" style="width:300px;" />