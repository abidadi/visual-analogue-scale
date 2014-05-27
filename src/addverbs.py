from survey.models import Survey, Verbs

f = open('verbs.txt')
for survey in Survey.objects.all():
        if (survey.name == 'Swati'):
            f = open('verbs.txt')
            verb_count = 0
            for line in f:
                    verb, created = Verbs.objects.get_or_create(verb_text=line.strip().title(),survey=survey)
                    if created:
                        verb_count += 1
            f.close()