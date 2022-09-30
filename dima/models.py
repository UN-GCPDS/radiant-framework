import os
import subprocess

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


# upload_to = os.path.join(settings.MEDIA_ROOT, 'uploads', 'newsletter')
# if not os.path.exists(upload_to):
    # os.makedirs(upload_to)
upload_to_newsletter = os.path.join('uploads', 'newsletter')
upload_to_broadcast = os.path.join('uploads', 'broadcast')


# ----------------------------------------------------------------------
def run_command(command):
    """This post save function creates a thumbnail for the commentary PDF"""
    proc = subprocess.Popen(command,
                            shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            )
    return proc.communicate()[0]


########################################################################
class Newsletter(models.Model):
    """"""
    file = models.FileField('newsletter', upload_to=upload_to_newsletter)
    upload = models.DateTimeField('upload', auto_now_add=True)
    thumbnail = models.ImageField('thumbnail', upload_to=upload_to_newsletter, blank=True, null=True)

    def save(self):
        thumbnail = f"{self.file.name.removesuffix('.pdf')}.png"
        self.thumbnail = os.path.join(upload_to_newsletter, thumbnail)
        super(Newsletter, self).save()


########################################################################
class Broadcast(models.Model):
    """"""
    image = models.FileField('broadcast', upload_to=upload_to_broadcast)
    link = models.URLField('link', blank=True, null=True)
    dominant = models.CharField('dominant', max_length=7, blank=True, null=True)
    title = models.CharField('title', max_length=2**10, blank=True, null=True)
    description = models.TextField('description', max_length=2**10, blank=True, null=True)
    upload = models.DateTimeField('upload', auto_now_add=True)

    # ----------------------------------------------------------------------
    def save(self):
        """"""
        super().save()
        command = f"{settings.SCRIPTS_ROOT}/dominantcolor {self.image.path}"
        dominant = run_command(command).strip()
        self.dominant = dominant.decode()
        super().save()


# ----------------------------------------------------------------------
def generate_thumbnail(sender, instance=False, **kwargs):
    """This post save function creates a thumbnail for the commentary PDF"""
    newsletter = sender.objects.get(pk=instance.pk)
    command = f"convert -quality 95 -thumbnail 222 {newsletter.file.path}[0] {newsletter.thumbnail.path}"
    run_command(command)


post_save.connect(generate_thumbnail, sender=Newsletter)
