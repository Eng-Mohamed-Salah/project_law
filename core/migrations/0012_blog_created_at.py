# Generated by Django 4.2 on 2023-11-02 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_teammembers'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateField(auto_now=True, verbose_name='تاريخ النشر'),
        ),
    ]
