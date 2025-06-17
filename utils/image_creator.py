import os
from PIL import Image, ImageDraw, ImageFont

# Load images
img = Image.open("skidpad_mac_Mesa_de_trabajo_1.png").convert("RGBA")
ev = Image.open("ev.png").convert("RGBA")
cv = Image.open("cv.png").convert("RGBA")

with open('../teams.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

teams = []
for line in lines:
    img = Image.open("skidpad_mac_Mesa_de_trabajo_1.png").convert("RGBA")
    team = line.strip().split(',')
    number = team[0]
    university = team[2]
    category = 'ev' if 'electric' in team[3].lower() else 'cv'

    if os.path.exists(f"{number}.png"):
        img2 = Image.open(f"{number}.png").convert("RGBA")
        img.paste(img2, (118, 30), img2)

    if category == 'cv':
        img.paste(ev, (0, 0), ev)
    else:
        img.paste(cv, (0, 0), cv)

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("Montserrat-SemiBoldItalic.ttf", size=29)
    x_min, x_max = 58, 117
    y_min, y_max = 29, 88

    text_width, text_height = draw.textsize(str(number), font=font, )

    x = x_min + (x_max - x_min - text_width) // 2
    y = y_min + (y_max - y_min - text_height) // 2

    draw.text((x, y), str(number), font=font, fill="#232323")

    font = ImageFont.truetype("MYRIADPRO-REGULAR.OTF", size=19)
    x_min, x_max = 117, 519
    y_min, y_max = 0, 30

    text_width, text_height = draw.textsize(university, font=font)

    x = x_min + (x_max - x_min - text_width) // 2
    y = y_min + (y_max - y_min - text_height) // 2

    draw.text((x, y), university, font=font, fill="white")

    img.save(f"exports/{number}.png", "PNG")
