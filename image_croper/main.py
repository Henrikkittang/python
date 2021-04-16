from PIL import Image
import os


def crop(filepath, width, height, space):
    img = Image.open(filepath)
    img_widht, img_height = img.size
    frame_num = 0
    for row in range(0, img_height, height+space):
        for column in range(0, img_widht, width+space):
            try:
                crop = img.crop((column, row, column + width, row + height))
                save_to = os.path.join('imgs', "testing_{:02}.png")
                crop.save(save_to.format(frame_num))
                frame_num += 1
            except:
                print('exeption')
                pass


def makeTransparant(filepath, colorToChange):
    
    img = Image.open(filepath)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == colorToChange[0] and item[1] == colorToChange[1] and item[2] == colorToChange[2]:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(filepath)

def convertJpgToPng(filepath):
    image = Image.open(filepath)
    image.save(filepath[:-4]+'.png')


def resize(filepath, width, height):
    image = Image.open(filepath)
    new_image = image.resize((width, height))
    new_image.save(filepath)


f = []
for (dirpath, dirnames, filenames) in os.walk('imgs'):
    f.extend(filenames)
    break


makeTransparant('temp/0.png', (0, 0, 0))
# resize('frightend1.png', 22, 22)





