"""
Brython MDCComponent: MDCFormField
==================================


"""

from .core import MDCTemplate
from browser import html

########################################################################


class MDCFormField(MDCTemplate):
    """"""
    NAME = 'formField', 'MDCFormField'

    MDC_optionals = {
        'end': 'mdc-form-field--align-end',
    }

    # ----------------------------------------------------------------------

    def __new__(self, **kwargs):
        """"""
        self.element = self.render(locals(), kwargs)

        self.element.style = {'width': '100%',
                              'min-height': '48px',
                              # 'margin-bottom': '8px',
                              }

        return self.element

    # ----------------------------------------------------------------------

    @classmethod
    def __html__(cls, **context):
        """"""
        code = """
            <div class="mdc-form-field {end}"></div>
        """
        return cls.render_html(code, context)


########################################################################
class MDCForm(MDCTemplate):
    """"""

    # ----------------------------------------------------------------------
    def __new__(self, separator=None, formfield=None, formfield_style={}, **kwargs):
        """"""
        self.separator = separator
        self.formfield = formfield
        self.formfield_style = formfield_style
        # if formfield_style:
            # self.formfield = MDCFormField()
            # self.formfield.style = formfield_style

        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        code = """
            <form></form>
        """
        return cls.render_html(code, context)

    # ----------------------------------------------------------------------
    @classmethod
    def __genericElement__(cls, parent, Element, extern_label, *args, **kwargs):
        """"""
        if cls.formfield:
            formfield = cls.formfield.clone()
        else:
            formfield = MDCFormField()
            formfield.style = cls.formfield_style

        # elif cls.formfield_style:
            # formfield = MDCFormField(style=cls.formfield_style)

        # if 'formfield' in kwargs:
            # formfield = kwargs['formfield']

        el = Element(*args, **kwargs)
        formfield <= el
        if extern_label:
            formfield <= __formLabel__(id_=el.mdc.get_id(), label=args[0])
        if kwargs.get('helper_text', False):
            # print(kwargs.get('helper_text_persistent'))
            formfield <= __formHelper__(id_=el.mdc.get_id(), label=kwargs.get(
                'helper_text'), persistent=kwargs.get('helper_text_persistent', True))
        # cls.element <= formfield
        parent <= formfield

        if cls.separator:
            # cls.element <= cls.separator.clone()
            parent <= cls.separator.clone()

        return el, formfield

    # ----------------------------------------------------------------------

    @classmethod
    def Checkbox(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(
            element, MDCCheckbox, True, *args, **kwargs)
        return el

    # ----------------------------------------------------------------------

    @classmethod
    def Radio(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(
            element, MDCRadio, True, *args, **kwargs)

        # element.input = el
        return el

    # ----------------------------------------------------------------------

    @classmethod
    def Select(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(
            element, MDCSelect, False, *args, **kwargs)
        return el

    # ----------------------------------------------------------------------

    @classmethod
    def Slider(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(
            element, MDCSlider, False, *args, **kwargs)
        return el
    # ----------------------------------------------------------------------

    @classmethod
    def RangeSlider(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(
            element, MDCRangeSlider, False, *args, **kwargs)
        return el

    # ----------------------------------------------------------------------

    @classmethod
    def Switch(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(
            element, MDCSwitch, True, *args, **kwargs)
        return el

    # ----------------------------------------------------------------------

    @classmethod
    def TextField(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(
            element, MDCTextField, False, *args, **kwargs)
        element.style = {'display': 'flow-root'}
        el.style = {'margin-top': 'unset'}
        return el

    # ----------------------------------------------------------------------

    @classmethod
    def TextAreaField(cls, element, *args, **kwargs):
        """"""
        el, element = cls.__genericElement__(
            element, MDCTextAreaField, False, *args, **kwargs)
        element.style = {'display': 'flow-root'}
        el.style = {'margin-top': '8px'}
        return el


########################################################################
class __formLabel__(MDCTemplate):
    """"""

    # ----------------------------------------------------------------------
    def __new__(self, id_, label):
        """"""
        code = """
            <label for="{id_}">{label}</label>
            """.format(id_=id_, label=label)
        return self.render_str(code)


########################################################################
class __formHelper__(MDCTemplate):
    """"""
    NAME = 'textField', 'MDCTextFieldHelperText'

    # ----------------------------------------------------------------------
    def __new__(self, id_, label, persistent=True):
        """"""
        if persistent:
            persistent = 'mdc-text-field-helper-text--persistent'
        else:
            persistent = ''
        code = """
            <p id="{id_}" class="mdc-text-field-helper-text {persistent}" aria-hidden="true">
              {label}
            </p>
            """.format(id_=id_, label=label, persistent=persistent)
        return self.render_str(code)


########################################################################
class MDCCheckbox(MDCTemplate):
    """"""
    NAME = 'checkbox', 'MDCCheckbox'

    MDC_optionals = {

        'disabled': 'mdc-checkbox--disabled',
        'checked': 'checked',

    }

    # ----------------------------------------------------------------------

    def __new__(self, label, name='', value='', checked=False, disabled=False, **kwargs):
        """"""
        self.element = self.render(locals(), kwargs)
        # self.element.need_label = True
        return self.element

    # ----------------------------------------------------------------------

    @classmethod
    def __html__(cls, **context):
        """"""

        cls.ID = cls.new_id()
        context['id'] = cls.ID

        code = """
            <div class="mdc-checkbox  {disabled}">
              <input type="checkbox" class="mdc-checkbox__native-control"
              id="{id}
              name="{name}"
              value="{value}"
              {checked}
              "/>
              <div class="mdc-checkbox__background">
                <svg class="mdc-checkbox__checkmark"
                     viewBox="0 0 24 24">
                  <path class="mdc-checkbox__checkmark-path"
                        fill="none"
                        d="M1.73,12.91 8.1,19.28 22.79,4.59"/>
                </svg>
                <div class="mdc-checkbox__mixedmark"></div>
              </div>
              <div class="mdc-checkbox__ripple"></div>
            </div>
        """
        return cls.render_html(code, context)


########################################################################
class MDCRadio(MDCTemplate):
    """"""
    NAME = 'radio', 'MDCRadio'

    MDC_optionals = {

        'disabled': 'mdc-radio--disabled',
        'checked': 'checked',

    }

    # ----------------------------------------------------------------------

    def __new__(self, label, name='', checked=False, disabled=False, **kwargs):
        """"""
        self.element = self.render(locals(), kwargs)
        # self.element.need_label = True
        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""

        cls.ID = cls.new_id()
        context['id'] = cls.ID

        if context['disabled']:
            context['input_disabled'] = 'disabled'
        else:
            context['input_disabled'] = ''

        code = """
            <div class="mdc-radio {disabled}">
              <input class="mdc-radio__native-control" type="radio" id="{id}" name="{name}" {input_disabled} {checked}>
              <div class="mdc-radio__background">
                <div class="mdc-radio__outer-circle"></div>
                <div class="mdc-radio__inner-circle"></div>
              </div>
              <div class="mdc-radio__ripple"></div>
            </div>
        """
        return cls.render_html(code, context)


########################################################################
class MDCSelect(MDCTemplate):
    """"""
    NAME = 'select', 'MDCSelect'

    MDC_optionals = {

        'disabled': 'mdc-select--disabled',
        'filled': 'mdc-select--filled',
        'outline': 'mdc-select--outline',

    }

    # ----------------------------------------------------------------------

    def __new__(self, label, options=[], selected=None, disabled=False, filled=False, outline=False, **kwargs):
        """"""
        self.element = self.render(locals(), kwargs, attach_now=False)
        # self.element.need_label = False

        if (not filled) and (not outline):
            filled = True

        if options:
            self.add_options(self.element, options, selected)
        self.attach()

        return self.element

    # ----------------------------------------------------------------------

    @classmethod
    def __html__(cls, **context):
        """"""

        cls.ID = cls.new_id()
        context['id'] = cls.ID

        # print('3' * 70)
        # print(context['outline'])
        # print(context['filled'])

        if context['outline']:
            code = """

                <div class="mdc-select mdc-select--outlined">
                  <div class="mdc-select__anchor" aria-labelledby="outlined-select-label">
                    <span class="mdc-notched-outline">
                      <span class="mdc-notched-outline__leading"></span>
                      <span class="mdc-notched-outline__notch">
                        <span id="outlined-select-label" class="mdc-floating-label">{label}</span>
                      </span>
                      <span class="mdc-notched-outline__trailing"></span>
                    </span>
                    <span class="mdc-select__selected-text-container">
                      <span id="demo-selected-text" class="mdc-select__selected-text">{selected}</span>
                    </span>


                    <span class="mdc-select__dropdown-icon">
                      <svg
                          class="mdc-select__dropdown-icon-graphic"
                          viewBox="7 10 10 5" focusable="false">
                        <polygon
                            class="mdc-select__dropdown-icon-inactive"
                            stroke="none"
                            fill-rule="evenodd"
                            points="7 10 12 15 17 10">
                        </polygon>
                        <polygon
                            class="mdc-select__dropdown-icon-active"
                            stroke="none"
                            fill-rule="evenodd"
                            points="7 15 12 10 17 15">
                        </polygon>
                      </svg>
                    </span>
                  </div>

                    <div class="mdc-select__menu mdc-menu mdc-menu-surface mdc-menu-surface--fullwidth">
                      <ul class="mdc-list" role="listbox">
                      </ul>
                    </div>
                </div>
            """

        else:
            code = """
                <div class="mdc-select mdc-select--filled">
                  <div class="mdc-select__anchor"
                       role="button"
                       aria-haspopup="listbox"
                       aria-expanded="false"
                       aria-labelledby="demo-label demo-selected-text">

                    <span class="mdc-select__ripple"></span>
                    <span id="demo-label" class="mdc-floating-label">{label}</span>

                    <span class="mdc-select__selected-text-container">
                      <span id="demo-selected-text" class="mdc-select__selected-text">{selected}</span>
                    </span>
                    <span class="mdc-select__dropdown-icon">
                      <svg
                          class="mdc-select__dropdown-icon-graphic"
                          viewBox="7 10 10 5" focusable="false">
                        <polygon
                            class="mdc-select__dropdown-icon-inactive"
                            stroke="none"
                            fill-rule="evenodd"
                            points="7 10 12 15 17 10">
                        </polygon>
                        <polygon
                            class="mdc-select__dropdown-icon-active"
                            stroke="none"
                            fill-rule="evenodd"
                            points="7 15 12 10 17 15">
                        </polygon>
                      </svg>
                    </span>
                    <span class="mdc-line-ripple"></span>
                  </div>

                  <div class="mdc-select__menu mdc-menu mdc-menu-surface mdc-menu-surface--fullwidth">
                    <ul class="mdc-list" role="listbox">
                    </ul>

                  </div>
                </div>
            """

        return cls.render_html(code, context)

    # ----------------------------------------------------------------------
    @classmethod
    def get(self, name):
        """"""
        if name is 'options_placeholder':
            return self.element.select('ul.mdc-list')[0]
        elif name is 'label':
            return self.element.select('.mdc-select__selected-text')[0]
        elif name is 'value':
            return self.element.select('.mdc-select__selected-text')[0].text

    # ----------------------------------------------------------------------
    @classmethod
    def add_option(cls, element, label, value, selected=False, disabled=False):
        """"""
        option = __selectItem__(label, value=value,
                                selected=selected, disabled=disabled)

        cls.get('options_placeholder') <= option
        return option

    # ----------------------------------------------------------------------
    @classmethod
    def add_options(cls, element, options, selected=None):
        """"""
        # if selected is None:
            # cls.add_option(element, '', '', selected=True)
        # else:
            # cls.get('label').class_name += cls.get('label').class_name.replace('mdc-list-item--selected', '')

        # if selected is None:
            # selected = options[0][1]

        if selected:
            cls.get('label').text = selected

        for option in options:
            cls.add_option(element, *option, option[1] == selected)


########################################################################
class __selectItem__(MDCTemplate):
    """"""

    MDC_optionals = {

        'selected': 'mdc-list-item--selected',

        'disable': 'mdc-list-item--disabled',
        # 'stack' = '{}'
        # 'icon': '<i class="radiant-menu-icon material-icons" aria-hidden="true" style="margin-right: 15px;">{icon}</i>',
        # 'fa_icon': '<i class="radiant-menu-icon {fa_style} {fa_icon}" style="margin-right: 15px;"></i>',

    }

    # ----------------------------------------------------------------------
    def __new__(self, label, value, selected=False, disable=False, **kwargs):
        """"""

        self.element = self.render(locals(), kwargs)

        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""
        if context['selected']:
            context['aria_selected'] = 'aria-selected="true"'
        else:
            context['aria_selected'] = 'aria-selected="false"'

        if context['disable']:
            context['aria_disabled'] = 'aria-selected="true"'
        else:
            context['aria_disabled'] = 'aria-selected="false"'

        code = """
            <li class="mdc-list-item {disable} {selected}" {aria_selected} data-value="{value}" {aria_disabled} role="option">
              <span class="mdc-list-item__ripple"></span>
              <span class="mdc-list-item__text">
                {label}
              </span>
            </li>
        """
        return cls.render_html(code, context)

    # # ----------------------------------------------------------------------
    # @classmethod
    # def get(self, name):
        # """"""
        # if name is 'icon':
            # return self.element.select('.radiant-menu-icon')[0]


########################################################################
class MDCSlider(MDCTemplate):
    """"""
    NAME = 'slider', 'MDCSlider'

    MDC_optionals = {

        'disabled': 'mdc-slider--disabled',
        'marks': 'mdc-slider--tick-marks',

    }

    # ----------------------------------------------------------------------
    def __new__(self, label, min=0, max=100, value=50, step=1, discrete=False, marks=False, continuous=False, disabled=False, **kwargs):
        """"""

        if not discrete and not continuous:
            continuous = True

        self.element = self.render(locals(), kwargs)
        # self.element.need_label = False

        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""

        cls.ID = cls.new_id()
        context['id'] = cls.ID

        if context['disabled']:
            context['input_disabled'] = 'disabled'
        else:
            context['input_disabled'] = ''

        if context.get('continuous'):
            code = """

                <div class="mdc-slider {disabled}">
                  <input class="mdc-slider__input" {input_disabled} type="range" min="{min}" max="{max}" value="{value}" step="{step}" name="name-{id}" aria-label="Continuous slider demo">
                  <div class="mdc-slider__track">
                    <div class="mdc-slider__track--inactive"></div>
                    <div class="mdc-slider__track--active">
                      <div class="mdc-slider__track--active_fill"></div>
                    </div>
                  </div>
                  <div class="mdc-slider__thumb">
                    <div class="mdc-slider__thumb-knob"></div>
                  </div>
                </div>

            """

        elif context.get('discrete'):
            code = """
                <div class="mdc-slider {disabled} mdc-slider--discrete {marks}">
                  <input class="mdc-slider__input" {input_disabled} type="range" min="{min}" max="{max}" value="{value}" "name-{id}" step="{step}" aria-label="Discrete slider demo">
                  <div class="mdc-slider__track">
                    <div class="mdc-slider__track--inactive"></div>
                    <div class="mdc-slider__track--active">
                      <div class="mdc-slider__track--active_fill"></div>
                    </div>
                  </div>
                  <div class="mdc-slider__thumb">
                    <div class="mdc-slider__value-indicator-container">
                      <div class="mdc-slider__value-indicator">
                        <span class="mdc-slider__value-indicator-text">
                          {value}
                        </span>
                      </div>
                    </div>
                    <div class="mdc-slider__thumb-knob"></div>
                  </div>
                </div>
            """

        return cls.render_html(code, context)


########################################################################
class MDCRangeSlider(MDCTemplate):
    """"""
    NAME = 'slider', 'MDCSlider'

    MDC_optionals = {

        'disabled': 'mdc-slider--disabled',

    }

    # ----------------------------------------------------------------------
    def __new__(self, label, min=0, max=100, value_lower=0, value_upper=100, step=1, disabled=False, **kwargs):
        """"""
        self.element = self.render(locals(), kwargs)
        # self.element.need_label = False

        return self.element

    # ----------------------------------------------------------------------
    @classmethod
    def __html__(cls, **context):
        """"""

        cls.ID = cls.new_id()
        context['id'] = cls.ID

        if context['disabled']:
            context['input_disabled'] = 'disabled'
        else:
            context['input_disabled'] = ''

        code = """
            <div class="mdc-slider mdc-slider--range {disabled}">
              <input class="mdc-slider__input" {input_disabled} type="range" min="{min}", step="{step}" max="{max}" value="{value_lower}" name="rangeStart-{id}" aria-label="Range lower slider demo">
              <input class="mdc-slider__input" {input_disabled} type="range" min="{min}", step="{step}" max="{max}" value="{value_upper}" name="rangeEnd-{id}" aria-label="Range upper slider demo">
              <div class="mdc-slider__track">
                <div class="mdc-slider__track--inactive"></div>
                <div class="mdc-slider__track--active">
                  <div class="mdc-slider__track--active_fill"
                       style="transform:scaleX(.4); left:30%"></div>
                </div>
              </div>
              <div class="mdc-slider__thumb" style="left:calc(30%-24px)">
                <div class="mdc-slider__thumb-knob"></div>
              </div>
              <div class="mdc-slider__thumb" style="left:calc(70%-24px)">
                <div class="mdc-slider__thumb-knob"></div>
              </div>
            </div>
        """

        return cls.render_html(code, context)


########################################################################
class MDCSwitch(MDCTemplate):
    """"""
    NAME = 'switchControl', 'MDCSwitch'

    MDC_optionals = {

        'disabled': 'disabled',
        # 'box': 'mdc-select--box',
        'checked': 'mdc-switch--checked',

    }

    # ----------------------------------------------------------------------

    def __new__(self, label, checked=True, **kwargs):
        """"""
        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------

    @classmethod
    def __html__(cls, **context):
        """"""

        cls.ID = cls.new_id()
        context['id'] = cls.ID

        if context.get('checked'):
            context['native_checked'] = 'checked'
        else:
            context['native_checked'] = ''

        code = """
        <div class="mdc-switch {checked}">
          <div class="mdc-switch__track"></div>
          <div class="mdc-switch__thumb-underlay">
            <div class="mdc-switch__thumb">
                <input type="checkbox" id="{id}" class="mdc-switch__native-control" role="switch" {native_checked}>
            </div>
          </div>
        </div>
        """

        return cls.render_html(code, context)


########################################################################
class MDCTextField(MDCTemplate):
    """"""
    NAME = 'textField', 'MDCTextField'

    MDC_optionals = {

        'disabled': 'mdc-text-field--disabled',
        # 'box': 'mdc-select--box',
        # 'fullwidth': 'mdc-text-field--fullwidth',

        'value': 'value="{value}"',


    }

    # ----------------------------------------------------------------------

    def __new__(self, label, value=False, type='text', leading_icon=False, trailing_icon=False, helper_text=False, helper_text_persistent=True, outlined=False, disabled=False, filled=False, **kwargs):
        """"""

        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------

    @classmethod
    def __html__(cls, **context):
        """"""
        cls.ID = cls.new_id()
        context['id'] = cls.ID

        if context['disabled']:
            context['input_disabled'] = 'mdc-text-field--disabled'
        else:
            context['input_disabled'] = ''

        if context['value']:
            context['upgraded'] = 'mdc-text-field--upgraded'
            context['floating'] = 'mdc-text-field--label-floating'
            context[
                'float_above'] = f'<span class="mdc-floating-label mdc-floating-label--float-above" id="my-label-id">{context["helper_text"]}</span>'
        else:
            context['upgraded'] = ''
            context['floating'] = ''
            context['float_above'] = ''

        # if context['helper_text']:
            # context['helper_text'] = 'aria-controls="username-helper-text" aria-describedby="username-helper-text"'
        # else:
            # context['helper_text'] = ''

        # if context['leading_icon']:
            # context['icon'] = '<i class="material-icons mdc-text-field__icon" tabindex="0" role="button">{icon}</i>'.format(
                # icon=context['leading_icon'])
            # context['leading_icon'] = 'mdc-text-field--with-leading-icon'

        # elif context['trailing_icon']:
            # context['icon'] = '<i class="material-icons mdc-text-field__icon" tabindex="0" role="button">{icon}</i>'.format(
                # icon=context['trailing_icon'])
            # context['trailing_icon'] = 'mdc-text-field--with-trailing-icon'

        # else:
            # context['leading_icon'] = ''
            # context['trailing_icon'] = ''
            # context['icon'] = ''

        if context.get('outlined'):
            code = """
                <label class="mdc-text-field mdc-text-field--outlined {input_disabled} {floating}">
                  <span class="mdc-notched-outline">
                    <span class="mdc-notched-outline__leading"></span>
                    <span class="mdc-notched-outline__notch">
                      <span class="mdc-floating-label" id="{id}">{label}</span>
                    </span>
                    <span class="mdc-notched-outline__trailing"></span>
                  </span>
                  <input type="text" class="mdc-text-field__input" aria-labelledby="{id}" {value}>
                </label>
            """

        elif context.get('filled'):

            if context.get('value'):
                code = """
                    <label class="mdc-text-field mdc-text-field--filled">
                      <span class="mdc-text-field__ripple"></span>
                      <span class="mdc-floating-label" id="label-{id}">{label}</span>
                      <input class="mdc-text-field__input" type="text" id={id}
                             aria-labelledby="label-{id}"
                             aria-controls="helper-{id}"
                             aria-describedby="my-helper-id"
                             {value}>
                      <span class="mdc-line-ripple"></span>
                    </label>
                    <div class="mdc-text-field-helper-line"><label class="mdc-text-field mdc-text-field--filled mdc-ripple-upgraded" id="[object Object]" style="margin-top: unset;width: 100%;">…</label>flex
                      <div class="mdc-text-field-helper-text" id="helper-{id}" aria-hidden="true">{helper_text}</div>
                    </div>
                    """

            else:
                code = """
                    <label class="mdc-text-field mdc-text-field--filled">
                      <span class="mdc-text-field__ripple"></span>
                      <span class="mdc-floating-label" id="label-{id}">{label}</span>
                      <input class="mdc-text-field__input" type="text" id={id}
                             aria-labelledby="label-{id}"
                             aria-controls="helper-{id}"
                             aria-describedby="my-helper-id">
                      <span class="mdc-line-ripple"></span>
                    </label>
                    <div class="mdc-text-field-helper-line">
                      <div class="mdc-text-field-helper-text" id="helper-{id}" aria-hidden="true">{helper_text}</div>
                    </div>
                    """

        return cls.render_html(code, context)


########################################################################
class MDCTextAreaField(MDCTemplate):
    """"""
    NAME = 'textField', 'MDCTextField'

    MDC_optionals = {

        'disabled': 'mdc-text-field--disabled',
        # 'dense': 'mdc-text-field--dense',
        # 'box': 'mdc-select--box',
        'fullwidth': 'mdc-text-field--fullwidth',

        # 'value': 'value="{value}"',


    }

    # ----------------------------------------------------------------------

    def __new__(self, label, value='', rows='2', cols='40', helper_text=False, helper_text_persistent=True, disabled=False, fullwidth=False, **kwargs):
        """"""

        self.element = self.render(locals(), kwargs)
        return self.element

    # ----------------------------------------------------------------------

    @classmethod
    def __html__(cls, **context):
        """"""
        cls.ID = cls.new_id()
        context['id'] = cls.ID

        if context['disabled']:
            context['input_disabled'] = 'disabled'
        else:
            context['input_disabled'] = ''

        if context['helper_text']:
            context['helper_text'] = 'aria-controls="username-helper-text" aria-describedby="username-helper-text"'
        else:
            context['helper_text'] = ''

        code = """
        <div class="mdc-text-field mdc-text-field--textarea {fullwidth} {disabled}">
          <textarea id="{id}" class="mdc-text-field__input" rows="{rows}" cols="{cols}" {helper_text} {input_disabled}>{value}</textarea>

            <div class="mdc-notched-outline">
              <div class="mdc-notched-outline__leading"></div>
              <div class="mdc-notched-outline__notch">
                <label for="{id}" class="mdc-floating-label">{label}</label>
              </div>
              <div class="mdc-notched-outline__trailing"></div>
            </div>

        </div>
        """

        return cls.render_html(code, context)
