from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def userprofile(request):
    return render(request, 'userprofile/profile.html')