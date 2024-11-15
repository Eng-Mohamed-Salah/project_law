# Generated by Django 4.2 on 2023-11-02 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_teammembers_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='الاسم')),
                ('email', models.EmailField(max_length=200, verbose_name='البريد الالكتروني')),
                ('phone', models.CharField(max_length=200, verbose_name='رقم الهاتف')),
                ('description', models.TextField(blank=True, null=True, verbose_name='الرسالة')),
                ('created_at', models.DateField(auto_now=True, verbose_name='تاريخ النشر')),
            ],
        ),
    ]
