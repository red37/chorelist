from django.contrib import admin

# Register your models here.
from .models import Chorelist,Chore
class ChoreInLine(admin.TabularInline):
	model = Chore
	extra = 3

class ChorelistAdmin(admin.ModelAdmin):
	fieldsets = [
			(None, {'fields': ['name']}),
			('Date Info', {'fields' : ['due_date'], 'classes': ['collapse']})
				]
	inlines = [ChoreInLine]

admin.site.register(Chorelist, ChorelistAdmin)
