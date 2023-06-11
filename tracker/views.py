from infrastructure.operations import fetch_stock_price
from django.shortcuts import render

def index(request):
    return render(request, 'tracker/index.html')

def search(request):
    if request.method == 'POST':
        stock = request.session.get('stock', '')

        form_data = request.POST
        element_name = form_data.get('element_name')
        
        
        stock_data = fetch_stock_price(element_name)

        request.session['stock'] = stock

        return render(request, 'tracker/index.html', {'stock': stock_data})
    else:
        request.session['stock'] = ''

        return render(request, 'tracker/index.html')