from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

# Create your views here.

def index0(request):
    return HttpResponse('<em> Italic html <em>')



def index1(request):

    res_dic={'result':'this is a test!!!'}
    return render(request,template_name='first_app/index.html',context=res_dic)

def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
     
    date_dict={'access_records':webpages_list}

    return render(request,template_name='first_app/index1.html',context=date_dict)

    
 