from django.shortcuts import render
from django.core.paginator import Paginator

from .utils import get_mongodb



# Create your views here.
def main(request):
    db = get_mongodb()
    quotes = db.quotes.find()
    return render(request, 'quotes/index.html',context={'quotes':quotes})
    # return render(request, 'quotes/index.html, context={}')

