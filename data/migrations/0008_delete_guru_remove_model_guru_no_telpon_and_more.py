# Generated by Django 4.1.5 on 2023-07-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_rename_email_model_pengurus_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Guru',
        ),
        migrations.RemoveField(
            model_name='model_guru',
            name='no_telpon',
        ),
        migrations.RemoveField(
            model_name='model_guru',
            name='password',
        ),
        migrations.RemoveField(
            model_name='model_guru',
            name='username',
        ),
        migrations.AddField(
            model_name='model_guru',
            name='alamat',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='model_guru',
            name='bidang_studi_yang_diampu',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='model_guru',
            name='nip',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='model_guru',
            name='nomer_hp',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='model_guru',
            name='tempat_tgl_lahir',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='model_guru',
            name='nama_guru',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='model_guru',
            name='staff',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
