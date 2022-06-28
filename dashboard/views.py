from django.shortcuts import render

# Create your views here.

# dashboard
def dashboard(request):
    return render(request, 'dashboard/index.html')