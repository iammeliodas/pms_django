# Generated by Django 3.0.1 on 2019-12-28 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0010_auto_20190404_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
