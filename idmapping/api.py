from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie import fields
from idmapping.models import ExternalDB, ExternalID, KBaseID

# auth/authz classes need to be defined before models that use them
# it seems like auth is not needed to do authz
class KBaseAuthorization(Authorization):
    def is_authorized(self,request,object=None):
# will want to do an in test for GET, HEAD, OPTIONS, but for now
# this is ok
        if request.method == 'GET':
            print request.method
# this seems to work!  comment out for testing
# uncomment to allow anonymous read requests
#            return True
# currently just look for a valid token
# later want to restrict to group
        if request.user.username:
# for groups: look through this structure and look for the right groupname
# (need to figure out the pythonesque idiom for this)
            print request.META['KBASEprofile']['groups']
            return True
        return False

class ExternalDBResource(ModelResource):
    class Meta:
        queryset = ExternalDB.objects.all()
        resource_name = 'externalDB'
	authorization = Authorization()

# how to get kbase ids to appear here?
class ExternalIDResource(ModelResource):
    externaldb = fields.ForeignKey(ExternalDBResource, 'externaldb',full=True)
# this line may be problematic if there's an external id with no kbase ids?
# need to investigate further
    kbaseids = fields.ToManyField('idmapping.api.KBaseIDResource','kbaseids')
    class Meta:
        queryset = ExternalID.objects.all()
        resource_name = 'externalID'
	authorization = Authorization()
	filtering = {
		"identifier": ('icontains','contains','exact','startswith',),
	}

class KBaseIDResource(ModelResource):
    externalids = fields.ToManyField(ExternalIDResource,'externalids',full=True)
    class Meta:
        queryset = KBaseID.objects.all()
        resource_name = 'kbaseID'
	authorization = Authorization()
#	authorization = KBaseAuthorization()


