from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
import datetime
from django.core.mail import send_mail, get_connection
from sample.forms import Email
from django.contrib.auth.decorators import login_required



def email(request):
    if request.method == 'POST':
        form = Email(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact/thanks/')
        else:
            form = Email()
            return render(request, 'email.html', {'form': form})
    else:
        return render(request,'email.html')





'''def upload_resume(request):
    if request.method == 'POST':
        form = Apply_Job(request.POST, request.Files)
        if form.is_valid():
            a = Apply_Job(request,upload_resume = request.Files['upload_resume'])
            a.save()
            return render_to_response('resume.html',{'form':form})
        else:
            form = Apply_Job()
            return render_to_response('resume.html',{'form':form})
        return render_to_response('resume.html')'''

