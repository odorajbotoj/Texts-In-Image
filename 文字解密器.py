from PIL import Image

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
    filename = input('请输入文件位置：')
    passwd = input('请输入密码：')
    pwlist = passwd.split(' ')
    whole_text = dc(Image.open(filename,"r"),int(pwlist[0],16),int(pwlist[1],16),int(pwlist[2],16),int(pwlist[3],16),int(pwlist[4],2))
    with open("output.txt","w",encoding = "UTF-8") as f:
    f.write(whole_text)
