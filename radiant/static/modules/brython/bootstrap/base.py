from browser import html


########################################################################
class Base:
    """"""

    # ----------------------------------------------------------------------
    @classmethod
    def render(cls, locals_, kwargs):
        """"""
        context = locals_.copy()
        if 'self' in context:
            context.pop('self')
        if 'kwargs' in context:
            context.pop('kwargs')
        context.update(**kwargs)

        cls.html_element = cls.__html__(**context)

        # if attach_now:
            # cls.attach()

        if 'Class' in kwargs:
            if cls.html_element.class_name:
                cls.html_element.class_name += ' {Class}'.format(
                    **kwargs)
            else:
                cls.html_element.class_name = '{Class}'.format(**kwargs)

        if 'id' in kwargs:
            cls.html_element.attrs['id'] = kwargs['id']

        if 'style' in kwargs:
            if kwargs['style']:
                cls.html_element.style = kwargs['style']

        if 'attr' in kwargs:
            for attr in kwargs['attr']:
                cls.html_element.attrs[attr] = kwargs['attr'][attr]

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
                    context[key] = cls.MDC_optionals[key].format(
                        **context)
                except:

                    context[key] = cls.MDC_optionals[key]

            else:
                context[key] = ''

        code = code.format(**context)

        return cls.render_str(code)

    # ----------------------------------------------------------------------
    @classmethod
    def render_str(cls, code):
        """"""
        return html.DIV(code.strip()).children[0]

    # ----------------------------------------------------------------------
    def bind(self, evt, callback):
        """"""
        self.element.addEventListener(evt, callback)

