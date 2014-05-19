import datetime
from django.utils import timezone
from django.db import models
from decimal import Decimal

class Survey(models.Model):
	name = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')

class Verbs(models.Model):
	survey = models.ForeignKey(Survey)
	verb_text = models.CharField(max_length=200)	# Verbs
	verb_scale = models.DecimalField(max_digits=4,decimal_places=1,default=Decimal("0.0"))
	verb_NA = models.BooleanField(default=False)	# Checkbox