from PIL import Image
import concurrent.futures


class ImageWrapper(object):

    @staticmethod
    def loadImage(path: str) -> Image:
        return Image.open(path)

    @staticmethod
    def saveListToFolder(path: str, images: list) -> None:
        [x.save(path+str(idx)+'.png') for idx, x in enumerate(images)]

    def _crop(self, image: Image, width: int, height: int, space: int) -> list:
        croppedImages = []
        imgWidth, imageHeight = image.size
        for row in range(0, imageHeight, height+space):
            for column in range(0, imgWidth, width+space):
                crop = image.crop((column, row, column + width, row + height))
                croppedImages.append(crop)
               
        return croppedImages

    def _makeTransparant(self, image: Image, colorToChange: tuple) -> Image:
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

    def _resize(self, image: Image, width: int, height: int) -> Image:
        return image.resize((width, height))

class SpriteHandler(ImageWrapper):
    
   
    @classmethod
    def crop(cls, baseImage: Image, width: int, height: int, space: int) -> list:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            f = executor.submit(cls._crop, cls, baseImage, width, height, space)
            return f.result()
            

    @classmethod
    def makeTransparant(cls, images: list, colorToChange: tuple) -> list:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(cls._makeTransparant, cls, image, colorToChange) for image in images]
            return [f.result() for f in concurrent.futures.as_completed(results)]
            
    
    @classmethod
    def resize(cls, images: list, width: int, height: int) -> list:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(cls._resize, cls, image, width, height) for image in images]            
            return [f.result() for f in concurrent.futures.as_completed(results)]
 


baseImage   = SpriteHandler.loadImage('util/spritesheet.png')
transparent = SpriteHandler.makeTransparant(baseImage, (0, 0, 0))
croped      = SpriteHandler.crop(transparent[0], 14, 14, 2)
rezied      = SpriteHandler.resize(croped[0], 25, 25)

for x in transparent:
    print(x, type(x))

SpriteHandler.saveListToFolder(croped, 'util/imgs/')

# for f in croped:
#     print(f)


# SpriteHandler.saveListToFolder(rezied, 'util/imgs/')


