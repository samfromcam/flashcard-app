from django.contrib import admin
from .models import FlashcardsBlock, Flashcard


class FlashcardInline(admin.StackedInline):
    model = Flashcard
    extra = 1  # Number of empty forms to display


@admin.register(FlashcardsBlock)
class FlashcardsBlockAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    inlines = [FlashcardInline]


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = (
        "question_text",
        "answer_text",
        "flashcards_block",
        "date_created",
    )
    list_filter = (
        "flashcards_block",
        "date_created",
    )
    search_fields = (
        "question_text",
        "answer_text",
        "flashcards_block__title",
    )
    date_hierarchy = "date_created"
