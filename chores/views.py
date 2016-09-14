from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, Http404
from .models import Chorelist

# Create your views here.

def index(request):
	lists = Chorelist.objects.all()
	context = {'chorelists': lists}
	return render(request,'chores/index.html', context)

def detail(request, chorelist_id):
	list = get_object_or_404(Chorelist, pk = chorelist_id)
	return render(request,'chores/detail.html', {'chorelists': list})

def chores(request, chorelist_id):
	list = get_object_or_404(Chorelist, pk = chorelist_id)
	chores = list.chore_set.all()
	return render(request,'chores/chores.html', {'chorelists': list, 'chores': chores})


def choredetail(request, chorelist_id, chore_id):
	list = get_object_or_404(Chorelist, pk = chorelist_id)
	chore = get_object_or_404(Chore, pk = chore_id)
	return render(request,'chores/choredetail.html', {'chorelists': list, 'chore': chore})

