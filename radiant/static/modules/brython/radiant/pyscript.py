class fake:
    def __getattr__(self, attr):
        return fake


import sys

import js
import io, base64

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
sys.modules["radiant.server"] = fake()
sys.modules["radiant.server.RadiantAPI"] = RadiantAPI
