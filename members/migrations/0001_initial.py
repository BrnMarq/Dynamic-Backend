# Generated by Django 3.1.5 on 2021-02-01 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.CharField(max_length=200, verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='media/members', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'miembro',
                'verbose_name_plural': 'miembros',
                'ordering': ['name'],
            },
        ),
    ]
