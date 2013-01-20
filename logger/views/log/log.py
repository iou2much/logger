from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from logger.models.LogModel import LogModel
from logger.models.SystemModel import SystemModel
from logger.models.ModuleModel import ModuleModel
from logger.models.FuncModel import FuncModel
from logger.models.KeynameModel import KeynameModel
from datetime import datetime
from json import loads

'''
#@register.tag(name="current_time")
def do_current_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
        print tag_name
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string[1:-1])

class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)
    def render(self, context):
        now = datetime.now()
        return now.strftime(self.format_string)
register.tag('current_time', do_current_time)
'''

def add_log(request):
    data = dict(request.POST)
    sys_name = request.POST['sys']
    mod_name = request.POST['mod']
    func_name = request.POST['func']
    try:
        open('/tmp/get','a').write(repr(request.POST)+'\n')
    except Exception,e:
        open('/tmp/get','a').write(e+'\n')

    sys = SystemModel.objects(name = sys_name)
    if not sys:
        sys = SystemModel()
        sys.name = sys_name
        sys.save()
        sys_id = sys.id
    else:
        sys_id = sys[0].id

    mod = ModuleModel.objects(sys_id = sys_id,name = mod_name)
    if not mod:
        mod = ModuleModel()
        mod.sys_id = sys_id
        mod.name = mod_name
        mod.save()
        mod_id = mod.id
    else:
        mod_id = mod[0].id

    func = FuncModel.objects(mod_id = mod_id,name = func_name)
    if not func:
        func = FuncModel()
        func.mod_id = mod_id
        func.name = func_name
        func.save()
        func_id = func.id
    else:
        func_id = func[0].id

    time = datetime.strptime(data['time'][0],'%Y-%m-%d %X')
    level = data['level'][0]
    '''
    try:
        ip = data['ip'][0]
    except:
        ip = ''
    rid = data['_rid_'][0]
    level = data.get('level',[''])[0]
    ip = data.get('ip',[''])[0]
    rid = data.get('_rid_',[''])[0]
    '''

    try:
        del data['sys']
        #del data['_rid_']
        del data['mod']
        del data['time']
        del data['level']
        del data['func']
        #del data['ip']
    except:
        pass

    detail = {}
    for k in data:
        if k == '_rid_':
            detail['rid'] = data[k][0]
        detail[k] = data[k][0]

    #log = LogModel(rid = rid, ip = ip,mod_id = mod_id,func_id=func_id,time = time,level = level, detail = detail)
    log = LogModel(mod_id = mod_id,func_id=func_id,time = time,level = level, detail = detail).exclude('id')
    log.save()
    #return HttpResponse(log.id)

#TODO:
def map_key_name(request):
    key = request.POST['key']
    sys_id = request.POST['sys_id']
    name = request.POST['name']

    kn = KeynameModel.objects(key = key,sys_id = sys_id)
    if not kn: 
        kn = KeynameModel(key = key,name = name,sys_id = sys_id)
        kn.save()
    else:
        kn = KeynameModel(id = kn[0].id,key = key,name = name)
        kn.save()
    return HttpResponse(request.POST['name'])

def ls_log(request):
    sys_id = request.GET.get('sys_id','')
    mod_id = request.GET.get('mod_id','')
    func_id = request.GET.get('func_id','')
    start = request.GET.get('start','')
    if start != '':
        start = datetime.strptime(start+':00','%Y-%m-%d %X')
    end = request.GET.get('end','')
    if end != '':
        end = datetime.strptime(end+':00','%Y-%m-%d %X')

    if sys_id !='' and mod_id == '':
        mods = ModuleModel.objects(sys_id = sys_id)
        if start == '' and end == '':
            log = LogModel.objects(mod_id__in = [mod.id for mod in mods]).order_by('-time')
        if start != '' and end == '':
            log = LogModel.objects(mod_id__in = [mod.id for mod in mods],time__gte=start).order_by('-time')
        if start == '' and end != '':
            log = LogModel.objects(mod_id__in = [mod.id for mod in mods],time__lte=end).order_by('-time')
        if start != '' and end != '':
            log = LogModel.objects(mod_id__in = [mod.id for mod in mods],time__gte=start,time__lte=end).order_by('-time')

    if mod_id != '' and func_id == '':
        if start == '' and end == '':
            log = LogModel.objects(mod_id = mod_id).order_by('-time')
        if start != '' and end == '':
            log = LogModel.objects(mod_id = mod_id,time__gte=start).order_by('-time')
        if start == '' and end != '':
            log = LogModel.objects(mod_id = mod_id,time__lte=end).order_by('-time')
        if start != '' and end != '':
            log = LogModel.objects(mod_id = mod_id,time__gte=start,time__lte=end).order_by('-time')
        #log = LogModel.objects(__raw__={'mod_id':mod_id})

    if func_id != '':
        #log = LogModel.objects(mod_id = mod_id,time__gte=start+':00',time__lte=end+':00')
        if start == '' and end == '':
            log = LogModel.objects(func_id = func_id).order_by('-time')
        if start != '' and end == '':
            log = LogModel.objects(func_id = func_id ,time__gte=start).order_by('-time')
        if start == '' and end != '':
            log = LogModel.objects(func_id = func_id ,time__lte=end).order_by('-time')
        if start != '' and end != '':
            log = LogModel.objects(func_id = func_id ,time__gte=start,time__lte=end).order_by('-time')
    if log:
        mod = ModuleModel.objects(id = log[0].mod_id)
        sys_id = mod[0].sys_id

    kn = KeynameModel.objects(sys_id = sys_id)
    keyname = {}
    for k in kn:
        keyname[k.key] = k.name

    t = get_template('log/index.html')
    html = t.render(Context({'logs':log,'detail':'detail','sys_id':sys_id,'mod_id':mod_id,'start':start,'end':end,'keyname':keyname}))
    return HttpResponse(html)

#TODO:
def rm_log(request):
    return HttpResponse('todo')
