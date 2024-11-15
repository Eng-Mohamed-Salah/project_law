# Generated by Django 4.2 on 2023-11-02 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_images_options_alter_images_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='الاسم')),
                ('image', models.ImageField(upload_to='images/', verbose_name='الصورة')),
                ('description', models.TextField(blank=True, null=True, verbose_name='الرأي')),
            ],
            options={
                'verbose_name': 'آراء العميل',
                'verbose_name_plural': 'آراء العملاء',
            },
        ),
    ]
