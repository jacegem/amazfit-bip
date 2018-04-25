#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Amazfit Bip(米动手表 青春版) 한글 글자 비트맵 이미지 생성기
Amazfit Bip(米动手表 青春版) Korean Hangul glyph bitmap image generator
Copyright (c) 2018 Youngbin Han <sukso96100@gmail.com>
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os

from PIL import ImageFont, ImageDraw, Image

root_path = os.path.dirname(os.path.abspath(__file__))

english_range = (0x0001, 0x01ff)
symbol_range = (0x2460, 0x266D)

hangul_jamo_range = (0x1100, 0x11ff)
hangul_char_range = (0xAC00, 0xD7AF)


def let_user_pick(options):
    print("Please choose:")
    for idx, element in enumerate(options):
        print("{}) {}".format(idx + 1, element))
    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            return int(i)
    except:
        pass
    return None


# input_list = [
#     '1111', '2222', '3333'
# ]
# P1 = let_user_pick(input_list)

print("""Amazfit Bip(米动手表 青春版) 한글 비트맵 이미지 생성기\n
      ©2018 Youngbin Han(sukso96100@gmail.com)\n
      이 스크립트는 한글 자모(U+1100~U+11FF) 와 한글 글자마디(U+AC00~U+D7AF) 에 헤당하는 파일만 생성합니다.""")
# fontPath = input("사용할 글꼴 파일(*.ttf/*.otf) 경로 또는 이름 입력:")
# destPath = input("생성된 비트맵 이미지를 저장할 경로 입력:") or 'bmp'
# marginLeft = int(input("글자 왼쪽 간격 정수로 입력.(기본값:0)") or "0")
# marginTop = int(input("글자 위쪽 간격 정수로 입력.(기본값:0)") or "0")

marginLeft = 0
marginTop = -3

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


# print("글꼴 불러오는 중...")b
# font = ImageFont.truetype(fontPath, 15)
#
# print("처리중...")
# printInRange(english_range, font)
# printInRange(hangul_jamo_range, font)
# printInRange(hangul_char_range, font)
#
# print("작업 완료.")


def printOne(char_hex, font):
    image = Image.new('1', (16, 16), "black")
    draw = ImageDraw.Draw(image)
    draw.text((marginLeft, marginTop), chr(char_hex), font=font, fill="white")
    # image.save("{}/{:04x}4.bmp".format(directory, i), "bmp")
    image.save("bmp/{:04x}4.bmp".format(char_hex), "bmp")


all_range = (0x0000, 0xFFFF)

from fontTools.ttLib import TTFont


def char_in_font(unicode_char, font):
    for cmap in font['cmap'].tables:
        if cmap.isUnicode():
            if ord(unicode_char) in cmap.cmap:
                return True
    return False


black_histogram = [256, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


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


if __name__ == '__main__':
    print("글꼴 불러오는 중...")
    # fontPath = 'nns.ttf'
    fontPath = 'malgunsl.ttf'
    ttfont = TTFont(fontPath)  # specify the path to the font in question

    font = ImageFont.truetype(fontPath, 15)
    printAllRange(all_range, font, ttfont)


    #
    # print("처리중...")
    # printInRange(english_range, font)
    # print("영어 완료...")
    # printInRange(hangul_jamo_range, font)
    # print("자음모음 완료...")
    # printInRange(symbol_range, font)
    # print("기호 완료...")
    # printInRange(hangul_char_range, font)
    # print("작업 완료.")

    # fontPath = 'GL.ttf'
    # printOne(0xc388, font)

    # from itertools import chain
    # import sys
    # from fontTools.ttLib import TTFont
    # from fontTools.unicode import Unicode
    #
    # ttf = TTFont(fontPath, 0, allowVID=0,
    #              ignoreDecompileErrors=True,
    #              fontNumber=-1)
    #
    # chars = chain.from_iterable([y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables)
    # print(list(chars))
    # for ch in chars:
    #     print(ch)
    # print('end')
