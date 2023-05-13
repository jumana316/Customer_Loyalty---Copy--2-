from django.db import models
from Customer.models import User
from django.utils import timezone


# Create your models here.
class SaleAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sale = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    add_date = models.DateTimeField(auto_now_add=False,null=True)

    class Meta:
        verbose_name_plural = "Add Sales"

    def __str__(self):
        return f"{self.user} - {self.sale}"

    
class TrxnAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    transactions = models.IntegerField(null=True)
    

    def __str__(self):
        return str(self.transactions)


    class Meta:
        verbose_name_plural = "Add Transaction"

class ProfitAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    profit = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    class Meta:
        verbose_name_plural = "Profit Analysis"

    def __str__(self):
        return f"{self.user} - {self.profit}"

    
    
    # @property
    # def total_profit(self):
    #     return self.total_sales - self.transactions



        # return f"Transaction: {self.transaction_date} ({self.amount})"