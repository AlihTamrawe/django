# Generated by Django 2.2.4 on 2022-09-28 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255)),
                ('network', models.TextField(max_length=255)),
                ('release_date', models.DateTimeField(auto_now=True)),
                ('desc', models.TextField(default='none')),
            ],
        ),
    ]