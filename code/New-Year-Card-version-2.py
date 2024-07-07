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
