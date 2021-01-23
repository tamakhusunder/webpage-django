from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Facedb

# Create your views here.
def indexs(request):
	return HttpResponse("hello world")

def index(request):
	facedbs=Facedb.objects
	return render(request,'faceapp/index.html',{'facedbs':facedbs})

def detail(request,facedb_id):
	# print(facedb_id)
	facedb_obj=get_object_or_404(Facedb,pk=facedb_id)
	return render(request,'faceapp/detail.html', {'facedb':facedb_obj})

def train(request):
	return render(request,'faceapp/train.html')

def recog(request):
	return render(request,'faceapp/recognize.html')

def thanks(request):
	return render(request,'faceapp/right.html')