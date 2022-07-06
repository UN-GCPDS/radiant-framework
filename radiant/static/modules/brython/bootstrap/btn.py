from browser import window, html
from .base import Base

from typing import Literal, Optional

# primary
# secondary
# success
# danger
# warning
# info
# light
# dark
# link

['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'link']


########################################################################
class Button(Base):
    """"""

    CSS_classes = {

        # 'raised': 'mdc-button--raised',
        # 'unelevated': 'mdc-button--unelevated',
        # 'outlined': 'mdc-button--outlined',
        # 'dense': 'mdc-button--dense',
        'large': 'btn-lg',
        'small': 'btn-sm',

    }

    MDC_optionals = {

        'outline': '-outline',
        'disabled': 'disabled',

        # # 'reversed': 'style = "margin-left: 8px; margin-right: -4px;"',
        # # Icons
        # 'icon': '<i class="material-icons mdc-button__icon" aria-hidden="true">{icon}</i>',
        # 'fa_icon': '<i class="mdc-button__icon {fa_style} {fa_icon}"></i>',
        # 'label': '<span class="mdc-button__label">{label}</span>',
        # # <i class="material-icons mdc-button__icon" aria-hidden="true">favorite</i>


    }

    # ----------------------------------------------------------------------
    def __new__(self, text,
                style: Literal['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'link'] = 'primary',
                tag: Literal['link', 'button', 'input', 'submit', 'reset'] = 'button',
                outline: Optional[bool] = False,
                href='#',

                ** kwargs):
        """Constructor"""
        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""

        match context['tag']:
            case 'button':
                code = """<button type="button" class="btn btn{outline}-{style} {CSS_classes}" style="">{text}</button>"""
            case 'link':
                code = """<a class="btn btn{outline}-{style} {CSS_classes}" href="{href}" role="button">{text}</a>"""
            case _:
                code = """<input class="btn btn{outline}-{style} {CSS_classes}" type="{tag.replace('input', 'button')}" value="{text}">"""

        return cls.render_html(code, context)

