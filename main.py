from PIL import Image, ImageChops
from bitmap import CreateBitMap, CompareBitMap
import time

create = CreateBitMap(32, -2, -6)

wish_height = 20;
scale_height = wish_height * 32;
wish_width = wish_height;
scale_width = wish_width * 32;

compare = CompareBitMap()
start_time = time.time()
with Image.open("debian.png") as image:
    image = image.convert("RGB")
    image = image.convert("L")
    image = image.point(lambda x: 0 if x == 0 else 1, mode='1')
    
    image = image.resize((scale_width, scale_height))
    for y in range(wish_height):
        line = "\x1b[38;2;255;0;95;48;2;0;0;0m"
        for x in range(wish_height * 2):
            line += compare.getSymbol(image.crop((x * 16, y * 32, x * 16 + 16, y * 32 + 32)))
        line += "\x1b[0m"
        print(line)
print(f"Time: {time.time() - start_time:.2f}s")

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
"""