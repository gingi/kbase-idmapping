from tastypie.resources import ModelResource
from tastypie import fields
from idmapping.models import Poll,Choice

class ChoiceResource(ModelResource):
    poll = fields.ForeignKey('idmapping.api.PollResource','poll', )
    class Meta:
        queryset = Choice.objects.all()
        resource_name = 'choice'

class PollResource(ModelResource):
    choice = fields.ToManyField(ChoiceResource,'choice')
    class Meta:
        queryset = Poll.objects.all()
        resource_name = 'poll'

