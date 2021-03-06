# Generated by Django 3.2.6 on 2022-06-15 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreC', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['nombreC'],
            },
        ),
        migrations.CreateModel(
            name='Coche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modeloC', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['modeloC'],
            },
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duracion', models.IntegerField(default=0)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alquileres', to='aplicacion.cliente')),
                ('coche', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alquileres', to='aplicacion.coche')),
            ],
            options={
                'ordering': ['coche', 'cliente'],
            },
        ),
    ]
