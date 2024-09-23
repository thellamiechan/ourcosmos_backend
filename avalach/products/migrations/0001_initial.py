# Generated by Django 4.2.3 on 2024-09-20 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Author', models.CharField(max_length=200)),
                ('Synopsis', models.TextField()),
                ('Image', models.ImageField(upload_to='')),
                ('Tags', models.CharField(max_length=250)),
                ('Price', models.FloatField()),
            ],
        ),
    ]
