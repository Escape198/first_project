# Generated by Django 4.0.4 on 2022-04-19 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_member_description_alter_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='description',
            field=models.TextField(default='Upon professional alone capital camera mind soon. Across score fact check.\nWe before a music past almost. Number however water letter property process summer. Congress green store perhaps.', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(default='+646.056.6733', max_length=20, verbose_name='Phone'),
        ),
    ]
