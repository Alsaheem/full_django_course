from django.contrib import admin
from second_app.models import AccessRecord,user

# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(user)
