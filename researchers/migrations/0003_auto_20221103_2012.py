# Generated by Django 3.2.15 on 2022-11-03 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchers', '0002_professor_cvlac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='departament',
            field=models.CharField(choices=[('departament_0001', 'Departamento de administración'), ('departament_0002', 'Departamento de ciencias humanas'), ('departament_0003', 'Departamento de física y química'), ('departament_0004', 'Departamento de informática y computación'), ('departament_0005', 'Departamento de ingeniería civil'), ('departament_0006', 'Departamento de ingeniería eléctrica, electrónica y computación'), ('departament_0007', 'Departamento de ingeniería industrial'), ('departament_0008', 'Departamento de ingeniería química'), ('departament_0009', 'Departamento de matemáticas'), ('departament_0010', 'Escuela de arquitectura y urbanismo')], max_length=116, verbose_name='Departament'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='faculty',
            field=models.CharField(choices=[('faculty_0001', 'Facultad de administración'), ('faculty_0002', 'Facultad de ciencias exactas y naturales'), ('faculty_0003', 'Facultad de ingeniería y arquitectura')], max_length=112, verbose_name='Faculty'),
        ),
    ]
