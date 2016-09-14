from django.db import models

# Create your models here.
class Chorelist(models.Model):
	name = models.CharField(max_length = 200)
	due_date= models.DateTimeField()
# this maps to chorlist table
	def __str__(self):
		return self.name

class Chore(models.Model):
	chore_list = models.ForeignKey(Chorelist)
	name= models.CharField(max_length= 200)
	due_date= models.DateTimeField()
	complete= models.BooleanField(default=False)

#multiple chores into a Chorelist
#doing many to one relation using foreign key from many side to the one side
	def __str__(self):
		return self.name