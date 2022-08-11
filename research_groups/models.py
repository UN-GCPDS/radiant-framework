from django.db.models import Q
from django.db import models


########################################################################
class Researcher(models.Model):
    """"""
    ROLES = (
            ('pr', 'Professor'),
            ('st', 'Student'),
    )
    first_name = models.CharField(max_length=2**6)
    last_name = models.CharField(max_length=2**6)
    role = models.CharField(max_length=2, choices=ROLES)

    # ----------------------------------------------------------------------
    def __str__(self):
        """"""
        return self.first_name


########################################################################
class ResearchGroup(models.Model):
    """"""
    SUB_OCDE = (

        ('aaa', 'bbb'),
    )

    OCDE = (
        ('nat', 'Ciencias naturales'),
        ('ing', 'Ingeniería y tecnología'),
        ('med', 'Ciencias médicas y de la salud'),
        ('agr', 'Ciencias agrícolas'),
        ('soc', 'Ciencias sociales'),
        ('hum', 'Humanidades'),

    )

    KNOWLEDGE = (

        ('amb', 'Ambiente y biodiversidad'),
        ('art', 'Arte y culturas'),
        ('bio', 'Biotecnología'),
        ('tec', 'Ciencia y tecnología de minerales y materiales'),
        ('agr', 'Ciencias agrarias y desarrollo rural'),
        ('ciu', 'Construcción de ciudadanía e inclusión social'),
        ('des', 'Desarrollo organizacional, económico e industrial'),
        ('ene', 'Energía'),
        ('est', 'Estados, sistemas políticos y jurídicos'),
        ('hab', 'Hábitat, ciudad y territorio'),
        ('sal', 'Salud y vida'),
        ('tic', 'Tecnologías de la información y las comunicaciones (TIC)'),




    )

    DEPARTAMENTS = (
        ('admin', 'Departamento de administración'),
        ('human', 'Departamento de ciencias humanas'),
        ('fisic', 'Departamento de física y química'),
        ('infor', 'Departamento de informática y computación'),
        ('civil', 'Departamento de ingeniería civil'),
        ('elect', 'Departamento de ingeniería eléctrica, electrónica y computación'),
        ('indus', 'Departamento de ingeniería industrial'),
        ('chemi', 'Departamento de ingeniería química'),
        ('maths', 'Departamento de matemáticas'),
        ('archi', 'Escuela de arquitectura y urbanismo'),
    )

    FACULTIES = (

        ('admin', 'Facultad de administración'),
        ('exact', 'Facultad de ciencias excatas y naturales'),
        ('ingen', 'Facultad de ingeniería y arquitectura'),
    )

    CATEGORIES = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B', 'B'),
        ('C', 'C'),
        ('NA', 'No reconcido'),
    )

    name = models.CharField(max_length=2**6)
    leader = models.OneToOneField(Researcher, on_delete=models.SET_NULL, null=True, blank=True, related_name='leader', limit_choices_to=Q(role='pr'))

    faculty = models.CharField(max_length=5, choices=FACULTIES)
    departament = models.CharField(max_length=5, choices=DEPARTAMENTS)

    category = models.CharField(max_length=2, choices=CATEGORIES)

    sub_ocde = models.CharField(max_length=3, choices=SUB_OCDE)
    ocde = models.CharField(max_length=3, choices=OCDE)
    knowledge = models.CharField(max_length=3, choices=KNOWLEDGE)

    researchers = models.ManyToManyField(Researcher, related_name='researchers')



