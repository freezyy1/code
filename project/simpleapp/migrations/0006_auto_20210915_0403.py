# Generated by Django 3.1.6 on 2021-09-15 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0005_auto_20210913_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
