from PIL import Image


class ImageCroper(object):
    
    @staticmethod
    def loadImage(path: str) -> Image:
        print(path)
        return Image.open(path)

    @staticmethod
    def crop(image: Image, width: int, height: int, space: int) -> list:
        croppedImages = []
        imgWidth, imageHeight = image.size
        for row in range(0, imageHeight, height+space):
            for column in range(0, imgWidth, width+space):
                crop = image.crop((column, row, column + width, row + height))
                croppedImages.append(crop)
               
        return croppedImages

    @staticmethod
    def makeTransparant(image: Image, colorToChange: tuple) -> Image:
        newImage = image.convert('RGBA')
        datas = newImage.getdata()

        newData = []
        for item in datas:
            if item[0] == colorToChange[0] and item[1] == colorToChange[1] and item[2] == colorToChange[2]:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        newImage.putdata(newData)
        return newImage

    @staticmethod
    def resize(image: Image, width: int, height: int) -> Image:
        return image.resize((width, height))

    @staticmethod   
    def saveListToFolder(path: str, images: list) -> None:
        [x.save(path+str(idx)+'.png') for idx, x in enumerate(images)]

class SpriteSheet(object):
    def __init__(self, path):
        self.path = path

    def loadGhosts(self):
        baseImage = ImageCroper.loadImage(self.path)
        transparent = ImageCroper.makeTransparant(baseImage, (0, 0, 0))
        croped = ImageCroper.crop(transparent, 14, 14, 2)
        rezied = [ImageCroper.resize(x, 22, 22) for x in croped]
        
        ImageCroper.saveListToFolder('temp/', rezied)

if __name__ == '__main__':
    sp = SpriteSheet('spritesheet.png')
    sp.loadGhosts()

    print('This is main')


