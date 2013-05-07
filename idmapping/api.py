from tastypie.resources import ModelResource
from tastypie import fields
from idmapping.models import ExternalDB, ExternalID, KBaseID

class ExternalDBResource(ModelResource):
    class Meta:
        queryset = ExternalDB.objects.all()
        resource_name = 'externalDB'

# how to get kbase ids to appear here?
class ExternalIDResource(ModelResource):
    externaldb = fields.ForeignKey(ExternalDBResource, 'externaldb')
    class Meta:
        queryset = ExternalID.objects.all()
        resource_name = 'externalID'

class KBaseIDResource(ModelResource):
    externalids = fields.ToManyField(ExternalIDResource,'externalids', full=True)
    class Meta:
        queryset = KBaseID.objects.all()
        resource_name = 'kbaseID'

