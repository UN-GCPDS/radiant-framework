# Generated by Django 4.1 on 2022-08-29 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0003_researchgroup_researchers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="researchgroup",
            name="founded",
            field=models.DateField(
                default="django.utils.timezone.now", verbose_name="Founded"
            ),
        ),
    ]
