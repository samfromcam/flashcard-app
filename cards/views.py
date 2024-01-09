from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse
from .models import FlashcardsBlock, Flashcard
from .forms import FlashcardsBlockForm, FlashcardForm
from django.shortcuts import get_object_or_404


# Create the flashcardblock (flashcard desk)
class FlashcardsBlockCreateView(CreateView):
    model = FlashcardsBlock
    form_class = FlashcardsBlockForm
    template_name = "cards/flashcardsblock_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse(
            "flashcard-create", kwargs={"flashcards_block_id": self.object.id}
        )


# Create individual flashcard within a flashcardblock
class FlashcardCreateView(CreateView):
    model = Flashcard
    form_class = FlashcardForm
    template_name = "cards/card_form.html"
    success_url = reverse_lazy("show-cards")

    def get_success_url(self):
        return reverse(
            "show-cards",
            kwargs={"flashcards_block_id": self.object.flashcards_block_id},
        )

    def form_valid(self, form):
        flashcards_block_id = self.kwargs.get("flashcards_block_id")
        form.instance.flashcards_block_id = flashcards_block_id
        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle invalid form submission, e.g., log errors or display a message
        return super().form_invalid(form)


# Show the flashcard desk
class FlashcardListView(ListView):
    model = Flashcard
    template_name = "cards/card_list.html"

    def get_queryset(self):
        flashcards_block_id = self.kwargs.get("flashcards_block_id")
        flashcards_block = get_object_or_404(FlashcardsBlock, id=flashcards_block_id)
        return Flashcard.objects.filter(flashcards_block=flashcards_block)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flashcards_block_id = self.kwargs.get("flashcards_block_id")
        flashcards_block = get_object_or_404(FlashcardsBlock, id=flashcards_block_id)
        context["flashcards_block"] = flashcards_block
        context[
            "flashcards"
        ] = flashcards_block.flashcards.all()  # Use .all() to get the list
        return context


# Update the existing flashcards
class FlashcardUpdateView(UpdateView):
    model = Flashcard
    form_class = FlashcardForm
    template_name = "cards/card_form.html"

    def get_success_url(self):
        return reverse(
            "show-cards",
            kwargs={"flashcards_block_id": self.object.flashcards_block_id},
        )

    def form_valid(self, form):
        flashcards_block_id = self.object.flashcards_block_id
        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle invalid form submission, e.g., log errors or display a message
        return super().form_invalid(form)


# View the flashcards detail and update them
class FlashcardBlockDetailView(DetailView):
    model = FlashcardsBlock
    template_name = "cards/flashcard_block_detail.html"
    context_object_name = "flashcards_block"

    # Optionally, you can override the get_context_data method to include flashcards
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flashcards"] = self.object.flashcards.all()
        return context
