# vocab_app/models.py

from django.db import models

class Vocabulary(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField()
    part_of_speech = models.CharField(max_length=50)
    example_sentence = models.TextField(blank=True)  # ← Make sure this is here and spelled correctly

    def __str__(self):
        return self.word
