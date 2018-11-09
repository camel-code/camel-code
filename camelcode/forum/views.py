from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'forum/index.html', {'all_albums': 1})

def detail(request, post_id):
    return render(request, 'forum/detail.html', {'all_albums': 1})