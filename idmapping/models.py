from django.db import models

# Create your models here.

class Poll(models.Model):
    def __unicode__(self):
        return self.question
    def _choice(self):
        return self.choice_set.all()
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    choice = property(_choice)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text
