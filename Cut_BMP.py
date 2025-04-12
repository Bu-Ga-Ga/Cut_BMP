from PIL import Image
N = int(input("Введите количество полосок: "))
filename = input("Введите название BMP-файла: ")
direction = input("Введите направление нарезки (h - горизонтально, v - вертикально): ")
img = Image.open(filename)
img_width, img_height = img.size
if direction == "h":
    strip_height = img_height // N
    strip_width = img_width
else:
    strip_width = img_width // N
    strip_height = img_height
for i in range(N):
    if direction == "h":
        top = i * strip_height
        bottom = (i + 1) * strip_height
        left = 0
        right = img_width
    else:
        left = i * strip_width
        right = (i + 1) * strip_width
        top = 0
        bottom = img_height
    strip = img.crop((left, top, right, bottom))
    filename = f"{i+1}.bmp"
    strip.save(filename)

