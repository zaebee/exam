from django.db.models import get_model
from django.http import HttpResponse
from django.views.generic.simple import direct_to_template

from django.utils import simplejson
from django.core.serializers import serialize


def get_qs(request, model_name):
    model = get_model('dynamic_models', model_name)
    qs = model.objects.all()
    data = serialize('json', qs)
    return HttpResponse(simplejson.dumps(data),
                        mimetype='application/javascript')


def model_list(request):
    return direct_to_template(request, 'dynamic_models/model_list.html',
                              {'data': 'data'})
