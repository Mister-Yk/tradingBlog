# Generated by Django 3.1 on 2021-02-28 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210228_1309'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artequipe',
            new_name='Aequipe',
        ),
        migrations.AlterModelOptions(
            name='aequipe',
            options={'verbose_name': 'Aequipe', 'verbose_name_plural': 'Aequipes'},
        ),
        migrations.RenameField(
            model_name='aequipe',
            old_name='contenue',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='aequipe',
            old_name='titre',
            new_name='title',
        ),
    ]
