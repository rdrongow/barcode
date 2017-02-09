import barcode
from barcode.writer import SVGWriter
import os

options = {
    "module_width": 0.3,
    "module_height": 6,
    "quiet_zone": 0,
    "font_size": 7,
    "text_distance": 2,
    "background": "white",
    "foreground": "black",
    "center_text": "true"
    }


def svg_init(self, code):
    width, height = self.calculate_size(len(code[0]), len(code), self.dpi)
    self._document = barcode.writer.create_svg_object()
    self._root = self._document.documentElement


SVGWriter._init = svg_init


def main():
    file_path = raw_input("Enter path of file [eans.csv]: ") or "eans.csv"
    output_to = raw_input("Enter name of output folder [eans]: ") or "eans"
    if not os.path.exists(output_to):
            os.makedirs(output_to)
    with open(file_path) as f:
        for line in f:
            artnr, ean = line.strip('\n').split(";")
            print 'Create ean for {}'.format(artnr)
            ean = barcode.get('ean13', ean)
            ean.save('{}/{}'.format(output_to, artnr), options)


if __name__ == '__main__':
    main()
