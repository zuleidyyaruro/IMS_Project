# Generated by Django 3.1.3 on 2020-11-23 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('semillero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=255)),
                ('correo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('rol', models.CharField(choices=[('Estudiante', 'Estudiante'), ('Docente', 'Docente')], default='Docente', max_length=20)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='integrantes/%Y/%m/%d')),
                ('semillero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semillero.semillero')),
            ],
            options={
                'verbose_name': 'Integrantes',
                'verbose_name_plural': 'Integrantes',
                'ordering': ['id'],
            },
        ),
    ]
