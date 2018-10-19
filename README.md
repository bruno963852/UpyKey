# UpyKey
Lib for reading matrix keyboars in Micropython.

Developed and tested using de LoBo Micropython for ESP32, but it should work in the standard version both in ESP32 and ESP8266

# Usage
You can just import and instantiate the class with a list of pins for the columns and rows
```python
from upykey import UpyKey
keyboard = UpyKey([16, 17, 18], [12, 13, 14, 15])
```
You can use the `read_key_press_positions()` function to return the positions of the keys that are being pressed
```python
key_positions = keyboard.read_key_press_positions()
```
It returns a list of touples with the positions of the keys that are currently being pressed, indexed from 0.
For instance, if the key in the first column, second row is being pressed it returns:
```python
[(0, 1)]
```
if both the previous key and the key in the second column, third row are being pressed at the same time it should return
```python
[(0, 1), (1, 2)]
```
And so on...
If no key is being pressed it returns an empty list `[]`

This function reads the keyboard only once, sou you should call it in a lopp and process the results.

## Setting key Strings
There is a constructor if you want to set the string correspondent to each key.
The strings must be in a matrix with each string being in the same position that the key, for example.
```python
columns = [16, 17, 18]
rows = [12, 13, 14, 15]
keys = [['1', '4', '7', '*'], ['2', '5', '8', '0'], ['3', '6', '9', '#']]
keyboard = UpyKey(columns, rows, keys)
```
Alternatively you can use the `set_keys(keys)` method to change the string matrix anytime

You can use the `get_key_pres_strings()` mehod to return the strings of the keys being pressed instead of the positions

```python
key_positions = keyboard.read_key_press_strings()
```
For instance, the same previous exampĺes, with the keys matrix set it returns:
```python
['4']
```
```python
['4', '8']
```
And so on...
If no key is being pressed it returns an empty list `[]`
