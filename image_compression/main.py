from PIL import Image
import pickle


class PixelCount(object):
    def __init__(self, count, pixel):
        self.count = count
        self.pixel = pixel

    def __repr__(self):
        return '{}{}'.format(self.count, self.pixel)


class ImageCompression(object):
    def __init__(self, filename):
        self.filename = filename
        self.width = Image.open(self.filename).width
        self.height = Image.open(self.filename).height

        self.compressedData = []


    def compressImage(self):
        self.compressedData.clear()
        pixels = Image.open(self.filename).getdata()

        pixelCount = PixelCount(0, pixels[0])
        for pixel in pixels:
            if pixelCount.pixel != pixel or pixelCount.count >= 254:
                self.compressedData.append(pixelCount)
                pixelCount = PixelCount(1, pixel)
            else:
                pixelCount.count += 1
        self.compressedData.append(pixelCount)       
        

    def saveData(self):
        data = bytearray(len(self.compressedData) * 4)

        for idx, pixelCount in enumerate(self.compressedData):
            dataIdx = idx*4
            data[dataIdx] = pixelCount.count
            data[dataIdx+1] = pixelCount.pixel[0]
            data[dataIdx+2] = pixelCount.pixel[1]
            data[dataIdx+3] = pixelCount.pixel[2]

        filename = self.filename.split('.')[0]
        with open(filename+'.txt', 'wb') as f:
            f.write(data)
            f.close()

    def restoreImage(self):
        data = []
        filename = self.filename.split('.')[0]
        with open(filename+'.txt', 'rb') as f:
            data = list(f.read())

        decompresdData = []
        for idx in range(0, len(data), 4):
            for _ in range(data[idx]):
                decompresdData.append(data[idx+1])
                decompresdData.append(data[idx+2])
                decompresdData.append(data[idx+3])
        
        newFilename = 'decompressed.' + self.filename.split('.')[1]
        Image.frombytes('RGB', (self.width, self.height), bytes(decompresdData)).save(newFilename)


ic = ImageCompression('testing.tiff')
ic.compressImage()
ic.saveData()
ic.restoreImage()

quit()




   