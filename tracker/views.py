from infrastructure.repositories.meilisearch import Meilisearch
from infrastructure.operations import fetch_stock_price
from django.shortcuts import render, redirect
import uuid
from datetime import datetime
from django.http import HttpResponse

def index(request):
    data = Meilisearch().search('admin')
    updated_data = []

    error = request.GET.get('error', '')

    for dt in data:
        stock_data = fetch_stock_price(dt.get('name'))
        temp = dt
        temp['price'] = stock_data.get('price')
        updated_data.append(temp)
    return render(request, 'tracker/index.html', {
            'data': updated_data,
            'error': error
        })

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
        meili = Meilisearch()
        user = 'admin'
        user_data = meili.search(user)
        name = form_data.get('name',[])[0]

        for dt in user_data:
            if dt.get('name') == name:
                print('Already exists')
                return redirect('/?error=conflict')

        data = {
            'max_val': form_data.get('max_val',[])[0], 
            'min_val': form_data.get('min_val',[])[0], 
            'timmer': form_data.get('timmer',[])[0], 
            'track_time': form_data.get('track_time',[])[0], 
            'name': name.upper(), 
            'price': form_data.get('price',[])[0],
            'id': str(uuid.uuid4()),
            'user': user,
            'created_at_dt': datetime.now().isoformat(),
            'last_check_at_dt': datetime.now().isoformat()
        }

        meili.write(data)
        return redirect('/')
    return render(request, 'tracker/index.html')


def deletestock(request):
    if request.method == 'POST':
        stock_id = request.POST.get('id')
        Meilisearch().remove(stock_id)
    return redirect('/')