"""
Brython MDCComponent: MDCCard
=============================


"""

from .core import MDCTemplate
from .MDCButton import MDCButton, MDCIconToggle

########################################################################


class MDCCard(MDCTemplate):
    """"""

    NAME = 'card', 'MDCCcard'

    MDC_optionals = {

        'outlined': 'mdc-card--outlined',
        'square': 'mdc-card__media--square',
        '_16_9': 'mdc-card__media--16-9',
        'full_bleed': 'mdc-card__actions--full-bleed',
        "primary_action": "mdc-card__primary-action",

    }

    # ----------------------------------------------------------------------
    def __new__(self, title='', subtitle='', media_content='', text_content='', square=True, **kwargs):
        """"""
        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        code = """
<div class="mdc-card">
  <div class="mdc-card__primary-action">
    <div class="mdc-card__media mdc-card__media--square">
      <div class="mdc-card__media-content">Title</div>
    </div>
    <!-- ... additional primary action content ... -->
  </div>
  <div class="mdc-card__actions">
    <div class="mdc-card__action-buttons">
      <button class="mdc-button mdc-card__action mdc-card__action--button">
        <div class="mdc-button__ripple"></div>
        <span class="mdc-button__label">Action 1</span>
      </button>
      <button class="mdc-button mdc-card__action mdc-card__action--button">
        <div class="mdc-button__ripple"></div>
        <span class="mdc-button__label">Action 2</span>
      </button>
    </div>
    <div class="mdc-card__action-icons">
      <button class="material-icons mdc-icon-button mdc-card__action mdc-card__action--icon" title="Share">share</button>
      <button class="material-icons mdc-icon-button mdc-card__action mdc-card__action--icon" title="More options">more_vert</button>
    </div>
  </div>
</div>
        """

        code = """
<div class="mdc-card demo-card">
  <div class="mdc-card__primary-action demo-card__primary-action" tabindex="0">
    <div class="mdc-card__media mdc-card__media--16-9 demo-card__media" style="background-image: url(&quot;https://material-components.github.io/material-components-web-catalog/static/media/photos/3x2/2.jpg&quot;);"></div>
    <div class="demo-card__primary">
      <h2 class="demo-card__title mdc-typography mdc-typography--headline6">Our Changing Planet</h2>
      <h3 class="demo-card__subtitle mdc-typography mdc-typography--subtitle2">by Kurt Wagner</h3>
    </div>
    <div class="demo-card__secondary mdc-typography mdc-typography--body2">Visit ten places on our planet that are undergoing the biggest changes today.</div>
  </div>
  <div class="mdc-card__actions">
    <div class="mdc-card__action-buttons">
      <button class="mdc-button mdc-card__action mdc-card__action--button">  <span class="mdc-button__ripple"></span> Read</button>
      <button class="mdc-button mdc-card__action mdc-card__action--button">  <span class="mdc-button__ripple"></span> Bookmark</button>
    </div>
    <div class="mdc-card__action-icons">
      <button class="mdc-icon-button mdc-card__action mdc-card__action--icon--unbounded" aria-pressed="false" aria-label="Add to favorites" title="Add to favorites">
        <i class="material-icons mdc-icon-button__icon mdc-icon-button__icon--on">favorite</i>
        <i class="material-icons mdc-icon-button__icon">favorite_border</i>
      </button>
      <button class="mdc-icon-button material-icons mdc-card__action mdc-card__action--icon--unbounded" title="Share" data-mdc-ripple-is-unbounded="true">share</button>
      <button class="mdc-icon-button material-icons mdc-card__action mdc-card__action--icon--unbounded" title="More options" data-mdc-ripple-is-unbounded="true">more_vert</button>
    </div>
  </div>
</div>
        """

        return cls.render_html(code, context)

    # ----------------------------------------------------------------------
    @classmethod
    def get(self, name):
        """"""
        if name is 'actions':
            return self.element.select('.mdc-card__actions')[0]

        elif name is 'title':
            return self.element.select('.radian-title')[0]

        elif name is 'subtitle':
            return self.element.select('.radian-subtitle')[0]

        elif name is 'header':
            return self.element.select('.radiant-title__header')[0]

        elif name is 'content':
            return self.element.select('.radian-content')[0]

        elif name is 'media':
            return self.element.select('.mdc-card__media')[0]

        elif name is 'media_content':
            return self.element.select('.mdc-card__media-content')[0]

        elif name is 'action_buttons':
            return self.element.select('.mdc-card__action-buttons')[0]

        elif name is 'action_icons':
            return self.element.select('.mdc-card__action-icons')[0]

    # ----------------------------------------------------------------------
    @classmethod
    def add_action_button(cls, element, *args, **kwargs):
        """"""
        button = MDCButton(*args, **kwargs)
        button.class_name += ' mdc-card__action mdc-card__action--button'
        cls.get('action_icons') <= button

        return button

    # ----------------------------------------------------------------------
    @classmethod
    def add_action_icontoggle(cls, element, *args, **kwargs):
        """"""
        button = MDCIconToggle(*args, **kwargs)
        button.class_name += ' mdc-card__action mdc-card__action--icon'
        cls.get('action_icons') <= button

        return button

    # ----------------------------------------------------------------------
    @classmethod
    def add_action_icon(cls, element, icon, *args, **kwargs):
        """"""
        button = MDCButton(icon=icon, *args, **kwargs)
        button.class_name += ' mdc-card__action mdc-card__action--icon'
        cls.get('action_icons') <= button

        return button
