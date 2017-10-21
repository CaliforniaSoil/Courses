from django.shortcuts import render, HttpResponse, redirect
from .models import Course

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses1/index.html', context)

def process(request):
    Course.objects.create(
        name = request.POST['name'],
        description = request.POST['description'],
    )
    return redirect('/')

def remove(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'courses1/remove.html', context)

def destroy(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')