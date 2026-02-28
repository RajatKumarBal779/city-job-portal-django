from django.shortcuts import render
from testapp.models import Jobs
# Create your views here.
def home_page_view(request):
    return render(request,template_name='testapp/index.html')


def jobs_view(request,city):
    jobs_list=Jobs.objects.filter(city__iexact=city)
    my_dict={'jobs_list':jobs_list,'city':city}
    return render(request,template_name='testapp/jobs.html',context=my_dict)


