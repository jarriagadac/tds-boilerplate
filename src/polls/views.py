from django.http import HttpResponse
from .models import Question
from django.template import loader


def index(request):
    template = loader.get_template('polls/index.html')
    questions = Question.objects.all()
    context = {'questions': questions}
    return HttpResponse(template.render(context, request))
