from PIL import Image
import math
def ec(t,pw_1,pw_2,pw_3,pw_4,pw_5):
    wd = math.ceil(len(t)**0.5)
    wd = wd + 1
    picture = Image.new("RGB",(wd,wd),0x0)
    x,y = 0,0
    for i in t:
        word = ord(i) + pw_5
        rgb = (pw_1, (word & 0xFF00) >> 8, word & 0xFF)
        picture.putpixel((x,y), rgb)
        if x == wd - 2:
            x = 0
            y += 1
        else:
            x += 1
    picture.putpixel((wd-1,wd-1),(pw_1,pw_1,pw_1))
    picture.putpixel((wd-1,wd-2),(pw_2,pw_3,pw_4))
    picture.putpixel((wd-2,wd-1),(pw_4,pw_3,pw_2))
    return picture
def dc(p,pw_1,pw_2,pw_3,pw_4,pw_5):
    w,h = p.size
    if p.getpixel((w-1,h-1))==(pw_1,pw_1,pw_1):
        if p.getpixel((w-1,h-2))==(pw_2,pw_3,pw_4):
            if p.getpixel((w-2,h-1))==(pw_4,pw_3,pw_2):
                lst = []
                for y in range(h):
                    for x in range(w):
                        r,g,b = p.getpixel((x,y))
                        if (b|g|r) == 0:
                            break
                        index = (g << 8) + b
                        lst.append(chr(index-pw_5))
                re = ''.join(lst)
            else:
                re = str('密码错误，解密失败！')
        else:
            re = str('密码错误，解密失败！')
    else:
        re = str('密码错误，解密失败！')
    return re
def cpw(p,pw_1,pw_2,pw_3,pw_4,pw_5):
    w,h = p.size
    if p.getpixel((w-1,h-1))==(pw_1,pw_1,pw_1):
        if p.getpixel((w-1,h-2))==(pw_2,pw_3,pw_4):
            if p.getpixel((w-2,h-1))==(pw_4,pw_3,pw_2):
                print('密码验证成功！\n')
                lst = []
                for y in range(h):
                    for x in range(w):
                        r,g,b = p.getpixel((x,y))
                        if (b|g|r) == 0:
                            break
                        index = (g << 8) + b
                        lst.append(chr(index-pw_5))
                tmp = ''.join(lst)
                picture = Image.new("RGB",(w,h),0x0)
                Pw_1 = int(input('请输入随机数作为新加密密码（0~255）[01]：'))
                Pw_2 = int(input('请输入随机数作为新加密密码（0~255）[02]：'))
                Pw_3 = int(input('请输入随机数作为新加密密码（0~255）[03]：'))
                Pw_4 = int(input('请输入随机数作为新加密密码（0~255）[04]：'))
                Pw_5 = int(input('请输入随机数作为新数据位移码（0~3）：'))
                x,y = 0,0
                for i in tmp:
                    word = ord(i) + Pw_5
                    rgb = (Pw_1, (word & 0xFF00) >> 8, word & 0xFF)
                    picture.putpixel((x,y), rgb)
                    if x == w - 2:
                        x = 0
                        y += 1
                    else:
                        x += 1
                picture.putpixel((w-1,h-1),(Pw_1,Pw_1,Pw_1))
                picture.putpixel((w-1,h-2),(Pw_2,Pw_3,Pw_4))
                picture.putpixel((w-2,h-1),(Pw_4,Pw_3,Pw_2))
                re = str('图片密码更改成功，保存至应用程序目录下的“new_passwd.bmp”！')
                passwd = str(hex(Pw_1)) +' '+ str(hex(Pw_2)) +' '+ str(hex(Pw_3)) +' '+ str(hex(Pw_4)) +' '+ str(bin(Pw_5))
                print('文件已保存至应用目录下的“locked.bmp”。解密密码（空格不能少！）：' + passwd)
            else:
                re = str('密码错误，修改失败！')
        else:
            re = str('密码错误，修改失败！')
    else:
        re = str('密码错误，修改失败！')
    print(re)
    return picture
if __name__ == '__main__':
    print('按照提示输入数据，请勿作死！如果程序闪退，可能是程序出错。请尝试重新运行或联系作者。by：024026008 可以在bilibili联系我。')
    print('原作者（GitHub）：3150601355')
    print('BUG?不存在的！（手动滑稽）\n')
    while True:
        choose = str(input('\n1：退出；\n2：加密；\n3：解密；\n4：修改密码。\n输入数字选择：'))
        if choose == '1':
            break
        elif choose == '2':
            filename1 = input('请输入文件位置：')
            Pw_1 = int(input('请输入随机数作为加密密码（0~255）[01]：'))
            Pw_2 = int(input('请输入随机数作为加密密码（0~255）[02]：'))
            Pw_3 = int(input('请输入随机数作为加密密码（0~255）[03]：'))
            Pw_4 = int(input('请输入随机数作为加密密码（0~255）[04]：'))
            Pw_5 = int(input('请输入随机数作为数据位移码（0~3）：'))
            with open(filename1,encoding="UTF-8") as f1:
                whole_text1 = f1.read()
            im1 = ec(whole_text1,Pw_1,Pw_2,Pw_3,Pw_4,Pw_5)
            im1.save("locked.bmp")
            passwd1 = str(hex(Pw_1)) +' '+ str(hex(Pw_2)) +' '+ str(hex(Pw_3)) +' '+ str(hex(Pw_4)) +' '+ str(bin(Pw_5))
            print('文件已保存至应用目录下的“locked.bmp”。解密密码（空格不能少！）：' + passwd1)
        elif choose == '3':
            filename2 = input('请输入文件位置：')
            passwd2 = input('请输入密码(格式：aaaa bbbb cccc dddd eeee ffff)：')
            pwlist1 = passwd2.split(' ')
            whole_text2 = dc(Image.open(filename2,"r"),int(pwlist1[0],16),int(pwlist1[1],16),int(pwlist1[2],16),int(pwlist1[3],16),int(pwlist1[4],2))
            with open("unlocked.txt","w",encoding = "UTF-8") as f2:
                f2.write(whole_text2)
            print('文件已保存至应用目录下的“unlocked.txt”。')
        elif choose == '4':
            filename3 = input('请输入文件位置：')
            passwd3 = input('请输入旧密码(格式：aaaa bbbb cccc dddd eeee ffff)：')
            pwlist2 = passwd3.split(' ')
            im2 = cpw(Image.open(filename3,"r"),int(pwlist2[0],16),int(pwlist2[1],16),int(pwlist2[2],16),int(pwlist2[3],16),int(pwlist2[4],2))
            im2.save("new_passwd.bmp")
        else:
            print('???请正确使用，谢谢！')
