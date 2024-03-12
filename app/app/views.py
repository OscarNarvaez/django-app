from django.http import HttpResponse

def index(request):
    return HttpResponse(request, "<h1>HOLA skjdhksjdhkjshdk</h1>")
