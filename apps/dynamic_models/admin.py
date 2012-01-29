from django.contrib import admin
from dynamic_models.models import BaseDynamicModel


baseDynamic = BaseDynamicModel()
models = baseDynamic.registry

admin.site.register([model for model in models.values()])
