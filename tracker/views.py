from infrastructure.operations import fetch_stock_price, write_dict_to_meilisearch, get_meilisearch
from django.shortcuts import render
import uuid

def index(request):
    data = get_meilisearch('admin')
    return render(request, 'tracker/index.html', {'data': data})

def search(request):
    if request.method == 'POST':
        form_data = request.POST
        stock = request.session.get('stock', '')
        element_name = form_data.get('element_name')
        
        stock_data = fetch_stock_price(element_name)
        request.session['stock'] = stock
        return render(request, 'tracker/index.html', {'stock': stock_data})
    else:
        request.session['stock'] = ''
        return render(request, 'tracker/index.html')
    

def persist(request):
    if request.method == 'POST':
        form_data = dict(request.POST)
        # form_data.pop('csrfmiddlewaretoken', None)
        data = {
            'max_val': form_data.get('max_val',[])[0], 
            'min_val': form_data.get('min_val',[])[0], 
            'timmer': form_data.get('timmer',[])[0], 
            'name': form_data.get('name',[])[0], 
            'price': form_data.get('price',[])[0],
            'id': str(uuid.uuid4()),
            'user': 'admin'
        }

        write_dict_to_meilisearch(data)
        # print(form_data)
        # element_name = form_data.get('element_name')
        
        # stock_data = fetch_stock_price(element_name)
        # request.session['stock'] = stock
    return render(request, 'tracker/index.html')