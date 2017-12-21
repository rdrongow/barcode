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


def create_eans(nr_eans):
    eans = []
    for nr, ean in nr_eans:
        ean = barcode.get('ean13', ean)
        eans.append((nr, ean))
    return eans


def _csv_to_tuple(file_path):
    nr_eans = []
    with open(file_path) as f:
        for line in f:
            if line == ';':
                continue
            nr_eans.append(line.strip('\n').split(";"))
    return nr_eans


if __name__ == '__main__':
    file_path = raw_input("Enter path of file [eans.csv]: ") or "eans.csv"
    output_to = raw_input("Enter name of output folder [eans]: ") or "eans"
    nr_eans = _csv_to_tuple(file_path)
    eans = create_eans(nr_eans)
    if not os.path.exists(output_to):
        os.makedirs(output_to)
    for nr, ean in eans:
        ean.save('{}/{}'.format(output_to, nr), options)
