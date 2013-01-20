from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from logger.models.SystemModel import SystemModel

def ls_sys(request):
    sys = SystemModel.objects
    t = get_template('system/index.html')
    html = t.render(Context({'sys':sys}))
    return HttpResponse(html)

def add_sys(request):
    sys_name = request.POST.get('name')
    if sys_name is None:
        return HttpResponse()
    entry = SystemModel()
    entry.name = sys_name
    entry.desc = request.POST.get('desc')
    entry.save()
    if entry.id:
        msg = 'succ'
    return HttpResponse(msg)

#TODO:
def rm_sys(request):
    return HttpResponse()

#TODO:
def up_sys(request):
    return HttpResponse()

