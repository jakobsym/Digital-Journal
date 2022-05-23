from django.shortcuts import render
from .models import Topic


def index(request):
    """ The homepage for learning_logs """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ Show all topics """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ Show single topic and all entries """
    topic = Topic.objects.get(id=topic_id) #queries, as this querys database. applies to line of code below too
    entries = topic.entry_set.order_by('-date_added') #sorts in reverse order
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
    
