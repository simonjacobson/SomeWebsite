from django.db import models

# Create your models here.

class Company(models.Model):
	ticker = models.CharField(max_length=3)
	role = models.CharField(max_length=250)
	option_a = models.BooleanField()
	option_b = models.BooleanField()
	option_c = models.BooleanField()
	option_d = models.BooleanField()
	option_e = models.BooleanField()
	option_f = models.BooleanField()
	option_g = models.BooleanField()
	option_h = models.BooleanField()
	option_i = models.BooleanField()
	option_j = models.BooleanField()
	option_k = models.BooleanField()
	option_l = models.BooleanField()
	option_m = models.BooleanField()
	option_n = models.BooleanField()
	option_o = models.BooleanField()
	option_p = models.BooleanField()

	business_unit = models.CharField(max_length=250)
	role = models.CharField(max_length=250)
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	timestamp = models.DateTimeField(auto_now_add=True)
	
	def __unicode__( self ):
		return "{}".format(self.ticker)

    
class Person(models.Model):
	email_address = models.ForeignKey(Company)
	company = models.CharField(max_length=3)
	business_unit = models.CharField(max_length=250)
	role = models.CharField(max_length=250)
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__( self ):
		return "{} {}".format(self.first_name, self.last_name)
		
    
class Incident(models.Model):
	company = models.ForeignKey(Company)
	incident_number = models.CharField(max_length=250)
	timestamp = models.DateTimeField(auto_now_add=True)

	reported_by = models.ForeignKey(Person)
	business_unit = models.CharField(max_length=250)
	business_owner = models.CharField(max_length=250)
	note = models.CharField(max_length=3200)
	cost = models.DecimalField(max_digits=16,decimal_places=2)
	action = models.CharField(max_length=3200)
	change_reason = models.CharField(max_length=3200)
	status = models.CharField(max_length=250)
	triggered = models.BooleanField()
	risk_category = models.CharField(max_length=250)
	kri_category = models.CharField(max_length=250)
	
	def __unicode__( self ):
		return "Incident number {}".format(self.incident_number)