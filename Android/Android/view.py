import simplejson
from django.http import HttpResponse


def hello(request):
    request.encoding = 'utf-8'
    if request.method == 'GET':
        return HttpResponse("Hello world ! "+request.method)
    else:
        req = simplejson.loads(request.raw_post_data)
        return HttpResponse("Hello! ")