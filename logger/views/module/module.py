from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from logger.models.ModuleModel import ModuleModel

def ls_mod(request):
    sys_id = request.GET['sys_id']
    mod = ModuleModel.objects(sys_id=sys_id)
    t = get_template('module/index.html')
    html = t.render(Context({'mod':mod}))
    return HttpResponse(html)

#TODO:
def add_mod(request):
    sys_id = request.POST.get('sys_id')
    name = request.POST.get('name')
    if sys_id is None or name is None:
        return HttpResponse(ret)
    mod = ModuleModel()
    mod.sys_id = sys_id
    mod.name = name
    mod.save()
    if mod.id:
        msg = 'succ'
    return HttpResponse(msg)

#TODO:
def rm_mod(request):
    return HttpResponse('a')

#TODO:
def up_mod(request):
    mod_id = '50c1994c14908d14c1069699'
    mod = ModuleModel(id=mod_id)
    mod.name = 'test'
    mod.save()
    return HttpResponse('a')
