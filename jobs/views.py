from django.shortcuts import render, get_object_or_404
from .models import Jobs


def home(request):
    jobs = Jobs.objects.all()

    return render(request, 'jobs/home.html', {'jobs': jobs})


def details(request, pk):

    data = get_object_or_404(Jobs, pk=pk)

    return render(request,'jobs/details.html', {'job': data})

