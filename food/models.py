from django.db import models

class Item(models.Model):
    def __str__(self):
        return self.item_name+" "+self.item_desc+" "+str(self.item_price)
    item_name=models.CharField(max_length=100)
    item_desc=models.CharField(max_length=100)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=500,default="https://theme-assets.getbento.com/sensei/fc2db91.sensei/assets/images/catering-item-placeholder-704x520.png")
    
