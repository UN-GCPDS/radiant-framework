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
        script = self.highlight_code()

        # print('#' * 20)
        # print(f'Length: {len(self.content)}')
        # print(self.content)

        script += self.gen_script(temp_id)

        if 'hide-output' in self.options:
            style = 'style="display: none"'
        else:
            style = ''

        script += '<div class="brython-out" {} id="{}"></div>\n'.format(
            style, temp_id)

        attributes = {'format': 'html', }
        node = brython_node(text=script, **attributes)

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
        script = script.replace('\_', "_")
        script = script.replace('!!!!', "    ")

        script += "</script>\n"

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
        code = code.replace('\_', "_")
        code = code.replace('!!!!', "    ")

        return highlight(code, Python3Lexer(), HtmlFormatter())


def setup(app):
    app.add_directive('brython', Brython)
    app.add_node(brython_node, html=(
        visit_brython, depart_brython), override=True)


def visit_brython(self, node):
    self.visit_raw(node)


def depart_brython(self, node):
    self.depart_raw(node)

