# Generated by Django 2.0.1 on 2018-01-14 04:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('text', models.TextField(verbose_name='main text')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='datetime')),
            ],
        ),
    ]
