# Generated by Django 4.2 on 2023-11-02 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_customers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='job',
            field=models.CharField(default=1, max_length=200, verbose_name='الوظيفة'),
            preserve_default=False,
        ),
    ]
