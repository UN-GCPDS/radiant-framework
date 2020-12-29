# import html

from pygments import highlight
from pygments.lexers import PythonLexer
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

        temp_id = ''.join([random.choice(ascii_lowercase) for i in range(16)])

        text = self.highlight_code()
        text += '<script type="text/python">\n'
        text += 'from browser import document\n'
        text += 'container = document.select("#{}")[0]\n'.format(temp_id)

        text += '\n'.join(self.content)
        text += '</script>\n'

        if 'hide-output' in self.options:
            style = 'style="display: none"'
        else:
            style = ''

        text += '<div class="brython-out" {} id="{}"></div>\n'.format(style, temp_id)

        attributes = {'format': 'html', }
        node = brython_node(text=text, **attributes)

        return [node]

    # ----------------------------------------------------------------------

    def highlight_code(self):
        """"""

        if '#!ignore' in self.content:
            index = self.content.index('#!ignore')
            code = self.content[index + 1:]
            code = '\n'.join(code)

        else:
            code = '\n'.join(self.content)

        return highlight(code, PythonLexer(), HtmlFormatter())


def setup(app):
    app.add_directive('brython', Brython)
    app.add_node(brython_node, html=(visit_brython, depart_brython), override=True)


def visit_brython(self, node):
    self.visit_raw(node)


def depart_brython(self, node):
    self.depart_raw(node)

