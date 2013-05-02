from django.contrib import admin
#from idmapping.models import Poll, Choice, ExternalDB, ExternalID, KBaseID
from idmapping.models import ExternalDB, ExternalID, KBaseID

#admin.site.register(Poll)
#admin.site.register(Choice)
admin.site.register(ExternalDB)
admin.site.register(ExternalID)
admin.site.register(KBaseID)
