#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from PIL import ImageFont, ImageDraw, Image

root_path = os.path.dirname(os.path.abspath(__file__))

marginLeft = 0
marginTop = -3
all_range = (0x0000, 0xFFFF)

black_histogram = [256, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

directory = os.path.join(root_path, 'bmp')
if not os.path.exists(directory):
    os.makedirs(directory)


def printInRange(charRange, font):
    for i in range(charRange[0], charRange[1]):
        image = Image.new('1', (16, 16), "black")
        draw = ImageDraw.Draw(image)
        draw.text((marginLeft, marginTop), chr(i), font=font, fill="white")
        # image.save("{}/{:04x}4.bmp".format(directory, i), "bmp")
        image.save("bmp/{:04x}4.bmp".format(i), "bmp")


def printAllRange(charRange, font, ttfont):
    for i in range(charRange[0], charRange[1]):

        result = char_in_font(chr(i), ttfont)
        if result is False:
            print('없음: {}'.format(i))
            continue

        image = Image.new('1', (16, 16), "black")
        draw = ImageDraw.Draw(image)
        draw.text((marginLeft, marginTop), chr(i), font=font, fill="white")
        # image.save("{}/{:04x}4.bmp".format(directory, i), "bmp")

        if i is not 32 and i is not 127 and image.histogram() == black_histogram:
            print("{:04x} is black".format(i))
            continue

        file_path = "bmp/{:04x}2.bmp".format(i)
        if os.path.isfile(file_path):
            continue

        image.save(file_path, "bmp")


def printOne(char_hex, font):
    image = Image.new('1', (16, 16), "black")
    draw = ImageDraw.Draw(image)
    draw.text((marginLeft, marginTop), chr(char_hex), font=font, fill="white")
    # image.save("{}/{:04x}4.bmp".format(directory, i), "bmp")
    image.save("bmp/{:04x}4.bmp".format(char_hex), "bmp")


#######################################################################################################
#######################################################################################################
#######################################################################################################


from fontTools.ttLib import TTFont


def char_in_font(unicode_char, font):
    for cmap in font['cmap'].tables:
        if cmap.isUnicode():
            if ord(unicode_char) in cmap.cmap:
                return True
    return False


def create_bmp_one(i, font):
    image = Image.new('1', (16, 16), "black")
    draw = ImageDraw.Draw(image)
    draw.text((marginLeft, marginTop), chr(i), font=font, fill="white")

    if i is not 32 and i is not 127 and image.histogram() == black_histogram:
        print("{:04x} is black".format(i))
        return

    file_path = "bmp/{:04x}2.bmp".format(i)
    if os.path.isfile(file_path):
        return

    image.save(file_path, "bmp")


def create_bmp_range(ttf_path, directory_path):
    ttfont = TTFont(ttf_path)
    font = ImageFont.truetype(ttf_path, 15)

    print('return before run')
    # for i in range(all_range[0], all_range[1]):
    #     result = char_in_font(chr(i), ttfont)
    #     if result is False:
    #         print('없음: {}'.format(i))
    #         continue
    #     create_bmp_one(i, font)

    #TODO: 생성이 끝나면, 폰트로 패킹한다.
    # pack(directory_path)


def runtest():
    print('run in ttf2bmp file')

if __name__ == '__main__':
    print("글꼴 불러오는 중...")
    # fontPath = 'nns.ttf'
    fontPath = 'malgunsl.ttf'
    # ttfont = TTFont(fontPath)  # specify the path to the font in question
    #
    # font = ImageFont.truetype(fontPath, 15)
    # printAllRange(all_range, font, ttfont)
