# Generated by Django 2.2.1 on 2019-06-10 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_dataschema'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataschema',
            old_name='fa_name',
            new_name='f_name',
        ),
    ]