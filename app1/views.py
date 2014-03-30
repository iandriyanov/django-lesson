#from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from app1.forms import MyForm


# Create your views here.
def mainpage(request):
    args = {}
    args.update(csrf(request))
    args['site_title'] = "My django server admin"
    args['proj_name'] = "Django server-panel"
    args['menu_name'] = "Menu"
    args['name_page'] = "Main"
    args['desc_page'] = "Page description"
    return render_to_response('index.html', args)


def srvinfo(request):

    def gethostname():
        import socket
        return socket.gethostname()

    def getuname():
        import os
        return os.uname()

    # Вероятно надо будет потом использовать uptime модуль, но сейчас так:
    def getuptime():
        from datetime import timedelta
        with open('/proc/uptime', 'r') as f:
            uptime_sec = float(f.readline().split()[0])
            uptime_str = str(timedelta(seconds=uptime_sec))
        return uptime_str

    args = {}
    args.update(csrf(request))
    args['site_title'] = "My django server admin"
    args['proj_name'] = "Django server-panel"
    args['menu_name'] = "Menu"
    args['name_page'] = "Server information"
    args['desc_page'] = "Page description"
    args['hostname'] = gethostname()
    args['uname'] = getuname()
    args['sysname'] = getuname()[0]
    args['relver'] = getuname()[2]
    args['archver'] = getuname()[4]
    args['uptime'] = getuptime()
    return render_to_response('srv_info.html', args)


def srvinfo_detail(request):

    def getmem():
        from subprocess import Popen, PIPE
        cmd = "free -m | sed '/Mem/!d' | awk '{print $2}'"
        output = Popen(cmd, shell=True, stdout=PIPE).communicate()
        memsize = int(output[0])
        return str(memsize)

    def gethumanmem():
        from subprocess import Popen, PIPE
        cmd = "free -h | sed '/Mem/!d' | awk '{print $2}'"
        output = Popen(cmd, shell=True, stdout=PIPE).communicate()
        memsize = output[0].decode()
        memsize = memsize.replace("\n", "")
        return str(memsize)

    args = {}
    args.update(csrf(request))
    if request.POST:
        if 'mem' in request.POST['system_ddlist']:
            flash_str = "Total memory size: %s MByte (%s)" \
                % (getmem(), gethumanmem())
            args['flash_info'] = flash_str
            return render_to_response('srv_properties.html', args)
        else:
            return render_to_response('srv_properties.html', args)
    return render_to_response('srv_properties.html', args)


def tostop(request):
    return render_to_response('stop.html')


def basic(request):
    args = {}
    args.update(csrf(request))
    args['gender'] = "Пол не выбран"
    _lcsrf = RequestContext(request)
    if request.POST:
        if "meminfo" in request.POST.get('sys', ''):
            import os
            args['gender'] = os.listdir("./")
            return render_to_response('basic.html', args)
        else:
            args['gender'] = request.POST.get('sex', '')
            return render_to_response('basic.html', args)

    return render_to_response('basic.html', args, context_instance=_lcsrf)


def my_view(request):
    args = {}
    _lcsrf = RequestContext(request)
    form = MyForm()
    args.update(csrf(request))
    args['form'] = form
    if request.POST:
        if "uname" in request.POST['my_choice_field']:
            import os
            args['text'] = " ".join(os.uname())
        elif "listdir" in request.POST['my_choice_field']:
            import os
            args['comm'] = os.listdir("./")
        else:
            args['text'] = request.POST['my_choice_field']
        return render_to_response('test.html', args, context_instance=_lcsrf)
    return render_to_response('test.html', args)
