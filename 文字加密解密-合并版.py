from PIL import Image
import math
def ec(t,pw_1,pw_2,pw_3,pw_4,pw_5):
    wd = math.ceil(len(t)**0.5)
    picture = Image.new("RGB",(wd+1,wd),0x0)
    x,y = 0,0
    for i in t:
        word = ord(i) + pw_5
        rgb = (pw_1, (word & 0xFF00) >> 8, word & 0xFF)
        picture.putpixel((x,y), rgb)
        if x == wd - 1:
            x = 0
            y += 1
        else:
            x += 1
    picture.putpixel((wd,wd-1),(pw_1,pw_1,pw_1))
    picture.putpixel((wd,wd-2),(pw_2,pw_3,pw_4))
    picture.putpixel((wd-1,wd-1),(pw_4,pw_3,pw_2))
    return picture
def dc(p,pw_1,pw_2,pw_3,pw_4,pw_5):
    w,h = p.size
    if p.getpixel((w-1,h-1))==(pw_1,pw_1,pw_1):
        if p.getpixel((w-1,h-2))==(pw_2,pw_3,pw_4):
            if p.getpixel((w-2,h-1))==(pw_4,pw_3,pw_2):
                lst = []
                for y in range(h):
                    for x in range(w-1):
                        r,g,b = p.getpixel((x,y))
                        if (b|g|r) == 0:
                            break
                        index = (g << 8) + b
                        lst.append(chr(index-pw_5))
                return ''.join(lst)
            else:
                pass
        else:
            pass
    else:
        pass
if __name__ == '__main__':
    print('按照提示输入数据，请勿作死！如果程序闪退，可能是程序出错。请尝试重新运行或联系作者。by：024026008 可以在bilibili联系我。')
    print('原作者（GitHub）：3150601355')
    print('BUG?不存在的！（手动滑稽）\n')
    while True:
        choose = str(input('1：加密；2：解密；3：退出。输入数字选择：'))
        if choose == '1':
            filename1 = input('请输入文件位置：')
            Pw_1 = int(input('请输入随机数作为加密密码（0~255）[01]：'))
            Pw_2 = int(input('请输入随机数作为加密密码（0~255）[02]：'))
            Pw_3 = int(input('请输入随机数作为加密密码（0~255）[03]：'))
            Pw_4 = int(input('请输入随机数作为加密密码（0~255）[04]：'))
            Pw_5 = int(input('请输入随机数作为数据位移码（0~3）：'))
            with open(filename1,encoding="UTF-8") as f1:
                whole_text1 = f1.read()
            im = ec(whole_text,Pw_1,Pw_2,Pw_3,Pw_4,Pw_5)
            im.save("output.bmp")
            passwd = str(hex(Pw_1)) +' '+ str(hex(Pw_2)) +' '+ str(hex(Pw_3)) +' '+ str(hex(Pw_4)) +' '+ str(bin(Pw_5))
            print('文件已保存。解密密码（空格不能少！）：' + passwd)
        elif choose == '2':
            filename2 = input('请输入文件位置：')
            passwd = input('请输入密码：')
            pwlist = passwd.split(' ')
            whole_text2 = dc(Image.open(filename2,"r"),int(pwlist[0],16),int(pwlist[1],16),int(pwlist[2],16),int(pwlist[3],16),int(pwlist[4],2))
            with open("output.txt","w",encoding = "UTF-8") as f2:
                f2.write(whole_text2)
        elif choose == '3':
            break
        else:
            print('???请正确使用，谢谢！')
