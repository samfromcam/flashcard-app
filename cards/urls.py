# cards/urls.py

from django.urls import path
from django.views.generic import TemplateView
from .views import (
    CardListView,
    FlashcardsBlockCreateView,
    FlashcardCreateView,
    FlashcardUpdateView,
    FlashcardBlockDetailView,
)

urlpatterns = [
    path("", TemplateView.as_view(template_name="cards/base.html"), name="home"),
    path(
        "flashcardsblock/create/",
        FlashcardsBlockCreateView.as_view(),
        name="flashcardsblock-create",
    ),
    path(
        "flashcards/create/<int:flashcards_block_id>/",
        FlashcardCreateView.as_view(),
        name="flashcard-create",
    ),
    path(
        "cards/card_list/<int:flashcards_block_id>/",
        CardListView.as_view(),
        name="show-cards",
    ),
    path(
        "flashcards/edit/<int:pk>",
        FlashcardUpdateView.as_view(),
        name="card-update",
    ),
    path(
        "flashcardsblock/detail/<int:pk>/",
        FlashcardBlockDetailView.as_view(),
        name="flashcard-block-detail",
    ),
]
