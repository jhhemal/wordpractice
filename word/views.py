from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from .forms import WordCreationForm
from .models import Word
# Create your views here.
def index(request):
    return render(request, 'word/index.html')

class WordCreateView(CreateView):
    form_class = WordCreationForm
    template_name = 'word/create.html'
    success_url = reverse_lazy('create-word')
    def form_valid(self, form):
        messages.success(self.request, "New Word has been added")
        return super().form_valid(form)

def allwords(request):
    words = Word.objects.all()
    context = {
        'words' : words
    }
    return render(request, 'word/all_words.html', context=context)

class WordUpdateView(UpdateView):
    model = Word
    form_class = WordCreationForm
    template_name = 'word/update.html'
    success_url = reverse_lazy('all-words')

    def form_valid(self, form):
        messages.warning(self.request, "Word has been updated")
        return super().form_valid(form)

class WordDetailView(DetailView):
    model = Word
    template_name = 'word/detail.html'
    context_object_name = 'word'

class WordDeleteView(DeleteView):
    model = Word
    success_url = reverse_lazy('all-words')

    def delete(self, *args, **kwargs):
        messages.error(self.request, "Word has been deleted")
        return super(WordDeleteView, self).delete(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
