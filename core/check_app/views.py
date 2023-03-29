import os.path

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from check_app.models import Check
from check_app.tasks import my_task

wkhtml_to_pdf = os.path.join(settings.BASE_DIR, "wkhtmltopdf.exe")

def check_generate(request, check_pk):
    check = get_object_or_404(Check, pk=check_pk)
    return render(request, 'check_app/index.html', {'check': check})



def test_pdf(request, check_pk):
    my_task.delay(check_pk)
    return HttpResponse('PDF is being generated asynchronously')


