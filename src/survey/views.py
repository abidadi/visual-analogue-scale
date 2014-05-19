from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from survey.models import Survey, Verbs

def index(request):
    latest_survey_list = Survey.objects.order_by('-pub_date')
    context = {'latest_survey_list': latest_survey_list}
    return render(request, 'survey/index.html', context)

def detail(request, survey_id):
    survey = get_object_or_404(Survey)
    return render(request, 'survey/detail.html', {'survey': survey})

def results(request, survey_id):
    p = get_object_or_404(Survey, pk=survey_id)
    return HttpResponse("Results.")