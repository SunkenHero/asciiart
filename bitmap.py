from PIL import Image, ImageDraw, ImageFont
import random

class CompareBitMap:

    def __init__(self):
        self.chars = list()
        for i in range(95):
            with Image.open("bitmap/" + str(i + 32) + ".bmp", "r") as char:
                char = char.point(lambda x: 0 if x == 0 else 1, mode='1')
                self.width, self.height = char.size
                char = list(char.getdata())
                char = [char[i:i + self.width] for i in range(0, len(char), self.width)]
                self.chars.append(char)

    def getSymbol(self, image):

        if(image.mode != '1'):
            if(image.mode != 'L'):
                image = image.convert('L')
            if(image.mode == 'L'):
                image = image.point(lambda x: 0 if x == 0 else 1, mode='1')
        
        image = list(image.getdata())
        image = [image[i:i + self.width] for i in range(0, len(image), self.width)]

        bestMatch = 0
        bestChar = " "
        maxMatch = self.height * self.width
        matchLimit = int(maxMatch * 0.02)

        for i in range(95):
            char = self.chars[i]
            matches = 0
            for x in range(self.width):
                for y in range(self.height):
                    if(char[y][x] == image[y][x]):
                        matches += 1
            if(i == 0 and matches == 0):
                return "M"
            if(matches > bestMatch):
                bestChar = chr(i + 32)
                if(matches >= maxMatch - matchLimit):
                    return bestChar
                if(bestChar == "M"):
                    return bestChar
                bestMatch = matches
        return bestChar

class CreateBitMap:
    
    def __init__(self, h, x_offset, y_offset):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.h = h
        self.w = int(self.h / 2)
        self.fontsize =  self.h
        self.w_com = len(range(32, 127))
        self.font  = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf", self.fontsize)
    
    def createBitmap(self):
        imageRGB = Image.new('RGB', (self.w * self.w_com, self.h))
        draw = ImageDraw.Draw(imageRGB)
        for i in range(0, 95):
            char = chr(i + 32)
            draw.text((self.x_offset + i * self.w, self.y_offset), char, font=self.font)

        image8bit = imageRGB.convert("L")

        image = image8bit.point(lambda x: 0 if x < 100 else 1, mode='1')
        image.save("bitmaps.bmp")
        return image

    def createBitmapSingle(self):
        for i in range(0, 95):
            imageRGB = Image.new('RGB', (self.w, self.h))
            draw = ImageDraw.Draw(imageRGB)
            char = chr(i + 32)
            draw.text((self.x_offset, self.y_offset), char, font=self.font)
            image8bit = imageRGB.convert("L")
            image = image8bit.point(lambda x: 0 if x < 100 else 1, mode='1')
            image.save("bitmap/" + str(i + 32) + ".bmp")

    def createRandomBitmap(self):
        random.seed()
        image = Image.new("1", (self.w, self.h))
        for y in range(image.height):
            for x in range(image.width):
                image.putpixel((x, y), random.randint(-15, 1))
        image.save("random.bmp")
        return image
    
    def noisedBitmap(self, image):
        random.seed()
        for y in range(image.height):
            for x in range(image.width):
                if(random.randint(-4, 1) > 0):
                    image.putpixel((x, y), 1)
        image.save("noised.bmp")
        return image

    def getHeight(self):
        return self.h
    
    def getWidth(self):
        return self.w