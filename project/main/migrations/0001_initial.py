# Generated by Django 4.0.4 on 2022-04-12 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Department')),
                ('description', models.TextField(verbose_name='Description')),
                ('url', models.URLField(verbose_name='Website')),
            ],
        ),
    ]