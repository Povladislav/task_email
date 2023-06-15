from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import MailingList
from .tasks import send_mailing


def index(request):
    mailing_lists = MailingList.objects.all()
    return render(request, 'mailing/index.html', {'mailing_lists': mailing_lists})


@csrf_exempt
def create_mailing_list(request):
    name = request.POST.get('name')
    email = request.POST.get('email')

    if name and email:  # Проверяем наличие значения name и email
        mailing_list = MailingList(name=name, email=email)
        mailing_list.save()
        send_mailing.delay(mailing_list.id, "testSubject", "Good")
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Name and email are required.'})
