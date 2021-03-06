# Generated by Django 3.0.7 on 2021-05-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210321_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_tr',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='doors_tr',
            field=models.CharField(default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='eksterier_tr',
            field=models.CharField(default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='electrik_tr',
            field=models.CharField(default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='floor_tr',
            field=models.CharField(default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='interier_tr',
            field=models.CharField(default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name_tr',
            field=models.CharField(default='', max_length=300, null=True),
        ),
    ]
