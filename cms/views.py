from django.shortcuts import render
from .models import News, Announcement

def index(request):
    news_list = News.objects.all()
    announcements = Announcement.objects.all()
    return render(request, 'cms/index.html', {'news_list': news_list, 'announcements': announcements})
