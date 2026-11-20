from django.db import models
class Donation(models.Model):
    CATEGORIES = [('Cooked Meals','Cooked Meals'),('Fruits & Vegetables','Fruits & Vegetables'),('Packaged Food','Packaged Food'),('Bakery','Bakery'),('Other','Other')]
    STATUSES = [('Available','Available'),('Claimed','Claimed'),('Collected','Collected')]
    donor_name = models.CharField(max_length=100)
    food_name = models.CharField(max_length=140)
    category = models.CharField(max_length=30, choices=CATEGORIES)
    quantity = models.CharField(max_length=80)
    pickup_location = models.CharField(max_length=180)
    contact = models.CharField(max_length=40)
    best_before = models.DateTimeField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=12, choices=STATUSES, default='Available')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['best_before', '-created_at']
    def __str__(self):
        return f'{self.food_name} – {self.quantity}'
