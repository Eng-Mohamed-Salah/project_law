from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .models import *


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = 'إدارة الجهيني للمحاماة'


@admin.register(CustomersFeedBacks)
class CustomersFeedBacksAdmin(admin.ModelAdmin):
    list_display = ("name", "job", "display_image")
    search_fields = ['name']
    def display_image(self, obj):
          return format_html('<a href="{}" target="_blank"><img src="{}" width="50" height="50" /></a>', obj.image.url, obj.image.url)
    display_image.allow_tags = True
    display_image.short_description = 'الصورة'


@admin.register(TeamMembers)
class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ("name", "title", 'facebook','youtube','twitter',"display_image")
    search_fields = ['name']
    def display_image(self, obj):
          return format_html('<a href="{}" target="_blank"><img src="{}" width="50" height="50" /></a>', obj.image.url, obj.image.url)
    display_image.allow_tags = True
    display_image.short_description = 'الصورة'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "display_link")
    search_fields = ['title']
    def display_link(self, obj):
          return format_html('<a href="{}" target="_blank">{}</a>', obj.link, obj.link)
    display_link.allow_tags = True
    display_link.short_description = 'الرابط'



@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ("id", "display_image")
    search_fields = ['id']
    def display_image(self, obj):
          return format_html('<a href="{}" target="_blank"><img src="{}" width="50" height="50" /></a>', obj.image.url, obj.image.url)
    display_image.allow_tags = True
    display_image.short_description = 'الصورة'
