# Generated by Django 5.1 on 2024-08-16 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='anio',
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha',
            field=models.DateField(default=2341, verbose_name='Fecha de lanzamiento'),
            preserve_default=False,
        ),
    ]
