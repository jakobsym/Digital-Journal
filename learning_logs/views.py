from pickletools import OpcodeInfo
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .models import Topic, Entry
from .forms import TopicForm, EntryForm  #'TopicForm' is a class from 'forms.py'



def index(request):
    """ The homepage for learning_logs """
    return render(request, 'learning_logs/index.html')
@login_required
def topics(request):
    """ Show all topics """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """ Show single topic and all entries """
    topic = Topic.objects.get(id=topic_id) #queries, as this querys database. applies to line of code below too
    entries = topic.entry_set.order_by('-date_added') #sorts in reverse order
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required    
def new_topic(request):
    """ Add new topic for user """
    if request.method != 'POST':
        # meaning no data submitted; send blank page
        form  = TopicForm()
    else:
        # POST data submitted; process this data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics') # redirect will redirect user back to Topics page after submitting topic
    # display blank/invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """ allow for new entry of a topic """
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data
        form = EntryForm()
    else:
        # Process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """ Edit exisiting entry """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic:': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
 

