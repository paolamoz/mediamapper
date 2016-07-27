# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-27 05:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medioschile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('rut', models.CharField(blank=True, max_length=250, null=True, verbose_name='R.U.T.')),
                ('empresa_sociedad_propietaria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medioschile.Empresa', verbose_name='Empresa o Sociedad Propietaria')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre/Apellido')),
                ('nombres', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombres')),
                ('apellidos', models.CharField(blank=True, max_length=250, null=True, verbose_name='Apellidos')),
                ('rut', models.CharField(blank=True, max_length=250, null=True, verbose_name='R.U.T.')),
                ('email', models.EmailField(blank=True, max_length=250, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]
