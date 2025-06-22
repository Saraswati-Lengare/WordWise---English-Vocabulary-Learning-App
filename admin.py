# vocab_app/admin.py

from django.contrib import admin
from .models import Vocabulary

@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('word', 'part_of_speech', 'definition', 'example_sentence')
    search_fields = ('word', 'part_of_speech')
    list_filter = ('part_of_speech',)
