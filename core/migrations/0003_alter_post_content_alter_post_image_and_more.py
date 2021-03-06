# Generated by Django 4.0.4 on 2022-06-09 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='media', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200, verbose_name='Subtítulo'),
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('subtitle', models.CharField(blank=True, max_length=200, verbose_name='Subtítulo')),
                ('video', models.CharField(blank=True, max_length=200, verbose_name='Video')),
                ('content', models.TextField(blank=True, verbose_name='Contenido')),
                ('image', models.ImageField(blank=True, upload_to='media', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'clase',
                'verbose_name_plural': 'clases',
                'ordering': ['-created'],
            },
        ),
    ]
