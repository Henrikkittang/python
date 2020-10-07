from PIL import Image


def compareTuple(tup1, tup2):
    if tup1 == tup2:
        return True
    for b1 in tup1:
        for b2 in tup2:
            if abs(b1-b2) < 1:
                return True

    return False

def compressImage(filename):
    img = Image.open(filename)
    pixels = img.getdata()

    pixelCollection = []
    curPixc = [1, pixels[0]]
    for idx in range(1, len(pixels)):
        if compareTuple(pixels[idx], pixels[idx+1]):
            curPixc[0] += 1
        else:
            pixelCollection.append(curPixc)
            curPixc = [1, pixels[idx]]
    
    return pixelCollection

def decompressImageData(data):
    pixels = []
    for collection in data:
        for _ in range(collection[0]):
            pixels.append(collection[1])
    return pixels

def saveCompresedData(data, filename):
    string = str(data)
    string.replace(' ', '')
    with open(filename, 'w') as f:
        f.write(string)
        f.close()

data = compressImage('img1.jpg')
newImage = Image.open('img1.jpg')
data = decompressImageData(data)


image_out = Image.new(newImage.mode,newImage.size)
image_out.putdata(data)
image_out.save('img2.jpg')



        