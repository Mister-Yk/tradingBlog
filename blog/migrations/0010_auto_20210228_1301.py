# Generated by Django 3.1 on 2021-02-28 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210228_1236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipe',
            options={},
        ),
        migrations.CreateModel(
            name='BlogEquipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('contenue', models.TextField()),
                ('equipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.equipe')),
            ],
            options={
                'verbose_name': 'Equipe',
                'verbose_name_plural': 'Equipes',
            },
        ),
    ]
