# Generated by Django 3.1 on 2021-02-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_testimonial_agence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='text',
            field=models.CharField(max_length=255),
        ),
    ]
