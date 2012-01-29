from django.db.models import get_model
from django.http import HttpResponse, Http404
from django.views.generic.simple import direct_to_template

from django.core.serializers import serialize


def get_qs(request, model_name):
    model = get_model('dynamic_models', model_name)
    qs = model.objects.all()
    data = serialize('json', qs)
    if request.is_ajax():
        return HttpResponse(data, mimetype='application/json')
    else:
        raise Http404


def model_list(request):
    if request.is_ajax():
        raise Http404
    return direct_to_template(request, 'dynamic_models/model_list.html',
                              {'data': 'data'})
