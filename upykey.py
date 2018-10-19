"""
This file is a class for controlling matrix keyboards in Micropython

Copyright 2018 Bruno Martins

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

from machine import Pin
import time


class UpyKey():
    """ This class configures and reads a matrix keyboard """
    def __init__(self, cols_pins: list, rows_pins: list):
        """
        Construct a new UpyKey object
        :param cols_pins: A list with the pin numbers of the collum pins
        :param rows_pins: A list with the pin numbers of the row pins
        """
        self._cols_pins = []
        self._rows_pins = []
        self.set_cols_pins(cols_pins)
        self.set_rows_pins(rows_pins)
        self.keys = []

    def __init__(self, cols_pins: list, rows_pins: list, keys: list):
        """
        Construct a new UpyKey object
        :param cols_pins: A list with the pin numbers of the collum pins
        :param rows_pins: A list with the pin numbers of the row pins
        :param keys: A matrix (lis of lists) with a string
        corresponding to each key position
        """
        self._cols_pins = []
        self._rows_pins = []
        self.set_cols_pins(cols_pins)
        self.set_rows_pins(rows_pins)
        self._keys = keys

    def set_cols_pins(self, cols_pins):
        """
        Sets the columns pins
        :param cols_pins: A list with the pin numbers of the collum pins
        """
        for col_pin in cols_pins:
            pin = Pin(col_pin, Pin.OUT)
            pin.value(0)
            self._cols_pins.append(pin)

    def set_rows_pins(self, rows_pins):
        """
        Sets the rows pins
        :param rows_pins: A list with the pin numbers of the row pins
        """
        for row_pin in rows_pins:
            pin = Pin(row_pin, Pin.IN, pull=Pin.PULL_DOWN)
            self._rows_pins.append(pin)

    def set_keys(self, keys):
        """
        Sets the keys matrix
        :param keys: A matrix (lis of lists) with a string
        corresponding to each key position
        """
        self._keys = keys

    def read_key_press_positions(self):
        """
        Reads de keyboard and returns a list of the positions of the keys
        being pressed, indexed starting from 0
        [(col1, row1), (col2, row2) ...]
        example:
        if the key on the first line and first collumn is being pressed
        returns [(0, 0)]
        if the second and the third keys of the first collumn are being pressed
        returns [(0, 1), (0, 2)]
        if no key is being pressed:
        returns []

        :returns: A list of touples with the positions of the keys being
        pressed
        """
        response = []
        col_index = 0
        for col_pin in self._cols_pins:
            col_pin.value(1)
            row_index = 0
            for row_pin in self._rows_pins:
                if row_pin.value():
                    response.append((col_index, row_index))
                row_index += 1
            col_index += 1
            col_pin.value(0)
        return response

    def read_key_press_strings(self):
        """
        Sets the keys matrix
        :raises: KeyError if the key's position is not in the keys matrix
        """
        response = []
        positions = self.read_key_press_positions()
        try:
            for position in positions:
                response.append(self._keys[position[0]][position[1]])
        except:
            raise KeyError("Key position not present in keys matrix")
        return response
