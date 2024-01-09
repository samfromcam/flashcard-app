from django.db import models


class FlashcardsBlock(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} (pk={self.pk})"

    @property
    def flashcards(self):
        return self.flashcard_set.order_by("order_id")


class Flashcard(models.Model):
    question_text = models.CharField(max_length=300)
    question_caption = models.CharField(max_length=100, blank=True, null=True)
    question_image = models.URLField(blank=True, null=True)

    answer_text = models.CharField(max_length=300)
    answer_caption = models.CharField(max_length=100, blank=True, null=True)
    answer_image = models.URLField(blank=True, null=True)

    flashcards_block = models.ForeignKey(
        FlashcardsBlock, related_name="flashcards", on_delete=models.CASCADE
    )

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question: {self.question_text}, Answer: {self.answer_text}, Block: {self.flashcards_block.title} (pk={self.pk})"

    class Meta:
        ordering = ["date_created"]
