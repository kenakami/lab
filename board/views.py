from django.shortcuts import render
from django.views import generic

from .models import Thread, Post
# Create your views here.

def index(request):
    context = {
        'num_threads': Thread.objects.count(),
        'num_posts': Post.objects.count(),
        'num_images': 0,
    }

    return render(request, 'index.html', context=context)


class FeedView(generic.ListView):
    model = Thread
    paginate_by = 10
    template_name = 'board/feed.html'

class CatalogListView(generic.ListView):
    model = Thread
    paginate_by = 50
    template_name = 'board/catalog.html'

class ThreadDetailView(generic.DetailView):
    model = Thread

import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from board.forms import CreateThreadForm, ReplyForm

def create_thread(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CreateThreadForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            # book_instance.due_back = form.cleaned_data['renewal_date']
            # book_instance.save()

            thread = Thread(subject=form.cleaned_data['subject'], last_updated=datetime.datetime.now())
            post = Post(thread=thread, name=form.cleaned_data['name'], comment=form.cleaned_data['comment'])
            thread.id = post.id

            thread.save()
            post.save()

            # redirect to a new URL:
            return HttpResponseRedirect(thread.get_absolute_url())

    # If this is a GET (or any other method) create the default form.
    # else:
        # proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        # form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
    else: 
        form = CreateThreadForm()

    context = {
        'form': form,
    }

    return render(request, 'board/create_thread.html', context)

def reply(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            thread.last_updated=datetime.datetime.now()
            post = Post(thread=thread, name=form.cleaned_data['name'], comment=form.cleaned_data['comment'])
            
            thread.save()
            post.save()

            return HttpResponseRedirect(thread.get_absolute_url())

    else: 
        form = ReplyForm()

    context = {
        'form': form,
    }

    return render(request, 'board/reply.html', context)

