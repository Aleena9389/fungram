# Generated by Django 4.1 on 2022-09-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SignUp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=100)),
            ],
        ),
    ]
