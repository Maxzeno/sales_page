from django.shortcuts import render
from .models import Course, Script

# Create your views here.

def index(request):
	courses = Course.objects.order_by('priority')
	scripts = Script.objects.all()
	return render(request, 'main/index.html', {'courses': courses, 'scripts': scripts})
	