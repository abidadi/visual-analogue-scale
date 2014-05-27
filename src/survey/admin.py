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
        import csv
        from django.http import HttpResponse
        import StringIO

        f = StringIO.StringIO()
        writer = csv.writer(f)
        writer.writerow(["name", "pub_date"])

	#import pdb; pdb.set_trace()

        for s in queryset:
		for verb in s.verbs_set.all():
		      	writer.writerow([verb.verb_text,verb.verb_scale,verb.verb_NA])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=vaSurvey_data.csv'
        return response

    download_csv.short_description = "Download CSV"
    
admin.site.register(Survey, SurveyAdmin)