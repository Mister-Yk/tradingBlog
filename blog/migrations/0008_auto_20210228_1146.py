# Generated by Django 3.1 on 2021-02-28 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210228_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='text',
            field=models.CharField(max_length=100),
        ),
    ]