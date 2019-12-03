from flask import render_template, send_file, request
from mbrot import app
from .mandelbrot import generate_mbrot

@app.route('/mandelbrot', methods=['GET'])
def render_mandelbrot_set():
    # try i.e. http://127.0.0.1:5000/mandelbrot?x=0.35&y=0.5&z=0.00005

    def clamp(x, low=-2, high=2):
        return min(high, max(x, low))

    x, y, step= float(request.args['X']), float(request.args['Y']), float(request.args['step'])

    # 512 px wide, 512 px high
    w, h = 512, 512

    # compute frame from center coordinate and step size. Clamp to -2, 2, -2, 2
    xa, xb, ya, yb = x - w/2 * step, x + w/2 * step, y - h/2 * step, y + h/2 * step
    xa, xb, ya, yb = tuple(map(clamp, [xa, xb, ya, yb]))

    img_io = generate_mbrot(xa, xb, ya, yb)
    return send_file(img_io, mimetype='image/png')


@app.route('/')
def index():
    return render_template('index.html')