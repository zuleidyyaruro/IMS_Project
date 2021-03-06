# Generated by Django 3.1.3 on 2020-11-23 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('semillero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('autores', models.CharField(max_length=255)),
                ('fecha_inicio', models.CharField(max_length=10)),
                ('semillero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semillero.semillero')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['id'],
            },
        ),
    ]
