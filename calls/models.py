from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from tinymce.models import HTMLField
from datetime import date
import random
import os

upload_to_internal_call = os.path.join('uploads', 'calls_internal')
upload_to_external_call = os.path.join('uploads', 'calls_external')
upload_to_join_call = os.path.join('uploads', 'calls_join')
upload_to_student_call = os.path.join('uploads', 'calls_student')


########################################################################
class InternalCall(models.Model):
    """"""
    image = models.FileField('Imagen de convocatoria', upload_to=upload_to_internal_call, help_text='Opcional', blank=True, null=True)
    expiration = models.DateField('Finalización', help_text='Hasta cuando está abierta la convocatoria')
    link = models.URLField('Link de referencia')
    title = models.CharField('Título', max_length=2 ** 10)
    objective = HTMLField('Objetivo', max_length=2 ** 12)
    headed = HTMLField('Dirigido a', max_length=2 ** 12)
    active = models.BooleanField('Convocatoria activa', help_text='Oculta la convoctaria de la vista pública', default=True)

    # ----------------------------------------------------------------------
    class Meta:
        verbose_name = "Convocatoria interna"
        verbose_name_plural = "Convocatorias internas"

    @property
    # ----------------------------------------------------------------------
    def color(self):
        """"""
        return random.choice([
            '#CCA529',
            '#B45C18',
            '#341B4D',
            '#135714',
            '#67160E',
            '#153465',
        ])

    # ----------------------------------------------------------------------
    @property
    def expired(self):
        return date.today() > self.expiration

    # ----------------------------------------------------------------------
    @property
    def show(self):
        return self.active and not self.expired


    # ----------------------------------------------------------------------
    def __str__(self):
        return f'Convocatoria interna (ID:#{self.pk})'


########################################################################
class MincienciasCall(models.Model):
    """"""
    image = models.FileField('Imagen de convocatoria', upload_to=upload_to_internal_call, help_text='Opcional', blank=True, null=True)
    expiration = models.DateField('Finalización', help_text='Hasta cuando está abierta la convocatoria')
    link = models.URLField('Link de referencia')
    title = models.CharField('Título', max_length=2 ** 10)
    objective = HTMLField('Objetivo', max_length=2 ** 12)
    headed = HTMLField('Dirigido a', max_length=2 ** 12)
    active = models.BooleanField('Convocatoria activa', help_text='Oculta la convoctaria de la vista pública', default=True)

    # ----------------------------------------------------------------------
    class Meta:
        verbose_name = "Convocatoria de Minciencias"
        verbose_name_plural = "Convocatorias de Minciencias"


    @property
    # ----------------------------------------------------------------------
    def color(self):
        """"""
        return random.choice([
            '#CCA529',
            '#B45C18',
            '#341B4D',
            '#135714',
            '#67160E',
            '#153465',
        ])

    # ----------------------------------------------------------------------
    @property
    def expired(self):
        return date.today() > self.expiration

    # ----------------------------------------------------------------------
    @property
    def show(self):
        return self.active and not self.expired


    # ----------------------------------------------------------------------
    def __str__(self):
        return f'Convocatoria de Minciencias (ID:#{self.pk})'


########################################################################
class JointCall(models.Model):
    """"""
    image = models.FileField('Imagen de convocatoria', upload_to=upload_to_join_call, help_text='Opcional', blank=True, null=True)
    expiration = models.DateField('Finalización', help_text='Hasta cuando está abierta la convocatoria')
    link = models.URLField('Link de referencia')
    title = models.CharField('Título', max_length=2 ** 10)
    objective = HTMLField('Objetivo', max_length=2 ** 12)
    headed = HTMLField('Dirigido a', max_length=2 ** 12)
    active = models.BooleanField('Convocatoria activa', help_text='Oculta la convoctaria de la vista pública', default=True)


    # ----------------------------------------------------------------------
    class Meta:
        verbose_name = "Convocatoria conjunta"
        verbose_name_plural = "Convocatorias conjuntas"

    # ----------------------------------------------------------------------
    @property
    def expired(self):
        return date.today() > self.expiration

    # ----------------------------------------------------------------------
    @property
    def show(self):
        return self.active and not self.expired

    # ----------------------------------------------------------------------
    def __str__(self):
        return f'Convocatoria conjunta (ID:#{self.pk})'


