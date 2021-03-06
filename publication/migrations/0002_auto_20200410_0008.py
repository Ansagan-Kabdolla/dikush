# Generated by Django 2.2.4 on 2020-04-09 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predmeti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('img_url', models.ImageField(upload_to='media/', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'ordering': ['date'],
            },
        ),
        migrations.AlterField(
            model_name='filepdf',
            name='serius',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='publication.Predmeti', verbose_name='Серия'),
        ),
    ]
