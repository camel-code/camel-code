from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'account/index.html')

def accountPage(request, account_id):
    return render(request, 'account/accountPage.html')