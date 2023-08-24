from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

class CardModel(models.Model):

    CONDITION_CHOICES = (
        (4, 'Excellent'),
        (3, 'Good'),
        (2, 'Fair'),
        (1, 'Poor'),
    )

    card_name = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    condition = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)], choices=CONDITION_CHOICES)
    category = models.TextField(blank=True)
    description = models.TextField(blank=True)
    price = models.TextField(blank=True)
    year_set = models.TextField(blank=True)
    card_num = models.TextField(blank = True)
    promotional = models.BooleanField()


    def __str__(self):
        return self.card_name
    
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         SAVE TO MARKETPLACE DATABASE

    #     super().save(*args, **kwargs)

