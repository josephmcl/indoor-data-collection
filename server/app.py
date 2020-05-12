import matplotlib
matplotlib.use("Qt5Agg")

from flask import Flask, jsonify, make_response, request
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import io
import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Don\'t talk to me'

# Bad stuff
X = []
Y = []
L = []

@app.route('/api/add_message/', methods=['POST'])
def add_message():
    global X
    global Y
    global L
    content = request.json
    print(content)
    X.append(content['location'][0])
    Y.append(content['location'][1])
    if 'lux' in content['lux']:
        L.append(content['lux']['lux'])
    else:
        if (len(L) == 0):
            L.append(0)
        else:
            L.append(L[-1])
    data = {'message': 'Created', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 201)

@app.route('/plot')
def plot_data():
    global X
    global Y
    global L
    img = io.BytesIO()

    #plt.scatter(X, Y, c=lux, cmap='plasma')

    fig, ax = plt.subplots()
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.05)

    ax.axis('equal')
    ax.grid()

    if len(X) > 0:
        im = ax.scatter(X, Y, c=L, cmap='plasma')
    else:
        im = ax.scatter([0], [0], c=[0], cmap='plasma')

    fig.colorbar(im, cax=cax, orientation='vertical')
    cax.set_ylabel('lux')

    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()

    return '<img src="data:image/png;base64,{}">'.format(plot_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0')