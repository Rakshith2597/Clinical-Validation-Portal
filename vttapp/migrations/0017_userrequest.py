# Generated by Django 3.0.3 on 2020-10-11 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vttapp', '0016_auto_20201009_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('registeration_number', models.CharField(max_length=50)),
                ('email_id', models.CharField(max_length=50)),
            ],
        ),
    ]