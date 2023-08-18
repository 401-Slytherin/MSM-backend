from django.db import models

class CardModel(models.Model):
    card_name = models.TextField()
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    condition = models.CharField(max_length = 1, choices=CONDITION_CHOICES)
    category = models.TextField(blank=True)
    description = models.TextField(blank=True)
    price = models.TextField(blank=True)
    year_set = models.TextField(blank=True)
    promotional = models.BooleanField()


    CONDITION_CHOICES = (
        ('4', 'Excellent'),
        ('3', 'Good'),
        ('2', 'Fair'),
        ('1', 'Poor'),
    )

