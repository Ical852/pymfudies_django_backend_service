from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.IntegerField()
    size = models.CharField(max_length=50)
    img = models.TextField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    order_id = models.CharField(max_length=255)
    total = models.IntegerField()
    payment_url = models.TextField()

    def __str__(self):
        return self.order_id

class TransactionDetail(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)
    size = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.transaction
    
class Notification(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.name