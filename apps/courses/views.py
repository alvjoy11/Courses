from django.shortcuts import render, redirect, HttpResponse
from .models import Course


def index(request):
	course = Course.objects.all()
	print course
	context = {
				"courses": course,
	}
	return render(request, 'courses/index.html', context)

def create(request):
	Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	return redirect ('/')


def deleting(request, id):
	Course.objects.filter(id=id).delete()
	return redirect ('/')

def delete(request, id):
	get_course = Course.objects.get(id=id)
	context = {
				"course": get_course,
	}
	return render(request, 'courses/show.html', context)