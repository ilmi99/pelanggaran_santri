# Generated by Django 4.2.1 on 2023-06-04 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_alter_guru_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='model_kamar',
            options={'verbose_name_plural': 'Model_kamar'},
        ),
        migrations.AlterModelOptions(
            name='model_pelanggaran2',
            options={'verbose_name_plural': 'Model_pelanggaran'},
        ),
        migrations.AlterModelOptions(
            name='model_pendidikan',
            options={'verbose_name_plural': 'Model_pendidikan'},
        ),
        migrations.AlterModelOptions(
            name='model_pengurus',
            options={'verbose_name_plural': 'Model_pengurus'},
        ),
        migrations.AlterModelOptions(
            name='model_santri2',
            options={'verbose_name_plural': 'Model_santri'},
        ),
    ]