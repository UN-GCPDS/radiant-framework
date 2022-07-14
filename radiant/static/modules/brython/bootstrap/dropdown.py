from .base import Base, ACCENTS
from typing import Literal, Optional, List
from browser import html


########################################################################
class Dropdown(Base):
    """"""

    CSS_classes = {
        'large': 'btn-lg',
        'small': 'btn-sm',
        'split': 'dropdown-toggle-split',
    }

    MDC_optionals = {
        'large': 'btn-lg',
        'small': 'btn-sm',
        'split': '<button type="button" class="btn btn-{accent} {large} {small}">{text}</button>',
        'dark': 'dropdown-menu-dark',
    }

    # ----------------------------------------------------------------------

    def __new__(self, text: str,
                accent: Optional[ACCENTS] = 'primary',
                options: Optional[list] = [],
                split: Optional[bool] = False,
                direction: Optional[Literal['center', 'dropup', 'dropup-center', 'dropend', 'dropstart']] = None,
                **kwargs):
        """"""
        match direction:
            case 'center':
                kwargs['direction'] = 'dropdown-center'
            case 'dropup':
                kwargs['direction'] = 'btn-group dropup'
            case 'dropup-center':
                kwargs['direction'] = 'dropup-center dropup'
            case 'dropend':
                kwargs['direction'] = 'btn-group dropend'
            case 'dropstart':
                kwargs['direction'] = 'btn-group dropstart'
            case _:
                kwargs['direction'] = 'btn-group'

        self.element = self.render(locals(), kwargs)

        self.add_options(self.element, options)
        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        code = """
        <div class="{direction}">
          {split}
          <button class="btn btn-{accent} dropdown-toggle {CSS_classes}" type="button" id="{id}" data-bs-toggle="dropdown" aria-expanded="false">
            <span class="{'visually-hidden' if split else ''}">{text}</span>
          </button>
          <ul class="dropdown-menu {dark}" aria-labelledby="{id}">
          </ul>
        </div>
        """

        return cls.render_html(code, context)

    # ----------------------------------------------------------------------
    @classmethod
    def add_options(self, element, options: list[tuple]):
        """"""
        for option in options:
            item = __dropown_item__(**option)
            element.select_one('.dropdown-menu') <= item


########################################################################
class __dropown_item__(Base):
    """"""

    MDC_optionals = {
        'disabled': 'disabled',
        'active': 'active',
    }

    # ----------------------------------------------------------------------
    def __new__(self, text='', href='#', header=False, divider=False, **kwargs):
        """Constructor"""

        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        if context['divider']:
            code = """<li><hr class="dropdown-divider"></li>"""
        elif context['header']:
            code = """<li><h6 class="dropdown-header">{header}</h6></li>"""
        else:
            code = """<li><a class="dropdown-item {disabled} {active}" href="{href}">{text}</a></li>"""
        return cls.render_html(code, context)

