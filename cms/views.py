from django.shortcuts import render
from .models import Announcement

def test_page(request):
    # Pobranie wszystkich ogłoszeń z bazy, posortowanych malejąco po dacie
    announcements = Announcement.objects.all().order_by('-date')
    return render(request, "test_page.html", {"announcements": announcements})
