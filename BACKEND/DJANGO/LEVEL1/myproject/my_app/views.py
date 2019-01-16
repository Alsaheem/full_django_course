from django.shortcuts import render

# Create your views here.
def index(request):
    mydict={"insert_something": "this is something being inserted"}
    return render(request,'my_app/index.html',context=mydict)
