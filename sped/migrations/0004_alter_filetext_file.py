# Generated by Django 3.2.6 on 2021-11-05 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sped', '0003_alter_filetext_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filetext',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