########################################################################
class StudentsCall(models.Model):
    """"""
    title = models.CharField('Título', max_length=2 ** 10)
    expiration = models.DateField('Finalización', help_text='Hasta cuando está abierta la convocatoria')
    funding = models.CharField('Recursos del proyecto', max_length=2 ** 12)
    supervise = models.CharField('Profesor responsable', max_length=2 ** 12)
    students = models.IntegerField('Estudiantes', help_text='Cantidad de estudiantes en la convocatoria')
    profile = HTMLField('Perfil', max_length=2 ** 12)
    time = models.IntegerField('Tiempo', help_text='Horas a la semana')
    economic_stimulus = models.CharField('Estímulo económico', help_text='ej. 3 pagos de $2.000.000 y uno de $350.000', max_length=2 ** 12)
    period = models.CharField('Periodo', max_length=2 ** 10, help_text='ej. 3 Meses y 5 días')
    active = models.BooleanField('Convocatoria activa', help_text='Oculta la convoctaria de la vista pública', default=True)

    # Anexo no recbir benificios
    # ----------------------------------------------------------------------
    class Meta:
        verbose_name = "Convocatoria para estudiantes auxiliares"
        verbose_name_plural = "Convocatorias para estudiantes auxiliares"

    # ----------------------------------------------------------------------
    @property
    def expired(self):
        return date.today() > self.expiration

    # ----------------------------------------------------------------------
    @property
    def show(self):
        return self.active and not self.expired

    # ----------------------------------------------------------------------
    def __str__(self):
        return f'Convocatoria para estudiante axiliar (ID:#{self.pk})'


########################################################################
class Timeline_JointCall(models.Model):
    joint_call = models.ForeignKey('calls.JointCall', related_name='timeline', on_delete=models.CASCADE)
    activity = models.CharField('Actividad', max_length=2 ** 10)
    start_date = models.DateField('Fecha de inicio')
    end_date = models.DateField('Fecha de finalización', help_text='Opcional', blank=True, null=True)

    class Meta:
        verbose_name = "Cronograma"
        verbose_name_plural = "Cronograma"

    @property
    # ----------------------------------------------------------------------
    def expired(self):
        return max(filter(None, [self.end_date, self.start_date])) <= date.today()


########################################################################
class TermsOfReference_JointCall(models.Model):
    joint_call = models.ForeignKey('calls.JointCall', related_name='terms_of_reference', on_delete=models.CASCADE)
    name = models.CharField('Nombre del archivo', max_length=2 ** 10)
    terms_of_reference = models.FileField('Archivo', upload_to=upload_to_student_call, blank=True, null=True)

    class Meta:
        verbose_name = "Términos de referencia"
        verbose_name_plural = "Términos de referencia"


########################################################################
class Annex_JointCall(models.Model):
    joint_call = models.ForeignKey('calls.JointCall', related_name='annex', on_delete=models.CASCADE)
    name = models.CharField('Nombre del archivo', max_length=2 ** 10)
    annex = models.FileField('Anexo', upload_to=upload_to_student_call, blank=True, null=True)

    class Meta:
        verbose_name = "Anexo"


########################################################################
class Result_JointCall(models.Model):
    joint_call = models.ForeignKey('calls.JointCall', related_name='results', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=2 ** 10)
    results = models.FileField('result', upload_to=upload_to_join_call, blank=True, null=True)

    class Meta:
        verbose_name = "Result"


########################################################################
class TermsOfReference_StudentsCall(models.Model):
    joint_call = models.ForeignKey('calls.StudentsCall', related_name='terms_of_reference', on_delete=models.CASCADE)
    name = models.CharField('Nombre del archivo', max_length=2 ** 10)
    terms_of_reference = models.FileField('Archivo', upload_to=upload_to_student_call, blank=True, null=True)

    class Meta:
        verbose_name = "Términos de referencia"
        verbose_name_plural = "Términos de referencia"


########################################################################
class Annex_StudentsCall(models.Model):
    joint_call = models.ForeignKey('calls.StudentsCall', related_name='annex', on_delete=models.CASCADE)
    name = models.CharField('Nombre del archivo', max_length=2 ** 10)
    annex = models.FileField('Anexo', upload_to=upload_to_student_call, blank=True, null=True)

    class Meta:
        verbose_name = "Anexo"


########################################################################
class Result_StudentsCall(models.Model):
    joint_call = models.ForeignKey('calls.StudentsCall', related_name='result', on_delete=models.CASCADE)
    name = models.CharField('Nombre del archivo', max_length=2 ** 10)
    result = models.FileField('Archivo', upload_to=upload_to_student_call, blank=True, null=True)

    class Meta:
        verbose_name = "Resultado"


########################################################################
class Timeline_InternalCall(models.Model):
    joint_call = models.ForeignKey('calls.InternalCall', related_name='timeline', on_delete=models.CASCADE)
    activity = models.CharField('Actividad', max_length=2 ** 10)
    start_date = models.DateField('Fecha de inicio')
    end_date = models.DateField('Fecha de finalización', help_text='Opcional', blank=True, null=True)

    # ----------------------------------------------------------------------
    @property
    def expired(self):
        return max(filter(None, [self.end_date, self.start_date])) <= date.today()

    # ----------------------------------------------------------------------
    class Meta:
        verbose_name = "Cronograma"
        verbose_name_plural = "Cronograma"


