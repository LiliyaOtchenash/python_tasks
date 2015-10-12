from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from .models import Table
from django.views.generic.edit import FromView

class TableView(FormView):
    template_name = 'table.html'


def index(request):
    text_list = Table.objects.order_by('-text')[:]
    template = loader.get_template('table/index.html')
    context = RequestContext(request, {
        'text_list': text_list,
    })
    return HttpResponse(template.render(context))

def det(request, tab_num):
    texts = get_object_or_404(Table, pk=tab_num)
    return render(request, 'table/det.html', {'texts': texts})
   # return HttpResponse('Def det %s.' % tab_num)

def res(request, tab_num):
    veriabl = 'Def res %s.'
    return HttpResponse(veriabl % tab_num)

def vot(request, tab_num):
    return HttpResponse('Def vot %s.' % tab_num)

# Create your views here.
