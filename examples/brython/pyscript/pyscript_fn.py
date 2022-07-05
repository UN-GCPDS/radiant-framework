

# ----------------------------------------------------------------------
def render_plotly_fig__(fig, chart):
    import json
    import plotly
    import js
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    js.Plotly.newPlot(chart, js.JSON.parse(graphJSON), {})

    return None


# ----------------------------------------------------------------------
def plot_sin(f=10):
    """"""
    import numpy as np
    from matplotlib import pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.linspace(0, 1, 1000)
    y = np.sin(2 * np.pi * f * x)
    ax.plot(x, y)

    return fig


# ----------------------------------------------------------------------
def plot_sinc(f):
    """"""
    import numpy as np
    from matplotlib import pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.linspace(0, 10, 1000)
    y = np.sin(2 * np.pi * f * x)
    ax.plot(x, y, color='C1')

    return fig
