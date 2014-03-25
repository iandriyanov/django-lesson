#from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext


# Create your views here.
def basic(request):
    args = {}
    args.update(csrf(request))
    args['gender'] = "Пол не выбран"
    _lcsrf = RequestContext(request)
    if request.POST:
        if "meminfo" in request.POST.get('sys', ''):
            import os
            args['gender'] = os.listdir("./")
            return render_to_response('basic.html', args, context_instance=_lcsrf)
        else:
            gender = request.POST.get('sex', '')
            args['gender'] = request.POST.get('sex', '')
            return render_to_response('basic.html', args, context_instance=_lcsrf)

    return render_to_response('basic.html', args, context_instance=_lcsrf)
