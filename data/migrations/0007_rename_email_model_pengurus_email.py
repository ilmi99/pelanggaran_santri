# Generated by Django 4.1.5 on 2023-07-27 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_rename_password_model_pengurus_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model_pengurus',
            old_name='Email',
            new_name='email',
        ),
    ]
