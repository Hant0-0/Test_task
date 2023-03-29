import pdfkit
from celery import shared_task
from celery.app import task
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from check_app.models import Check


@shared_task
def my_task(check_pk):
    check = get_object_or_404(Check, pk=check_pk)
    context = {'check': check}
    html = render_to_string('check_app/index.html', context)

    pdf = pdfkit.from_string(html, False)

    response = JsonResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+str(check_pk)+'_'+str(check.check_type)+'.pdf'


    if response.status_code != 200:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response


