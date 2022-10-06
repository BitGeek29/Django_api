from django.shortcuts import render
from .models import ApiModel
from django.http import JsonResponse
from .form import GeeksForm


# Create your views here.
def test_api(request):
    subscribers = ApiModel.objects.values('title', 'description')
    data = {
        'subscribers' : list(subscribers)
    }
    return JsonResponse(data)
  
def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
          
    context['form']= form
    return render(request, "create_view.html", context)