import os
import binascii
import glob
import shutil
from PyQt5.QtCore import QThread, pyqtSignal
from fontTools.ttLib import TTFont
from PIL import ImageFont, ImageDraw, Image

all_range = (0x0000, 0xFFFF)

black_histogram = [256, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


class FontCreator(QThread):
    set_progress_text = pyqtSignal(str)
    set_progress = pyqtSignal(int, int)
    done = pyqtSignal()

    def __init__(self, font_path, margin_top, margin_left, delete_bmp, overwrite_bmp, parent=None):
        QThread.__init__(self, parent)
        self.font_path = font_path
        self.margin_top = int(margin_top)
        self.margin_left = int(margin_left)
        self.delete_bmp = delete_bmp
        self.overwrite_bmp = overwrite_bmp

        self.tt_font = TTFont(self.font_path)
        self.image_font = ImageFont.truetype(self.font_path, 15)
        self.root_path = os.path.dirname(os.path.abspath(__file__))

        self.bmp_dir = None
        self.ft_dir = None
        self.create_directory()

    def create_directory(self):
        self.bmp_dir = os.path.join(self.root_path, 'bmp')
        if not os.path.exists(self.bmp_dir):
            os.makedirs(self.bmp_dir)

        self.ft_dir = os.path.join(self.root_path, 'ft')
        if not os.path.exists(self.ft_dir):
            os.makedirs(self.ft_dir)

    def __del__(self):
        self.wait()

    def char_in_font(self, unicode_char, font):
        for cmap in font['cmap'].tables:
            if cmap.isUnicode():
                if ord(unicode_char) in cmap.cmap:
                    return True
        return False

    def create_bmp(self):
        for i in range(all_range[0], all_range[1]):
            self.set_progress.emit(i, all_range[1])

            result = self.char_in_font(chr(i), self.tt_font)
            if result is False:
                print('없음: {}'.format(i))
                continue

            image = Image.new('1', (16, 16), "black")
            draw = ImageDraw.Draw(image)
            draw.text((self.margin_left, self.margin_top), chr(i), font=self.image_font, fill="white")

            if i is not 32 and i is not 127 and image.histogram() == black_histogram:
                print("{:04x} is black".format(i))
                continue

            file_path = "bmp/{:04x}2.bmp".format(i)
            if self.overwrite_bmp:
                if os.path.isfile(file_path):
                    continue

            image.save(file_path, "bmp")

    def pack_bmp(self):
        base = os.path.basename(self.font_path)
        file, ext = os.path.splitext(base)
        ft_file_name = 'amazfit_bip_{}.ft'.format(file)
        ft_path = os.path.join(self.ft_dir, ft_file_name)
        self.pack_font(ft_path)

    # Create a Amazfit Bip file from bmps
    def pack_font(self, font_path):
        print('Packing', font_path)
        font_file = open(font_path, 'wb')
        header = bytearray(binascii.unhexlify('4E455A4B08FFFFFFFFFF01000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000'))
        bmps = bytearray()

        range_nr = 0
        seq_nr = 0
        startrange = -1

        bmp_files = sorted(glob.glob('bmp' + os.sep + '*'))
        bmp_len = len(bmp_files)

        for i in range(0, bmp_len):
            print('pack_font', i, bmp_len)
            self.set_progress.emit(i, bmp_len)

            margin_top = int(bmp_files[i][8])

            if (i == 0):
                unicode = int(bmp_files[i][4:-5], 16)
            else:
                unicode = next_unicode

            if (i + 1 < len(bmp_files)):
                next_unicode = int(bmp_files[i + 1][4:-5], 16)
            else:
                next_unicode = -1

            if (unicode != next_unicode):
                if (startrange == -1):
                    range_nr += 1
                    startrange = unicode

                img = Image.open(bmp_files[i])
                img_rgb = img.convert('RGB')
                pixels = img_rgb.load()

                x = 0
                y = 0
                char_width = 0

                while y < 16:
                    b = 0
                    for j in range(0, 8):
                        if pixels[x, y] != (0, 0, 0):
                            b = b | (1 << (7 - j))
                            if (x > char_width):
                                char_width = x
                        x += 1
                        if x == 16:
                            x = 0
                            y += 1
                    bmps.extend(b.to_bytes(1, 'big'))
                char_width = char_width * 16 + margin_top
                bmps.extend(char_width.to_bytes(1, 'big'))

                if unicode + 1 != next_unicode:
                    endrange = unicode
                    sb = startrange.to_bytes(2, byteorder='big')
                    header.append(sb[1])
                    header.append(sb[0])
                    eb = endrange.to_bytes(2, byteorder='big')
                    header.append(eb[1])
                    header.append(eb[0])
                    seq = seq_nr.to_bytes(2, byteorder='big')
                    header.append(seq[1])
                    header.append(seq[0])
                    seq_nr += endrange - startrange + 1
                    startrange = -1
            else:
                print('multiple files of {:04x}'.format(unicode))

        rnr = range_nr.to_bytes(2, byteorder='big')
        header[0x20] = rnr[1]
        header[0x21] = rnr[0]

        font_file.write(header)
        font_file.write(bmps)

    def run(self):
        self.set_progress_text.emit("1/2")
        self.create_bmp()
        self.set_progress_text.emit("2/2")
        self.pack_bmp()

        if self.delete_bmp:
            shutil.rmtree(self.bmp_dir)

        self.done.emit()
