from typing import Iterable


########################################################################
class Choices:
    """"""

    OCDE = (
        'Matemática',
        'Computación y ciencias de la información',
        'Ciencias físicas',
        'Ciencias químicas',
        'Ciencias de la tierra y medioambientales',
        'Ciencias biológicas',
        'Otras ciencias naturales',

        'Ingeniería civil',
        'Ingenierías eléctrica, electrónica e informática',
        'Ingeniería mecánica',
        'Ingeniería química',
        'Ingeniería de materiales',
        'Ingeniería médica',
        'Ingeniería ambiental',
        'Biotecnología ambiental',
        'Biotecnología industrial',
        'Nanotecnología',
        'Otras ingenierías tecnologías',

        'Medicina básica',
        'Medicina clínica',
        'Ciencias de la salud',
        'Biotecnología en salud',
        'Otras ciencias médicas',

        'Agricultura, silvicultura y pesca',
        'Ciencias animales y lechería',
        'Ciencias veterinarias',
        'Biotecnología agrícola',
        'Otras ciencias agrícolas',

        'Psicología',
        'Economía y negocios',
        'Ciencias de la educación',
        'Sociología',
        'Derecho',
        'Ciencias políticas',
        'Geografía social y económica',
        'Periodismo y comunicaciones',
        'Otras ciencias sociales',

        'Historia y arqueología',
        'Idiomas y literatura',
        'Otras historias',
        'Arte',
        'Otras humanidades'
    )

    KNOWLEDGE = (
        'Ambiente y biodiversidad',
        'Arte y cultura',
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
        'No reconocido',
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

    PATENT_TYPE = (
        'Patente de invención',
        'Patente modelo de utilidad',
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

