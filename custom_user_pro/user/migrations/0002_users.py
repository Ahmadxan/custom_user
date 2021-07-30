# Generated by Django 3.2.5 on 2021-07-29 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.SmallIntegerField(choices=[(1, 'admin'), (2, 'editer'), (3, 'muharrir')], default=1)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]