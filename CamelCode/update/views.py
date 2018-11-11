from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'update/index.html')

def updatePage(request, update_id):
    return render(request, 'update/updatePage.html')