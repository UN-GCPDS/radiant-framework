""""""
import numpy as np
from matplotlib import pyplot as plt
import json


# ----------------------------------------------------------------------
def render_plotly_fig__(fig, chart):
    import json
    import plotly
    import js
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    js.Plotly.newPlot(chart, js.JSON.parse(graphJSON), {})

# # ----------------------------------------------------------------------
# @pyscript()
# def brython_serializer(data):
    # """"""
    # return json.dumps(data)


# ----------------------------------------------------------------------
def plot_non_inline_arg(f):
    """"""
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('Non-inline function [ARG]')
    x = np.linspace(0, 10, 1000)
    y = np.sinc(2 * np.pi * f * x)
    ax.plot(x, y, color='C1')

    return fig


# ----------------------------------------------------------------------
def plot_non_inline():
    """"""
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('Non-inline function')
    x = np.linspace(0, 10, 1000)
    y = np.sinc(2 * np.pi * 1 * x)
    ax.plot(x, y, color='C1')

    return fig


# ----------------------------------------------------------------------
def test_callback():
    """"""
    print('Callback not-inline')
    import json
    return json.dumps({'B': 100})
""""""
test_callback_inline()
