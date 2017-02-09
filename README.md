# Purpose

Create a series of EAN SVGs from a CSV of the structure
`art_nr;ean`, where `art_nr` can be any number and `ean`
must be a number of 13 digits. The SVGs will be stored
to a folder, the name of the SVG file is `art_nr`.

# Installation

After cloning the repository, you need to initialize a
virtualenv (e.g, `virtualenv .`). Afterwards you need
to install the neccessary packages via
`bin/pip install -r requirements.txt`. There is also an
init script which you can execute with `./initialize.sh`.

# Usage

Type `bin/python create_barcode.py`. You will be asked
for a CSV file and an output folder. Afterwards the EANs
will be written to the given folder.

