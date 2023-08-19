from django.db import models
from django.contrib.auth import get_user_model

class CardModel(models.Model):
    card_name = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to = 'images/')
    condition = models.CharField(max_length = 1, choices=CONDITION_CHOICES)
    category = models.TextField(blank=True)
    description = models.TextField(blank=True)
    price = models.TextField(blank=True)
    year_set = models.TextField(blank=True)
    card_num = models.TextField(blank = True)
    promotional = models.BooleanField()

    CONDITION_CHOICES = (
        ('4', 'Excellent'),
        ('3', 'Good'),
        ('2', 'Fair'),
        ('1', 'Poor'),
    )

    def __str__(self):
        return self.location
    
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         SAVE TO MARKETPLACE DATABASE

    #     super().save(*args, **kwargs)
