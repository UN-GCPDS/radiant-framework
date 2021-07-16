# import html

from pygments import highlight
from pygments.lexers import Python3Lexer
from pygments.formatters import HtmlFormatter

import random
from string import ascii_lowercase

from docutils import nodes
from docutils.parsers.rst import directives, Directive


class brython_node(nodes.raw):
    pass


class Brython(Directive):
    has_content = True
    option_spec = {'hide-output': directives.flag,
                   # 'title': directives.unchanged,
                   # 'keywords': directives.unchanged,
                   # 'categories': directives.unchanged,
                   }

    def run(self):

        temp_id = ''.join([random.choice(ascii_lowercase)
                           for i in range(16)])

        text = self.highlight_code()
        text += f'<iframe src="about:blank" class="brython-out" id="iframe_{temp_id}"></iframe>'

        script = self.gen_script(temp_id)

        if 'hide-output' in self.options:
            style = 'style="display: none"'
        else:
            style = ''

        text += f"""
        <script type="text/python">

from browser import document
from radiant.utils import autoiframe

frame = document.select_one('#iframe_{temp_id}').contentDocument

frame.open()

frame.write("<scr"+"ipt type='text/javascript' src='/_static/brython/brython.js'></scr"+"ipt>")
frame.write("<scr"+"ipt type='text/javascript' src='/_static/brython/brython_stdlib.js'></scr"+"ipt>")
frame.write("<scr"+"ipt type='text/javascript' src='/_static/brython/material-components-web/material-components-web.min.js'></scr"+"ipt>")
frame.write("<link rel='stylesheet' type='text/css' href='/_static/brython/material-components-web/material-components-web.min.css'>")
frame.write("<link rel='stylesheet' type='text/css' href='/_static/theme.css'>")

frame.write("<link rel='stylesheet' type='text/css' href='/_static/brython/fonts/fontawesome-free-5.5.0-web/css/all.min.css'>")
frame.write("<link rel='stylesheet' type='text/css' href='/_static/brython/fonts/roboto-android/roboto.css'>")
frame.write("<link rel='stylesheet' type='text/css' href='/_static/brython/fonts/roboto-android/roboto-mono.css'>")
frame.write("<link rel='stylesheet' type='text/css' href='/_static/brython/fonts/material-design-icons-3.0.1/iconfont/material-icons.css'>")
frame.write("<link rel='stylesheet' type='text/css' href='/_static/custom_iframe.css'>")


frame.write("<scr"+"ipt type='text/javascript' src='/en/latest/_static/brython/brython.js'></scr"+"ipt>")
frame.write("<scr"+"ipt type='text/javascript' src='/en/latest/_static/brython/brython_stdlib.js'></scr"+"ipt>")
frame.write("<scr"+"ipt type='text/javascript' src='/en/latest/_static/brython/material-components-web/material-components-web.min.js'></scr"+"ipt>")
frame.write("<link rel='stylesheet' type='text/css' href='/en/latest/_static/brython/material-components-web/material-components-web.min.css'>")
frame.write("<link rel='stylesheet' type='text/css' href='/en/latest/_static/theme.css'>")

frame.write("<link rel='stylesheet' type='text/css' href='/en/latest/_static/brython/fonts/fontawesome-free-5.5.0-web/css/all.min.css'>")
frame.write("<link rel='stylesheet' type='text/css' href='/en/latest/_static/brython/fonts/roboto-android/roboto.css'>")
frame.write("<link rel='stylesheet' type='text/css' href='/en/latest/_static/brython/fonts/roboto-android/roboto-mono.css'>")
frame.write("<link rel='stylesheet' type='text/css' href='/en/latest/_static/brython/fonts/material-design-icons-3.0.1/iconfont/material-icons.css'>")
frame.write("<link rel='stylesheet' type='text/css' href='/en/latest/_static/custom_iframe.css'>")


frame.write("<scr"+"ipt type='text/python'>import sys;sys.path.append('/root/');sys.path.append('/static/Lib/site-packages/')</scr"+"ipt>")

frame.write('''{script}'''+"</scr"+"ipt>")
frame.write("<div class='brython-out' {style} id='{temp_id}'></div>")

frame.write("<scr"+"ipt type='text/python'>from radiant.utils import autoinit;autoinit()</scr"+"ipt>")

frame.write("<scr"+"ipt type='text/javascript'>brython()</scr"+"ipt>")

frame.close()

autoiframe("iframe_{temp_id}", ".brython-out")


        </script>
        """

        attributes = {'format': 'html', }
        node = brython_node(text=text, **attributes)

        return [node]

    # ----------------------------------------------------------------------
    def gen_script(self, temp_id):
        script = "<script type='text/python'>\n"
        script += "from browser import document\n"
        script += f"container = document.select('#{temp_id}')[0]\n"

        if self.content[0].endswith(';'):
            script += "\n".join(self.content.data[0].split('; '))
        else:
            script += "\n".join(self.content)

        script = script.replace('‘', "'")
        script = script.replace('’', "'")

        # script += "</script>\n"

        return script

    # ----------------------------------------------------------------------
    def highlight_code(self):
        """"""
        if self.content[0].endswith(';'):
            if '#!ignore' in self.content[0]:
                index = self.content[0].index('#!ignore')
                code = self.content[0][index + 8:-1]
                code = '\n'.join(code.split('; '))

            else:
                code = '\n'.join(self.content[0][:-1].split('; '))

        else:
            if '#!ignore' in self.content:
                index = self.content.index('#!ignore')
                code = self.content[index + 1:]
                code = '\n'.join(code)
            else:
                code = '\n'.join(self.content)

        code = code.replace('‘', '"')
        code = code.replace('’', '"')

        return highlight(code, Python3Lexer(), HtmlFormatter())


def setup(app):
    app.add_directive('brython_iframe', Brython)
    app.add_node(brython_node, html=(
        visit_brython, depart_brython), override=True)


def visit_brython(self, node):
    self.visit_raw(node)


def depart_brython(self, node):
    self.depart_raw(node)

