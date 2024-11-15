from tabnanny import verbose
from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100,verbose_name = 'العنوان')
    description = models.TextField(verbose_name = 'الوصف',blank = True,null = True)
    link = models.URLField(max_length = 200 , verbose_name = 'لينك الفيديو') 
    background_img_link = models.URLField(max_length = 200, verbose_name = 'لينك صورة الفيديو')
    created_at = models.DateField(auto_now = True,verbose_name = 'تاريخ النشر')
    class Meta:
        verbose_name = 'المدونة'
        verbose_name_plural = "المدونات"
    def __str__(self):
        return self.title
    
class Images(models.Model):
    image = models.ImageField(upload_to = 'images/' , verbose_name = 'الصورة')
    class Meta:
        verbose_name = 'صورة المعرض'
        verbose_name_plural = "صور المعرض"
    def __str__(self):
        return str(self.id)

class CustomersFeedBacks(models.Model):
    name = models.CharField(max_length = 200 , verbose_name = 'الاسم')
    job =  models.CharField(max_length = 200 , verbose_name = 'الوظيفة')
    image = models.ImageField(upload_to = 'images/' , verbose_name = 'الصورة')
    description = models.TextField(verbose_name = 'الرأي',blank = True,null = True)
    class Meta:
        verbose_name = 'آراء العميل'
        verbose_name_plural = "آراء العملاء"
    def __str__(self):
        return self.name

class TeamMembers(models.Model):
    name = models.CharField(max_length = 200 , verbose_name = 'الاسم')
    title =  models.CharField(max_length = 200 , verbose_name = 'الوظيفة',blank = True,null = True)
    image = models.ImageField(upload_to = 'images/' , verbose_name = 'الصورة')
    description = models.TextField(verbose_name = 'الوصف',blank = True,null = True)
    facebook = models.URLField(max_length = 200 , verbose_name = 'فيس بوك',blank = True,null = True)
    youtube = models.URLField(max_length = 200 , verbose_name = 'يوتيوب',blank = True,null = True)
    twitter = models.URLField(max_length = 200 , verbose_name = 'تويتر',blank = True,null = True)
    class Meta:
        verbose_name = 'عضو الفريق'
        verbose_name_plural = "أعضاء الفريق"
    def __str__(self):
        return self.name



class Consultation(models.Model):
    name = models.CharField(max_length = 200 , verbose_name = 'الاسم')
    email = models.EmailField(max_length = 200 , verbose_name = 'البريد الالكتروني')
    phone = models.CharField(max_length = 200 , verbose_name = 'رقم الهاتف')
    description = models.TextField(verbose_name = 'الرسالة',blank = True,null = True)
    created_at = models.DateField(auto_now = True,verbose_name = 'تاريخ النشر')