# Generated by Django 4.0.6 on 2022-07-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='ImgURL',
            field=models.URLField(max_length=1000),
        ),
    ]