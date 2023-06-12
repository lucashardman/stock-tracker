from infrastructure.repositories.meilisearch import Meilisearch
from infrastructure.operations import fetch_stock_price
from django.shortcuts import render, redirect
import uuid
from datetime import datetime

def index(request):
    data = Meilisearch().search('admin')
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
        data = {
            'max_val': form_data.get('max_val',[])[0], 
            'min_val': form_data.get('min_val',[])[0], 
            'timmer': form_data.get('timmer',[])[0], 
            'track_time': form_data.get('track_time',[])[0], 
            'name': form_data.get('name',[])[0], 
            'price': form_data.get('price',[])[0],
            'id': str(uuid.uuid4()),
            'user': 'admin',
            'created_at_dt': datetime.now().isoformat()
        }

        Meilisearch().write(data)
        return redirect('/')
    return render(request, 'tracker/index.html')