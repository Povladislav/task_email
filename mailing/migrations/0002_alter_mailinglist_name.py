# Generated by Django 4.2.2 on 2023-06-15 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]