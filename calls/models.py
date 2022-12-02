from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
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
    image = models.FileField('call', upload_to=upload_to_internal_call, blank=True, null=True)
    expiration = models.DateField('expiration')
    link = models.URLField('link')
    title = models.CharField('title', max_length=2 ** 10)
    objective = models.TextField('objective', max_length=2 ** 12)
    headed = models.TextField('headed', max_length=2 ** 12)
    active = models.BooleanField('active', default=True)

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


########################################################################
class MincienciasCall(models.Model):
    """"""
    image = models.FileField('call', upload_to=upload_to_internal_call, blank=True, null=True)
    expiration = models.DateField('expiration')
    link = models.URLField('link')
    title = models.CharField('title', max_length=2 ** 10)
    objective = models.TextField('objective', max_length=2 ** 12)
    headed = models.TextField('headed', max_length=2 ** 12)
    active = models.BooleanField('active', default=True)

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


########################################################################
class JointCall(models.Model):
    """"""
    image = models.FileField('call', upload_to=upload_to_join_call, blank=True, null=True)
    expiration = models.DateField('expiration')
    link = models.URLField('link')
    title = models.CharField('title', max_length=2 ** 10)
    objective = models.TextField('objective', max_length=2 ** 12)
    headed = models.TextField('headed', max_length=2 ** 12)
    active = models.BooleanField('active', default=True)

    # ----------------------------------------------------------------------
    @property
    def expired(self):
        return date.today() > self.expiration

    # ----------------------------------------------------------------------
    @property
    def show(self):
        return self.active and not self.expired


########################################################################
class StudentsCall(models.Model):
    """"""
    title = models.CharField('title', max_length=2 ** 10)
    expiration = models.DateField('expiration')
    funding = models.CharField('funding', max_length=2 ** 12)
    supervise = models.CharField('supervise', max_length=2 ** 12)
    students = models.IntegerField('students')
    profile = models.TextField('profile', max_length=2 ** 12)
    time = models.IntegerField('time', help_text='Horas a la semana')
    economic_stimulus = models.CharField('economic stimulus', max_length=2 ** 12)
    period = models.CharField('period', max_length=2 ** 10, help_text='ej. 3 Meses y 5 días')
    active = models.BooleanField('active', default=True)

    # Anexo no recbir benificios

    # ----------------------------------------------------------------------
    @property
    def expired(self):
        return date.today() > self.expiration

    # ----------------------------------------------------------------------
    @property
    def show(self):
        return self.active and not self.expired


########################################################################
class Timeline_JointCall(models.Model):
    joint_call = models.ForeignKey('calls.JointCall', related_name='timeline', on_delete=models.CASCADE)
    activity = models.CharField('activity', max_length=2 ** 10)
    start_date = models.DateField('start date')
    end_date = models.DateField('finalization date', blank=True, null=True)

    class Meta:
        verbose_name = "Timeline"

    @property
    # ----------------------------------------------------------------------
    def expired(self):
        return max(filter(None, [self.end_date, self.start_date])) <= date.today()


########################################################################
class TermsOfReference_JointCall(models.Model):
    joint_call = models.ForeignKey('calls.JointCall', related_name='terms_of_reference', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=2 ** 10)
    terms_of_reference = models.FileField('terms of reference', upload_to=upload_to_join_call, blank=True, null=True)

    class Meta:
        verbose_name = "Terms of reference"


########################################################################
class Annex_JointCall(models.Model):
    joint_call = models.ForeignKey('calls.JointCall', related_name='annex', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=2 ** 10)
    annex = models.FileField('annex', upload_to=upload_to_join_call, blank=True, null=True)

    class Meta:
        verbose_name = "Annex"


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
    name = models.CharField('name', max_length=2 ** 10)
    terms_of_reference = models.FileField('terms of reference', upload_to=upload_to_student_call, blank=True, null=True)

    class Meta:
        verbose_name = "Terms of reference"


########################################################################
class Annex_StudentsCall(models.Model):
    joint_call = models.ForeignKey('calls.StudentsCall', related_name='annex', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=2 ** 10)
    annex = models.FileField('annex', upload_to=upload_to_student_call, blank=True, null=True)

    class Meta:
        verbose_name = "Annex"


########################################################################
class Result_StudentsCall(models.Model):
    joint_call = models.ForeignKey('calls.StudentsCall', related_name='results', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=2 ** 10)
    results = models.FileField('results', upload_to=upload_to_student_call, blank=True, null=True)

    class Meta:
        verbose_name = "Result"


########################################################################
class Timeline_InternalCall(models.Model):
    joint_call = models.ForeignKey('calls.InternalCall', related_name='timeline', on_delete=models.CASCADE)
    activity = models.CharField('activity', max_length=2 ** 10)
    start_date = models.DateField('start date')
    end_date = models.DateField('finalization date', blank=True, null=True)

    # ----------------------------------------------------------------------
    @property
    def expired(self):
        return max(filter(None, [self.end_date, self.start_date])) <= date.today()

    class Meta:
        verbose_name = "Timeline"


########################################################################
class TermsOfReference_InternalCall(models.Model):
    joint_call = models.ForeignKey('calls.InternalCall', related_name='terms_of_reference', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=2 ** 10)
    terms_of_reference = models.FileField('terms of reference', upload_to=upload_to_internal_call, blank=True, null=True)

    class Meta:
        verbose_name = "Terms of reference"


########################################################################
class Annex_InternalCall(models.Model):
    joint_call = models.ForeignKey('calls.InternalCall', related_name='annex', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=2 ** 10)
    annex = models.FileField('annex', upload_to=upload_to_internal_call, blank=True, null=True)

    class Meta:
        verbose_name = "Annex"


########################################################################
class Result_InternalCall(models.Model):
    joint_call = models.ForeignKey('calls.InternalCall', related_name='results', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=2 ** 10)
    results = models.FileField('result', upload_to=upload_to_internal_call, blank=True, null=True)

    class Meta:
        verbose_name = "Result"


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
