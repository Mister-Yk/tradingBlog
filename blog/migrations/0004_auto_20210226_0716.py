# Generated by Django 3.1 on 2021-02-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_testimonial_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='text',
            field=models.CharField(max_length=300),
        ),
    ]
