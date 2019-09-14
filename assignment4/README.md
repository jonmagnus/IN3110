# Assignment 4

### `blur_1.py`
To run `blur_1.py` type `python3 blur_1.py` with the image file `beatles.jpg` in your working directory.
```
$ python3 blur_1.py
```

### `blur_2.py`
To run `blur_2.py` type `python3 blur_2.py` with the image file `beatles.jpg` in your working directory.
```
$ python3 blur_2.py
```

### `blur_3.py`
To run `blur_3.py` type `python3 blur_3.py` with the image file `beatles.jpg` in your working directory.
```
$ python3 blur_3.py
```

### `blur.py`
```
$ python3 blur.py --help
usage: blur.py [-h] [-o FILENAME] [-m METHOD] image

Blur an image using the mean value of a 3*3 kernel

positional arguments:
  image                 an image to blur

optional arguments:
  -h, --help            show this help message and exit
  -o FILENAME, --outfile FILENAME
  -m METHOD, --method METHOD
                        the method used to produce the blurred image. Default
                        is set to 'numpy'.
```

To produce a blurred image using the numpy method you can type:

```
$ python3 blur.py beatles.jpg -o numpy.jpg --method numpy
```

If the method you specify does not exist the program will exit with something like the following.

```
$ python3 blur.py beatles.jpg -o numpy.jpg --method nonexistent_method
Traceback (most recent call last):
  File "blur.py", line 40, in <module>
    raise ValueError(f'Method \'{method}\' not found.')
ValueError: Method 'nonexistent_method' not found.
```

### Packaging and unit tests
Just use `pytest` in the root of `assignment4` to run the two unit tests.
```
$ pytest
============================= test session starts ==============================
platform linux -- Python 3.6.8, pytest-5.1.2, py-1.8.0, pluggy-0.13.0
rootdir: /home/jon-magnus/Documents/IN3110-jonmagnr/assignment4
collected 2 items

test_blur.py ..                                                          [100%]

============================== 2 passed in 8.21s ===============================
```

### Blurring faces
```
$ python3 blur_faces.py
```
![](.blur_faces_output.png)
