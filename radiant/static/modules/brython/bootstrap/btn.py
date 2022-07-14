from browser import window, html
from .base import Base, ACCENTS

from typing import Literal, Optional


########################################################################
class Button(Base):
    """"""
    NAME = 'Button'

    CSS_classes = {
        'large': 'btn-lg',
        'small': 'btn-sm',
        'active': 'active',
    }

    MDC_optionals = {
        'outline': '-outline',
        'disabled': 'disabled',
        'toggle': 'data-bs-toggle="button"',
    }

    # ----------------------------------------------------------------------
    def __new__(self, text,
                accent: ACCENTS = 'primary',
                tag: Literal['link', 'button', 'input', 'submit', 'reset'] = 'button',
                outline: Optional[bool] = False,
                href='#',

                **kwargs):
        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        match context['tag']:
            case 'button':
                code = """<button type="button" class="btn btn{outline}-{accent} {CSS_classes}" style="" {disabled} {toggle}>{text}</button>"""
            case 'link':
                code = """<a class="btn btn{outline}-{accent} {CSS_classes}" href="{href}" role="button" {disabled} {toggle}>{text}</a>"""
            case _:
                code = """<input class="btn btn{outline}-{accent} {CSS_classes}" type="{tag.replace('input', 'button')}" value="{text}" {disabled} {toggle}>"""

        return cls.render_html(code, context)


########################################################################
class ButtonGroup(Base):
    """"""
    CSS_classes = {
        'large': 'btn-group-lg',
        'small': 'btn-group-sm',
    }

    MDC_optionals = {

        'vertical': '-vertical',

    }

    # ----------------------------------------------------------------------
    def __new__(self, role: Literal['group', 'toolbar'] = 'group', **kwargs):
        """"""
        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        code = """
        <div class="btn-group{vertical} {CSS_classes}" role="{role}">
        </div>
        """
        return cls.render_html(code, context)

    # ----------------------------------------------------------------------
    @classmethod
    def add_button(cls, element, text: str,
                   accent: Optional[ACCENTS] = 'primary',
                   checked: Optional[bool] = False,
                   radio: Optional[bool] = False,
                   checkbox: Optional[bool] = False):
        """"""
        id = cls.new_id()
        in_ = html.INPUT()
        if radio:
            in_.attrs['type'] = 'radio'
            in_.attrs['name'] = 'btnradio'
        elif checkbox:
            in_.attrs['type'] = 'checkbox'

        in_.attrs['id'] = f'btncheck-{id}'
        in_.attrs['class'] = 'btn-check'
        in_.attrs['autocomplete'] = 'off'

        lb_ = html.LABEL(text)
        lb_.attrs['class'] = f'btn btn-outline-{accent}'
        lb_.attrs['for'] = f'btncheck-{id}'

        if checked:
            in_.attrs['checked'] = ''

        cls.element <= in_
        cls.element <= lb_


########################################################################
class ButtonToolbar(Base):
    """"""

    # ----------------------------------------------------------------------
    def __new__(self, **kwargs):
        """"""
        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        code = """
        <div class="btn-toolbar" role="toolbar">
        </div>
        """
        return cls.render_html(code, context)
