# Generated by Django 3.0.3 on 2020-03-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vttapp', '0002_auto_20200305_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ct',
            name='q_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mr',
            name='q_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='xr',
            name='q_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]