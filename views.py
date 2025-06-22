from django.shortcuts import render, redirect
from .models import Vocabulary
from .forms import VocabularyForm

def home(request):
    words = Vocabulary.objects.all()
    return render(request, 'vocab_app/home.html', {'words': words})

def add_word(request):
    if request.method == 'POST':
        form = VocabularyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VocabularyForm()
    return render(request, 'vocab_app/add_word.html', {'form': form})

