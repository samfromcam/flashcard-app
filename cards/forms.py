# cards/forms.py

from django import forms
from .models import FlashcardsBlock, Flashcard


class FlashcardsBlockForm(forms.ModelForm):
    class Meta:
        model = FlashcardsBlock
        fields = ["title"]


class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = [
            "question_text",
            "question_image",
            "question_caption",
            "answer_text",
            "answer_image",
            "answer_caption",
        ]
