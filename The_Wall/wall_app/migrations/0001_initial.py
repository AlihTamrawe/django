# Generated by Django 2.2.4 on 2022-10-03 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=255)),
                ('created_at', models.DateField(auto_now=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('poster', models.ForeignKey(on_delete='cascade', related_name='messager', to='login_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=255)),
                ('created_at', models.DateField(auto_now=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('commander', models.ForeignKey(on_delete='cascade', related_name='commander', to='login_app.User')),
                ('reply', models.ForeignKey(on_delete='cascade', related_name='reply', to='wall_app.Messages')),
            ],
        ),
    ]
