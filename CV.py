from PIL import Image
from sys import argv
import os


def md():
    print('*'*50)
    print(' Welcome use my program.')
    print(' This progarm is like opencv.')
    print(' Parameter explain :')
    print('  -p/-P is source file path.')
    print('  -l/-L is grey level [0-255].')
    print('  -o/-O is out file path.')
    print(' Example : xxx.exe -p /xx/xx/xx.jpg -l 150 -o /xx/xx/xx.jpg.')
    print('*'*50)


def cmd():
    if argv != '':
        parm_1 = argv[1]
        if parm_1 == '-p'or parm_1 == '-P':
            parm_2 = argv[2]
            parm_3 = argv[3]
            parm_4 = argv[4]
            parm_5 = argv[5]
            parm_6 = argv[6]
            if parm_2 != '' and parm_3 == '-L' or parm_3 == '-l' and parm_4 != '' and parm_5 == '-o' or parm_5 == '-O' and parm_6 != '':
                CV_PIC(parm_2, parm_4, parm_6)
        elif parm_1 == '-h' or parm_1 == '--help' or parm_1 == '-H':
            md()
        else:
            print('Parameter error')
            print('please try input xxx.exe -h')


def CV_PIC(Path, ColorLevel, Out):
    img = Image.open(Path)
    Img = img.convert('L')
    threshold = int(ColorLevel)
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    photo = Img.point(table, '1')
    photo.save(Out)


if __name__ == "__main__":
    cmd()
