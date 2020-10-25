# Generated by Django 3.0.5 on 2020-10-25 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vttapp', '0022_auto_20201026_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='alpha_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testresult',
            name='beta_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testresult',
            name='bit_depth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testresult',
            name='compression_factor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testresult',
            name='hauffman_coding',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='testresult',
            name='image_one',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='testresult',
            name='image_one_format',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='testresult',
            name='image_quid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='testresult',
            name='image_two',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='testresult',
            name='image_two_format',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='testresult',
            name='modality',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='testresult',
            name='original_image',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='testresult',
            name='quality_factor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testresult',
            name='quantizer_bit_depth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testresult',
            name='selected_image',
            field=models.CharField(default='', max_length=50),
        ),
    ]