########################################################################
class TermsOfReference_InternalCall(models.Model):
    joint_call = models.ForeignKey('calls.InternalCall', related_name='terms_of_reference', on_delete=models.CASCADE)
    name = models.CharField('Nombre del archivo', max_length=2 ** 10)
    terms_of_reference = models.FileField('Archivo', upload_to=upload_to_internal_call, blank=True, null=True)

    class Meta:
        verbose_name = "Términos de referencia"
        verbose_name_plural = "Términos de referencia"


########################################################################
class Annex_InternalCall(models.Model):
    joint_call = models.ForeignKey('calls.InternalCall', related_name='annex', on_delete=models.CASCADE)
    name = models.CharField('Nombre del archivo', max_length=2 ** 10)
    annex = models.FileField('Anexo', upload_to=upload_to_internal_call, blank=True, null=True)

    class Meta:
        verbose_name = "Anexo"


########################################################################
class Result_InternalCall(models.Model):
    joint_call = models.ForeignKey('calls.InternalCall', related_name='results', on_delete=models.CASCADE)
    name = models.CharField('Nombre del archivo', max_length=2 ** 10)
    results = models.FileField('Archivo', upload_to=upload_to_internal_call, blank=True, null=True)

    class Meta:
        verbose_name = "Resultado"


# ----------------------------------------------------------------------
@receiver(post_delete, sender=InternalCall)
def on_post_delete_InternalCall(sender, instance, **kwargs):
    """"""
    for object_ in ['image']:
        if file := getattr(instance, object_, None):
            if os.path.isfile(file.path):
                os.remove(file.path)


# ----------------------------------------------------------------------
@receiver(post_delete, sender=MincienciasCall)
def on_post_delete_MincienciasCall(sender, instance, **kwargs):
    """"""
    for object_ in ['image']:
        if file := getattr(instance, object_, None):
            if os.path.isfile(file.path):
                os.remove(file.path)


# ----------------------------------------------------------------------
@receiver(post_delete, sender=TermsOfReference_InternalCall)
def on_post_delete_TermsOfReference_InternalCall(sender, instance, **kwargs):
    """"""
    for object_ in ['terms_of_reference']:
        if file := getattr(instance, object_, None):
            if os.path.isfile(file.path):
                os.remove(file.path)


# ----------------------------------------------------------------------
@receiver(post_delete, sender=Annex_InternalCall)
def on_post_delete_Annex_InternalCall(sender, instance, **kwargs):
    """"""
    for object_ in ['annex']:
        if file := getattr(instance, object_, None):
            if os.path.isfile(file.path):
                os.remove(file.path)


# ----------------------------------------------------------------------
@receiver(post_delete, sender=Result_InternalCall)
def on_post_delete_Result_InternalCall(sender, instance, **kwargs):
    """"""
    for object_ in ['results']:
        if file := getattr(instance, object_, None):
            if os.path.isfile(file.path):
                os.remove(file.path)


# ----------------------------------------------------------------------
@receiver(post_delete, sender=TermsOfReference_JointCall)
def on_post_delete_TermsOfReference_JointCall(sender, instance, **kwargs):
    """"""
    for object_ in ['terms_of_reference']:
        if file := getattr(instance, object_, None):
            if os.path.isfile(file.path):
                os.remove(file.path)


# ----------------------------------------------------------------------
@receiver(post_delete, sender=Annex_JointCall)
def on_post_delete_Annex_JointCall(sender, instance, **kwargs):
    """"""
    for object_ in ['annex']:
        if file := getattr(instance, object_, None):
            if os.path.isfile(file.path):
                os.remove(file.path)


# ----------------------------------------------------------------------
@receiver(post_delete, sender=Result_JointCall)
def on_post_delete_Result_JointCall(sender, instance, **kwargs):
    """"""
    for object_ in ['results']:
        if file := getattr(instance, object_, None):
            if os.path.isfile(file.path):
                os.remove(file.path)


# ----------------------------------------------------------------------
@receiver(post_delete, sender=TermsOfReference_StudentsCall)
def on_post_delete_TermsOfReference_StudentsCall(sender, instance, **kwargs):
    """"""
    for object_ in ['terms_of_reference']:
        if file := getattr(instance, object_, None):
            if os.path.isfile(file.path):
                os.remove(file.path)


# ----------------------------------------------------------------------
@receiver(post_delete, sender=Annex_StudentsCall)
def on_post_delete_Annex_StudentsCall(sender, instance, **kwargs):
    """"""
    for object_ in ['annex']:
        if file := getattr(instance, object_, None):
            if os.path.isfile(file.path):
                os.remove(file.path)


# ----------------------------------------------------------------------
@receiver(post_delete, sender=Result_StudentsCall)
def on_post_delete_Result_StudentsCall(sender, instance, **kwargs):
    """"""
    for object_ in ['results']:
        if file := getattr(instance, object_, None):
            if os.path.isfile(file.path):
                os.remove(file.path)
