# Generated by Django 4.0 on 2021-12-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialgreenprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialgreenprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]