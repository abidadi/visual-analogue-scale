import csv
import StringIO

from django.http import HttpResponse
from django.contrib import admin

from survey.models import Survey, Verbs

class VerbsInline(admin.TabularInline):
    model = Verbs
    extra = 3

class SurveyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'pub_date')
    inlines = [VerbsInline]

    actions = ['download_csv']

    def download_csv(ModelAdmin, request, queryset):
        f = StringIO.StringIO()
        writer = csv.writer(f)
        writer.writerow(["name", "value", "N/A", "survey"])

        for s in queryset:
            for verb in s.verbs_set.all():
                writer.writerow([verb.verb_text, verb.verb_scale, verb.verb_NA, verb.survey.name])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=vaSurvey_data.csv'
        return response

    download_csv.short_description = "Download CSV"

admin.site.register(Survey, SurveyAdmin)
