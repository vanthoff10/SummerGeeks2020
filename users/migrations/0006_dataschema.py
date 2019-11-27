# Generated by Django 2.2.1 on 2019-06-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_delete_dataschema'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('company_url', models.CharField(max_length=100)),
                ('company_email', models.EmailField(max_length=50)),
                ('fa_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('city_name', models.CharField(max_length=100)),
            ],
        ),
    ]