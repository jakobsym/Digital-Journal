from django.shortcuts import render

def index(request):
    """ The homepage for learning_logs """
    return render(request, 'learning_logs/index.html')
# Create your views here.
