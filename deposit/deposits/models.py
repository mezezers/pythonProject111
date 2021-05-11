from django.db import models

class Deposit(models.Model):

    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.DecimalField(max_digits=5, decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    #interest = models.DecimalField(max_digits=10, decimal_places=2)



    def _get_interest(self):

        return self.deposit * (1 + self.rate*self.term)



    interest = property(_get_interest)

