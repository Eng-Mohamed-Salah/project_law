from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .models import Blog, CustomersFeedBacks, Images, TeamMembers
# Create your views here.


def home(request):
    recent_posts = Blog.objects.all().order_by('-id')[:3]
    slider_images = Images.objects.all()
    context = {'title':'الرئيسية','recent_posts':recent_posts,'slider_images':slider_images}
    return render(request,'core/home.html',context = context)


def about(request):
    feedbacks = CustomersFeedBacks.objects.all()
    context = {'title':'من نحن','feedbacks':feedbacks}
    return render(request,'core/about.html',context = context)


def services(request):
    context = {'title':'الرئيسية'}
    return render(request,'core/services.html',context = context)


def blog(request):
    posts = Blog.objects.all()
    context = {'title':'الرئيسية','posts':posts}
    return render(request,'core/blog.html',context = context)


def team(request):
    team = TeamMembers.objects.all()
    context = {'title':'الرئيسية','team':team}
    return render(request,'core/team.html',context = context)


def contact(request):
    context = {'title':'الرئيسية'}
    return render(request,'core/contact.html',context = context)


def contact_form(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('subject'):
            subject = request.POST.get('subject')
            message = f'{request.POST.get("name")}\n{request.POST.get("email")}\n{request.POST.get("message")}'

        else:
            subject = f'رسالة من {request.POST.get("name")}'
            message = f'{request.POST.get("name")}\n{request.POST.get("service")}\n{request.POST.get("email")}\n{request.POST.get("message")}'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['Afg.economics7@gmail.com'],
            fail_silently=False,
        )
        return redirect('home')
    else:
        return redirect(request.path_info)