from django.template import Context, loader
from django.http import HttpResponse

def home(request):
    t = loader.get_template("index.html")
	metaUserKey = "LOGON_USER" if "LOGON_USER" in request.META.iterkeys() else "USERNAME"
    c = Context({
                 "username" : "user: {0}".format(metaUserKey)
                 })
    return HttpResponse(t.render(c)) 