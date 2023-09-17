from PIL import Image, ImageChops
from bitmap import CreateBitMap, CompareBitMap
import random
import time

create = CreateBitMap(32, -2, -6)

wish_height = 50;
scale_height = wish_height * 32;
wish_width = wish_height;
scale_width = wish_width * 32;

random.seed()
"""
lines1 = list()
lines2 = list()

compare = CompareBitMap()
start_time = time.time()
with Image.open("arch.png") as image:
    image = image.convert("RGB")
    image = image.convert("L")
    image = ImageChops.invert(image)
    image.save("test.bmp")
    image = image.point(lambda x: 0 if x == 0 else 1, mode='1')
    
    image = image.resize((scale_width, scale_height))
    for y in range(wish_height):
        line = "\x1b[38;2;255;0;95;48;2;0;0;0m"
        for x in range(wish_height * 2):
            line += compare.getSymbol(image.crop((x * 16, y * 32, x * 16 + 16, y * 32 + 32)))
        line += "\x1b[0m"
        print(line)
        lines1.append(line)
print(f"Time: {time.time() - start_time:.2f}s")

start_time = time.time()
with Image.open("debian.png") as image:
    image = image.convert("RGB")
    image = image.convert("L")
    image = image.point(lambda x: 0 if x == 0 else 1, mode='1')
    image.save("test.bmp")
    image = image.resize((scale_width, scale_height))
    for y in range(wish_height):
        line = "\x1b[38;2;0;255;255;48;2;0;0;0m"
        for x in range(wish_height * 2):
            line += compare.getSymbol(image.crop((x * 16, y * 32, x * 16 + 16, y * 32 + 32)))
        line += "\x1b[0m"
        print(line)
        lines2.append(line)
print(f"Time: {time.time() - start_time:.2f}s")

if(lines1 == lines2):
    print("\x1b[38;2;0;255;0msame\x1b[0m")
else:
    print("\x1b[38;2;255;0;0mnot same\x1b[0m")

for i in range(len(lines1)):
    if(lines1[i] == lines2[i]):
        print(lines1[i], end="")
        print(lines2[i])
    else:
        lines1[i] = lines1[i].replace("\x1b[38;2;0;255;255;48;2;0;0;0m", "\x1b[38;2;255;0;0;48;2;0;0;0m")
        print(lines1[i], end="")
        lines2[i] = lines2[i].replace("\x1b[38;2;0;255;255;48;2;0;0;0m", "\x1b[38;2;255;0;0;48;2;0;0;0m")
        print(lines2[i])
"""

frames = list()
lines = list()

start_time = time.time()
compare = CompareBitMap()
with Image.open("debian.png") as image:
    image = image.convert("RGB")
    image = image.convert("L")
    image = image.point(lambda x: 0 if x == 0 else 1, mode='1')
    image.save("test.bmp")
    image = image.resize((scale_width, scale_height))
    for i in range(int(360 / 10)):
        for y in range(wish_height):
            lines.append("\x1b[38;2;255;0;95;48;2;0;0;0m")
            for x in range(wish_height * 2):
                lines[y] += compare.getSymbol(image.crop((x * 16, y * 32, x * 16 + 16, y * 32 + 32)))
            lines[y] += "\x1b[0m"
        frames.append(lines)
        for line in lines:
            print(line)
        lines = list()
        image = image.rotate(10)
    while True:
        for frame in frames:
            print("\n" * 60)
            for line in frame:
                print(line)
            time.sleep(0.016)
print(f"Time: {time.time() - start_time:.2f}s")
