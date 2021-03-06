# Generated by Django 3.1 on 2021-02-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('images', models.FileField(upload_to='images')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='images',
            field=models.FileField(default=1, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accueil',
            name='contact',
            field=models.CharField(max_length=155),
        ),
        migrations.AlterField(
            model_name='accueil',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='accueil',
            name='titre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='article',
            name='categorie',
            field=models.ManyToManyField(to='blog.Categorie'),
        ),
        migrations.AlterField(
            model_name='auteur',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='images',
            field=models.FileField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='images',
            field=models.FileField(upload_to='images'),
        ),
    ]
