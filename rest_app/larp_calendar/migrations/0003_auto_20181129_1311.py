# Generated by Django 2.1.3 on 2018-11-29 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('larp_calendar', '0002_auto_20181129_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='larp',
            name='image',
            field=models.ImageField(null=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='larp',
            name='website',
            field=models.URLField(null=True),
        ),
    ]
