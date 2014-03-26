#from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from app1.forms import MyForm


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
