from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from survey.models import Survey, Verbs

#import pdb; pdb.set_trace()

def index(request):
    latest_survey_list = Survey.objects.order_by('-pub_date')
    context = {'latest_survey_list': latest_survey_list}
    return render(request, 'survey/index.html', context)

def detail(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    return render(request, 'survey/detail.html', {'survey': survey})

def results(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    
    for value in survey.verbs_set.all():
        if (request.POST.get(value.verb_text), None):
            v = Verbs.objects.filter(survey=survey, verb_text=value.verb_text)
            if request.POST.get(value.verb_text) == 'on':
                v.verb_NA = True
            else:
                v.verb_scale = request.POST.get(value.verb_text)
            v.update()

    return render(request, 'survey/results.html', {'survey': survey})