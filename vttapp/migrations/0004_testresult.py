# Generated by Django 3.0.3 on 2020-03-10 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vttapp', '0003_auto_20200310_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testresult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('dataset', models.CharField(default='', max_length=50)),
                ('selcted_image', models.CharField(default='', max_length=50)),
                ('confidence', models.IntegerField(default=0)),
            ],
        ),
    ]