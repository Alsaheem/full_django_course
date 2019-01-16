from django.shortcuts import render
# from second_app.models import AccessRecord,user
from second_app.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'second_app/index.html')

def users(request):

    form = NewUserForm

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('Form is Invalid')
    return render(request,'second_app/users.html',{'form':form})
