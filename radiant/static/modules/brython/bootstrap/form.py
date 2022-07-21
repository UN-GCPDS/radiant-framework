from browser import window, html, document
from .base import Base, ACCENTS

from typing import Literal, Optional


########################################################################
class Select(Base):
    """"""

    # ----------------------------------------------------------------------
    def __new__(self, text, options=[], **kwargs):
        """Constructor"""

        self.element = self.render(locals(), kwargs)
        self.add_options(self.element, options)

        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        code = """
        <select class="form-select" aria-label="Default select example">
        </select>
        """
        return cls.render_html(code, context)

    # ----------------------------------------------------------------------
    @classmethod
    def add_options(self, element, options: list[tuple]):
        """"""
        for option in options:
            element <= html.OPTION(option['text'], value=option['value'], selected=option.get('selected', False))

    # ----------------------------------------------------------------------
    @classmethod
    def clear(self, element):
        """"""
        for o in element.select('option'):
            o.remove()
