from browser import html, window
from typing import Callable, Literal


ACCENTS = Literal['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'link']


########################################################################
class MDCObject():
    """"""
    # ----------------------------------------------------------------------

    def __init__(self, view, mdc, element, name='MDCObject'):
        """Constructor"""
        self.__mdc__ = mdc
        self.__view__ = view
        self.__element__ = element

    # ----------------------------------------------------------------------
    def __getattr__(self, attr):
        """"""
        # check first for existence in view model, the method in view model can use MDC call
        if hasattr(self.__view__, attr):
            def inset(*args, **kwargs):
                # must be a classmethod
                return getattr(self.__view__, attr)(self.__element__, *args, **kwargs)
            return inset

        # else, define in the view models then look up in MDC (foundation is not defined here)
        elif hasattr(self.__mdc__, attr):
            return getattr(self.__mdc__, attr)

    # ----------------------------------------------------------------------
    def __getitem__(self, item):
        """"""
        # views can define and use a __getitem__ as a shortcut
        return self.__view__[item]


########################################################################
class Base:
    """"""
    NAME = None
    CSS_classes = {}
    MDC_optionals = {}

    # ----------------------------------------------------------------------
    @classmethod
    def render(cls, locals_, kwargs, attach_now=True):
        """"""
        context = locals_.copy()
        if 'self' in context:
            context.pop('self')
        if 'kwargs' in context:
            context.pop('kwargs')
        context.update(**kwargs)

        cls.html_element = cls.__html__(**context)

        if attach_now:
            cls.attach()

        if 'Class' in kwargs:
            if cls.html_element.class_name:
                cls.html_element.class_name += ' {Class}'.format(
                    **kwargs)
            else:
                cls.html_element.class_name = '{Class}'.format(**kwargs)

        if 'id' in kwargs:
            cls.html_element.attrs['id'] = kwargs['id']
        else:
            cls.ID = cls.new_id()
            kwargs['id'] = cls.ID

        if 'style' in kwargs:
            if kwargs['style']:
                cls.html_element.style = kwargs['style']

        if 'attr' in kwargs:
            for attr in kwargs['attr']:
                cls.html_element.attrs[attr] = kwargs['attr'][attr]

        for arg in kwargs:
            if arg.startswith('on_'):
                # print(f"{arg.replace('on_', '')}, {kwargs[arg]}")
                cls.html_element.addEventListener(arg.replace('on_', ''), kwargs[arg])

        return cls.html_element

    # ----------------------------------------------------------------------
    @classmethod
    def render_html(cls, code, context):
        """"""
        classes = []
        for key in cls.CSS_classes.keys():
            if context.get(key, False):
                classes.append(cls.CSS_classes[key])
        context['CSS_classes'] = ' '.join(classes)

        for key in cls.MDC_optionals.keys():
            if context.get(key, False):

                try:
                    # context[key] = cls.MDC_optionals[key].format(**context)
                    context[key] = eval(f"""f'''{cls.MDC_optionals[key]}'''""", context)
                    # context[key] = eval(f'f"{cls.MDC_optionals[key]}"', context)
                except:

                    context[key] = cls.MDC_optionals[key]

            else:
                context[key] = ''

        # code = code.format(**context)
        code = eval(f"""f'''{code}'''""", context)

        return cls.render_str(code)

    # ----------------------------------------------------------------------
    @classmethod
    def render_str(cls, code):
        """"""
        return html.DIV(code.strip()).children[0]

    # ----------------------------------------------------------------------
    @classmethod
    def bind(self, element, evt, callback: Callable):
        """"""
        element.addEventListener(evt, callback)

    # ----------------------------------------------------------------------
    @classmethod
    def attach(cls):
        """"""

        if cls.NAME is None:
            cls.html_element.bs = MDCObject(cls, None, cls.html_element)
            cls.bs = cls.html_element.bs
            return

        cls.html_element.bs = MDCObject(cls, None, cls.html_element)
        cls.bs = cls.html_element.bs
        cls.bs = getattr(window.bootstrap, cls.NAME).new(cls.html_element)
        cls.html_element.bs = MDCObject(cls, cls.bs, cls.html_element)

    # ----------------------------------------------------------------------
    @classmethod
    def new_id(cls):
        """"""
        ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        import random
        return ''.join([random.choice(ascii_lowercase) for l in range(2**5)])

    # ----------------------------------------------------------------------
    @classmethod
    def get_id(cls, element=None):
        """"""
        return cls.ID
