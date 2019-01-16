from django.shortcuts import render
from second_app.models import AccessRecord,user

# Create your views here.
def index(request):
    my_dict = {"insertion":"my name is alsaheem"}
    return render(request,'second_app/index.html',context=my_dict)

def users(request):
    users_list = user.objects.order_by('first_name')
    users_dict = {'users_record':users_list}
    return render(request,'second_app/users.html',context=users_dict)
