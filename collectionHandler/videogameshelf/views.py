from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import editor

def index(request):
    return HttpResponse ("Hi, welcome to your video game shelf !")
def editor(request):
    editorList = Editor.objects.order_by(creationDate)
    context = {'editorList' : editorList}
    return render(request,'videogameshelf/editor.html',context)
