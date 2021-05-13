from PIL import Image
import pygame

class SpriteHandler(object):
    def __init__(self, path):
        self._spriteSheet: Image = Image.open(path)
        self._images     : list = []

    def crop(self, width: int, height: int, space: int) -> None:
        imgWidth, imgHeight = self._spriteSheet.size
        for row in range(0, imgHeight, height+space):
            for column in range(0, imgWidth, width+space):
                crop = self._spriteSheet.crop((column, row, column + width, row + height))
                self._images.append(crop)

    def makeTransparent(self, colorToChange: tuple) -> None:
        for idx, img in enumerate(self._images):
            self._images[idx] = self._makeTransparant(img, colorToChange)
               
    def resize(self, width: int, height: int) -> None:
        for idx, img in enumerate(self._images):
            self._images[idx] = self._resize(img, width, height)

    def getSprites(self, width: int, height: int) -> list:
        return [pygame.image.fromstring(image.tobytes(), (width, height), 'RGBA') for image in self._images]

    def _makeTransparant(self, image: Image, colorToChange: tuple) -> Image:
        newImage = image.convert('RGBA')
        datas = newImage.getdata()

        newData = [None] * len(datas)
        for idx, item in enumerate(datas):
            # newData[idx] = (255, 255, 255, 0) if *item == *colorToChange else item
            # if *item == *colorToChange:
            if item[0] == colorToChange[0] and item[1] == colorToChange[1] and item[2] == colorToChange[2]:
                newData[idx] = (255, 255, 255, 0) 
            else:
                newData[idx] = item

        newImage.putdata(newData)
        return newImage

    def _resize(self, image: Image, width: int, height: int) -> Image:
        return image.resize((width, height))   



