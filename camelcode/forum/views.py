from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'forum/index.html')

def forumPage(request, post_id):
    return render(request, 'forum/forumPage.html')