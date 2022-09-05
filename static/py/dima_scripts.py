from browser import document, window, ajax
import json
import logging


# ----------------------------------------------------------------------
def ajax_render(id, url, data=None):
    """"""
    def read(req):
        document.select_one(f'#{id}').html = req.text
        if script := document.select_one(f'#{id}-script'):
            if size := document.select_one(f'#{id}').attrs.get('dima-size', False):
                document.select_one(f'#{id}').style = {'height': f'{60 * float(size)}px'}
            elif size := script.attrs.get('dima-size', False):
                document.select_one(f'#{id}').style = {'height': f'{60 * float(size)}px'}
            window.eval(script.innerHTML)

    req = ajax.ajax()
    req.bind('complete', read)
    req.open('POST', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send({'data': json.dumps(data), 'csrfmiddlewaretoken': window.CSRF_TOKEN})


# ----------------------------------------------------------------------
def update_plot(id, filters=None):
    """"""
    if not document.select_one(f'#{id}'):
        logging.warning("Missing '{id}' id")
        return
    data = {
        "id": id,
        "context": document.select_one(f'#{id}').attrs.get('dima-context', None),
        'filters': filters,
    }
    ajax_render(id, "/load_template", data)


# ----------------------------------------------------------------------
def ajax_request(url, data=None, callback=None):
    """"""
    req = ajax.ajax()
    req.bind('complete', callback)
    req.open('POST', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send({**data, 'csrfmiddlewaretoken': window.CSRF_TOKEN})
