# Generated by Django 3.0.5 on 2020-10-04 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vttapp', '0010_auto_20201004_2357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ct',
            old_name='fake_image',
            new_name='jpeg_image',
        ),
        migrations.RenameField(
            model_name='ct',
            old_name='real_image',
            new_name='our_image',
        ),
        migrations.RenameField(
            model_name='mr',
            old_name='fake_image',
            new_name='jpeg_image',
        ),
        migrations.RenameField(
            model_name='mr',
            old_name='real_image',
            new_name='our_image',
        ),
        migrations.RenameField(
            model_name='xr',
            old_name='fake_image',
            new_name='jpeg_image',
        ),
        migrations.RenameField(
            model_name='xr',
            old_name='real_image',
            new_name='our_image',
        ),
    ]