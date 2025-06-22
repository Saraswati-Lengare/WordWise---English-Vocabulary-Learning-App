# vocab_app/forms.py

from django import forms
from .models import Vocabulary

class VocabularyForm(forms.ModelForm):
    class Meta:
        model = Vocabulary
        fields = ['word', 'definition', 'part_of_speech', 'example_sentence']
