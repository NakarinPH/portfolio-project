from django.shortcuts import render


# Create your views here.
def nakarin(request):
    return render(request, 'jobs/nakarin.html')


def home(request):
    # path: http://127.0.0.1:8000/
    return render(request, 'jobs/home.html')

