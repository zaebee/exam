from django.db.models import get_model
from django.http import HttpResponse, Http404
from django.views.generic.simple import direct_to_template

from django.utils import simplejson


def get_qs(request, model_name):
    model = get_model('dynamic_models', model_name)
    if not model:
        raise Http404
    fields = [f.name for f in model._meta.fields]
    qs = model.objects.all().values_list(*fields)
    fields = [f.verbose_name for f in model._meta.fields]
    result = {'fields': fields, 'qs':list(qs)}
    if request.is_ajax():
        return HttpResponse(simplejson.dumps(result),
                            mimetype='application/json')
    else:
        raise Http404


def model_list(request):
    if request.is_ajax():
        raise Http404
    return direct_to_template(request,
                              'dynamic_models/model_list.html',
                              {'data': 'data'})
