from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


class RecordResource(ModelResource):

    class Meta:
        queryset = Record.objects.all()
        resource_name = 'record'
        authorization = RecordAuthorization()
        #authentication = ApiKeyAuthentication()
        filtering = {
                "id": ALL,
                "content": ALL,
                "name": ALL,
                "domain": ALL_WITH_RELATIONS,
        }
