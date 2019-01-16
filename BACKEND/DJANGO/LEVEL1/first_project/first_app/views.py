from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,WebPage
# Create your views here.

def index(request):

    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'accessrecord':webpages_list}

    # my_dict = { 'insert_me':'i am from the first_app/index.html'}
    return render(request,'first_app/index.html',context=date_dict)
