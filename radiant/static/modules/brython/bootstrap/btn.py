from browser import window, html
from .base import Base


# primary
# secondary
# success
# danger
# warning
# info
# light
# dark
# link


########################################################################
class Button(Base):
    """"""

    CSS_classes = {

        # 'raised': 'mdc-button--raised',
        # 'unelevated': 'mdc-button--unelevated',
        # 'outlined': 'mdc-button--outlined',
        # 'dense': 'mdc-button--dense',

    }

    MDC_optionals = {

        # 'disabled': 'disabled',
        # # 'reversed': 'style = "margin-left: 8px; margin-right: -4px;"',
        # # Icons
        # 'icon': '<i class="material-icons mdc-button__icon" aria-hidden="true">{icon}</i>',
        # 'fa_icon': '<i class="mdc-button__icon {fa_style} {fa_icon}"></i>',
        # 'label': '<span class="mdc-button__label">{label}</span>',
        # # <i class="material-icons mdc-button__icon" aria-hidden="true">favorite</i>


    }

    # ----------------------------------------------------------------------
    def __new__(self, text, mode='primary', **kwargs):
        """Constructor"""
        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        code = """
        <button type="button" class="btn btn-{mode}" style="margin-right: 4px;">{text}</button>
        """
        return cls.render_html(code, context)

