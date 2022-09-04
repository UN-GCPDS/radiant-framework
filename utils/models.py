from typing import Iterable


########################################################################
class Choices:
    """"""

    SUB_OCDE = (
        'Economía y negocios',
        'Ingeniería civil',
        'Ingeniería química',
        'Ingenierías eléctrica, electrónica e informática',
        'Otras ingenierías y tecnologías',
    )

    OCDE = (
        'Ciencias naturales',
        'Ingeniería y tecnología',
        'Ciencias médicas y de la salud',
        'Ciencias agrícolas',
        'Ciencias sociales',
        'Humanidades',
    )

    KNOWLEDGE = (
        'Ambiente y biodiversidad',
        'Arte y culturas',
        'Biotecnología',
        'Ciencia y tecnología de minerales y materiales',
        'Ciencias agrarias y desarrollo rural',
        'Construcción de ciudadanía e inclusión social',
        'Desarrollo organizacional, económico e industrial',
        'Energía',
        'Estados, sistemas políticos y jurídicos',
        'Hábitat, ciudad y territorio',
        'Salud y vida',
        'Tecnologías de la información y las comunicaciones',

        'Desarrollo organizacional económico e industrial',
        'Energía',
        'Hábitat, ciudad y territorio',
        'Tecnologías de la información y las comunicaciones'

    )

    DEPARTAMENT = (
        'Departamento de administración',
        'Departamento de ciencias humanas',
        'Departamento de física y química',
        'Departamento de informática y computación',
        'Departamento de ingeniería civil',
        'Departamento de ingeniería eléctrica, electrónica y computación',
        'Departamento de ingeniería industrial',
        'Departamento de ingeniería química',
        'Departamento de matemáticas',
        'Escuela de arquitectura y urbanismo',
        'Instituto de estudios ambientales - idea - manizales'
    )

    FACULTY = (
        'Facultad de administración',
        'Facultad de ciencias exactas y naturales',
        'Facultad de ingeniería y arquitectura',
        'Instituto de estudios ambientales - idea - manizales'
    )

    RESEARCHER_CATEGORY = (
        'Investigador asociado',
        'Investigador emerito',
        'Investigador junior',
        'Investigador senior',
        'Sin información'
    )

    GROUPS_CATEGORY = (
        'A1',
        'A',
        'B',
        'C',
        'No reconcido',
    )

    CALL_TYPE = (
        'Minciencias',
        'Regalías',
        'Interna',
        'Otra',
    )

    PROJECT_STATE = (
        'Propuesto',
        'No aprobado',
        'Activo',
        'Finalizado',
        'Sin finalizar',
    )

    # ----------------------------------------------------------------------
    def __new__(self, choices: str) -> dict:
        """"""
        assert getattr(
            self, choices, False), f"Choices for '{choices}' not found."

        n = 4
        prefix = choices.lower()
        choices = sorted(list(set(getattr(self, choices))))
        choices = [(f'{prefix}_{str(i).rjust(n, "0")}', choice)
                   for i, choice in enumerate(choices, start=1)]

        return {'max_length': len(choices[0][0]), 'choices': choices, }

