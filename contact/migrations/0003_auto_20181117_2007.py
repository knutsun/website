# Generated by Django 2.1.3 on 2018-11-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
