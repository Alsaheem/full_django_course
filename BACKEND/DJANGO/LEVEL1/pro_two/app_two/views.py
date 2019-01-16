from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict2 = {'insert_me_now':"this is what is being inserted into my page gotcha!!!"}
    return render(request,'app_two/help.html',context=my_dict2)
