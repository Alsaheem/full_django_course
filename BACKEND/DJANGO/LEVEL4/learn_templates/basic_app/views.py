from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def other(request):
    mydict = {'text': 'this is a really good text' ,'number':'100-CONTACT'}
    return render(request,'basic_app/other.html',context=mydict)

def relative(request):
    return render(request,'basic_app/relative_url.html')
