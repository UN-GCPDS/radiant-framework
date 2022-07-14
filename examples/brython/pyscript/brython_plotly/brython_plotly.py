#!brython

from radiant.server import RadiantAPI, RadiantServer, pyscript, pyscript_globals
from browser import document, html
import bootstrap as bs


########################################################################
class BareMinimum(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        document.select_one('.top') <= html.H1('Radiant-Framework')

        document.select_one('.top') <= html.DIV(id='mpl')
        document.select_one('.top') <= bs.Button('Plot', 'primary', on_click=lambda evt: self.show_plot())

    # ----------------------------------------------------------------------
    @pyscript_globals
    def _(self):
        """"""
        # Import libraries
        import pandas as pd
        import matplotlib.pyplot as plt
        import js
        import json
        import plotly
        import plotly.express as px

        # Get the data
        from pyodide.http import open_url

        from js import document
        from pyodide import create_proxy

    # ----------------------------------------------------------------------
    @pyscript(output=None)
    def show_plot(self):
        """"""
        url = 'https://raw.githubusercontent.com/alanjones2/uk-historical-weather/main/data/Heathrow.csv'
        url_content = open_url(url)

        df = pd.read_csv(url_content)
        df = df[df['Year'] == 2020]

        def plot(chart):
            fig = px.line(df,
                          x="Month", y=chart,
                          width=800, height=400)
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            js.plot(graphJSON, "chart1")

        def selectChange(event):
            choice = document.getElementById("select").value
            plot(choice)

        def setup():
            # Create a JsProxy for the callback function
            change_proxy = create_proxy(selectChange)

            e = document.getElementById("select")
            e.addEventListener("change", change_proxy)

        setup()

        plot('Tmax')


if __name__ == '__main__':
    RadiantServer('BareMinimum',
                  template='layout.html')
