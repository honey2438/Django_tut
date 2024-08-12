from django.db import models

class Item(models.Model):
    def __str__(self):
        return self.item_name+" "+self.item_desc+" "+str(self.item_price)
    item_name=models.CharField(max_length=100)
    item_desc=models.CharField(max_length=100)
    item_price=models.IntegerField()
    
