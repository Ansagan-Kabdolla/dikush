# Generated by Django 2.2.4 on 2020-04-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0003_auto_20200410_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='filepdf',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='Описание'),
        ),
    ]