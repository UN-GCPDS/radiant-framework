from browser import document, window, ajax
import json
import logging


# ----------------------------------------------------------------------
def ajax_render(id, url, data=None, callback=None, execute_scripts=True):
    """"""
    def read(req):
        document.select_one(f'#{id}').html = req.text

        if execute_scripts:
            if script := document.select_one(f'#{id}-script'):
                if size := document.select_one(f'#{id}').attrs.get('dima-size', False):
                    document.select_one(f'#{id}').style = {
                        'height': f'{60 * float(size)}px'}
                elif size := script.attrs.get('dima-size', False):
                    document.select_one(f'#{id}').style = {
                        'height': f'{60 * float(size)}px'}
                window.eval(script.innerHTML)

        if callback:
            callback(req)

    req = ajax.ajax()
    req.bind('complete', read)
    req.open('POST', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send({'data': json.dumps(data),
             'csrfmiddlewaretoken': window.CSRF_TOKEN})


# ----------------------------------------------------------------------
def ajax_request(url, data=None, callback=None, method='POST'):
    """"""
    req = ajax.ajax()
    req.bind('complete', callback)
    req.open(method, url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send({**data, 'csrfmiddlewaretoken': window.CSRF_TOKEN})


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


# # ----------------------------------------------------------------------
# def binds(selectors, event):
    # """"""
    # def fn(*args, **kwargs):
        # for selector in selectors:
            # document.select_one(selector).bind(event, fn)
    # return fn
