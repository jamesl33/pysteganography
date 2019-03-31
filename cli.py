#!/usr/bin/python3

"""This file is a part of "pysteganography" a Python steganography tool.

Copyright (C) 2019 James Lee <jamesl33info@gmail.com>.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>."""

import argparse

from pysteganography import Steganography


def command_line():
    """ Parse command line arguments and allow easy use of pysteganography """
    parser = argparse.ArgumentParser(description='Simple Python script to use "Last Bit Steganography" to hide messages in images')
    parser.add_argument('-i', '--input-file', action='store', type=str, help='Path to "PNG"/"BMP" which your file will be hidden in or is hidden in *THIS OPTION IS MANDITORY*')
    parser.add_argument('-e', '--encode-file', action='store', type=str, help='Path to the file you want to hide')
    parser.add_argument('-d', '--decode-file', action='store_true', help='Decodes "--input-file"')
    arguments = parser.parse_args()

    if not arguments.input_file:
        raise ValueError('Missing argument "-i/--input-file"')

    if arguments.encode_file and arguments.decode_file:
        raise ValueError('You cannot encode/decode at the same time')

    if arguments.encode_file:
        steg = Steganography(arguments.input_file)
        steg.encode_file(arguments.encode_file)

    if arguments.decode_file:
        steg = Steganography(arguments.input_file)
        steg.decode_file()


if __name__ == '__main__':
    command_line()
