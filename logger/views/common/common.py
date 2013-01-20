from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from logger.models.LogModel import LogModel
from logger.models.SystemModel import SystemModel
from logger.models.ModuleModel import ModuleModel
from logger.models.FuncModel import FuncModel

def index(request):
    sys = SystemModel.objects
    t = get_template('common/index.html')

    mod = ModuleModel.objects
    func = FuncModel.objects
    #html = t.render(Context({'mod':mod}))


    html = t.render(Context({'sys':sys,'mod':mod,'func':func}))
    return HttpResponse(html)
