from django.template import Context, loader
from django.http import HttpResponse

def home(request):
    t = loader.get_template("index.html")
    c = Context({
                 "username" : "user: {0}".format(request.META["USERNAME"])
                 })
    return HttpResponse(t.render(c)) 