import base64
import io
import js
import sys


class fake:
    def __init__(self, submodules=None, *args, **kwargs):
        """"""
        self.submodules = submodules

    def __getattr__(self, attr):
        if attr in self.submodules:
            return self.submodules[attr]
        else:
            return fake


########################################################################
class RadiantAPI:
    """"""

    # ----------------------------------------------------------------------
    def fig2img(self, fig, id=None):
        """"""
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        img_str = 'data:image/png;base64,' + base64.b64encode(
            buf.read()
        ).decode('UTF-8')

        img = js.document.createElement("img")
        if id:
            img.id = id
        img.src = img_str
        return img


sys.modules["radiant"] = fake()
sys.modules["radiant.server"] = fake({'RadiantAPI': RadiantAPI})
