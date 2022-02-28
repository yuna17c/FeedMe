# Generated by Django 3.2.6 on 2022-02-28 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_recipelist_prep_min'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeGenerator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('prep_time', models.TextField(blank=True, null=True)),
                ('prep_min', models.IntegerField(blank=True, default=0, null=True)),
                ('ingredients', models.TextField(blank=True, null=True)),
                ('img_link', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='recipelist',
            name='prep_min',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
