from PIL import Image
from io import BytesIO
import math
import numpy as np


# NOTE: You do not have to touch this code, however if you want feel free to play around with it.

table = [(66, 30, 15),
         (25, 7, 26),
         (9, 1, 47),
         (4, 4, 73),
         (0, 7, 100),
         (12, 44, 138),
         (24, 82, 177),
         (57, 125, 209),
         (134, 181, 229),
         (211, 236, 248),
         (241, 233, 191),
         (248, 201, 95),
         (255, 170, 0),
         (204, 128, 0),
         (153, 87, 0),
         (106, 52, 3)]
table = np.array(table)


def color(n, maxIt):
    if n > 0:
        # interpolate
        nhigh = math.ceil(n)
        nlow = math.floor(n)

        return table[nlow % 16, :] * (n - nlow) + table[nhigh % 16, :] * (nhigh - n)
    else:
        return np.array([0, 0, 0])


def mandelbrot(c, maxIt):
    z = c
    for i in range(maxIt + 1):
        if abs(z) > 2.0:
            break
        z = z * z + c

    smooth = i + 1 - math.log(math.log2(abs(z))) if i < maxIt else maxIt
    return color(smooth, maxIt)

def generate_mbrot(xa, xb, ya, yb, w=512, h=512):
    # drawing area
    maxIt = 256  # max iterations allowed
    # image size
    imgx = w
    imgy = h
    image = Image.new("RGB", (imgx, imgy))

    dy = 1. / (imgy - 1)
    dx = 1. / (imgx - 1)
    d2x = .5 * dx
    d2y = .5 * dy
    for y in range(imgy):
        zy = y * (yb - ya) * dy + ya
        for x in range(imgx):
            zx = x * (xb - xa) * dx + xa

            # use this code for faster mandelbrot generation
            z = zx + zy * 1j
            col = mandelbrot(z, maxIt)
            col = (int(col[0]), int(col[1]), int(col[2]))

            # # 2x2 antialiasing
            # z = zx + zy * 1j
            # z1 = z + (d2x + d2y * 1j)
            # z2 = z + (d2x - d2y * 1j)
            # z3 = z + (- d2x + d2y * 1j)
            # z4 = z + (- d2x - d2y * 1j)
            # col = .25 * (np.array(mandelbrot(z1, maxIt)) +
            #              np.array(mandelbrot(z2, maxIt)) +
            #              np.array(mandelbrot(z3, maxIt)) +
            #              np.array(mandelbrot(z4, maxIt)))

            col = (int(col[0]), int(col[1]), int(col[2]))
            image.putpixel((x, y), tuple(col))

    img_io = BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io
