from django.shortcuts import render

# Create your views here.
def guide(request):
    return render(request, 'guide/guide.html')