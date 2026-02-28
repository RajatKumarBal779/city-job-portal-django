from django.contrib import admin
from testapp.models import Jobs
# Register your models here.
class JobsAdmin(admin.ModelAdmin):
    list_display=['id','date','company','title','eligibility','salary','address','email','phonenumber','city']
admin.site.register(Jobs,JobsAdmin)