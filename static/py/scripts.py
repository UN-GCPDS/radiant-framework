from browser import document, bind, window
from browser import ajax
import json


def read(req):

    document.select_one('#placeholder').html = req.text
    window.eval(document.select_one('#my_id-script').innerHTML)


# ----------------------------------------------------------------------
@bind('#test-button', 'click')
def test_click(evt):
    """"""
    req = ajax.ajax()
    req.bind('complete', read)
    req.open('POST', "/load_template", True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send({'data': json.dumps({
        "template": 'bars',
        "id": 'my_id',
        'height': '300px',
        'x': [1, 2, 3, 4],
        'y': ["1", "2", "3", "4"],

    }), 'csrfmiddlewaretoken': window.CSRF_TOKEN})






