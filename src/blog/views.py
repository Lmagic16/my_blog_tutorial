from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def hello(request):
    return HttpResponse('<html>hello world</html>')
def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.</body></html>' % now
    return HttpResponse(html)

    
    
