from django.forms.models import model_to_dict
from tracker.models import Stock

class StockManager:
    def write(self, data):
        Stock.objects.create(**data)

    def search_by_user(self, field):
        return [model_to_dict(stock) for stock in Stock.objects.filter(user=field)]
    
    def all(self):
        return [model_to_dict(stock) for stock in Stock.objects.all()]

    def reset_index(self):
        Stock.objects.all().delete()

    def remove(self, id):
        Stock.objects.filter(id=id).delete()

    def update(self, document, data):
        Stock.objects.filter(id=document.get("id")).update(**data)