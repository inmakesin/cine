# Generated by Django 4.2.4 on 2023-08-23 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dffd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
