from django.db import models

# Create your models here.

# TODO: Remove 'Poll' at some point.
class Poll(models.Model):
    def __unicode__(self):
        return self.question
    def _choice(self):
        return self.choice_set.all()
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    choice = property(_choice)

# TODO: Remove 'Choice' at some point.
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text

class ExternalDB(models.Model):
    def __unicode__(self):
        return self.name
    name        = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=200)
    url         = models.CharField(max_length=255)

class KBaseIDTypes(models.Model):
    def __unicode__(self):
        return self.name
    name        = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=200)

class ExternalID(models.Model):
    def __unicode__(self):
        return self.identifier
    def _kbaseids(self):
        return self.kbaseid_set.all()
    identifier  = models.CharField(max_length=50,unique=True)
    externaldb  = models.ForeignKey(ExternalDB)
    kbaseids = property(_kbaseids)
     
class KBaseID(models.Model):
    def __unicode__(self):
        return self.identifier
    identifier  = models.CharField(max_length=50,unique=True)
    externalids = models.ManyToManyField(ExternalID)

     

