# Generated by Django 3.2.6 on 2021-11-05 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, max_length=400, upload_to='')),
                ('title', models.CharField(blank=True, max_length=400)),
            ],
        ),
    ]