# Generated by Django 3.2.18 on 2023-02-17 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
