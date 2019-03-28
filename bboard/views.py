from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import db
from .models import Rubric

# Create your views here.

def index(request):
    bbs = db.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbc': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    bbs = db.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbc': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

# def index(request):
#     "Low level style rendering"
#     template =  loader.get_template('bboard\index.html')
#     bbs = db.objects.order_by('-published')
#     context = {'bbs': bbs}
#     # s = 'Список объявлений\r\n\r\n\r\n'
#     # for obj in db.objects.order_by('-published'):
#     #     s += obj.title + '\r\n' + obj.content + '\r\n'
#
#     return HttpResponse(template.render(context, request))