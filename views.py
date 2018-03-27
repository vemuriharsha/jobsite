import datetime

from django.contrib.auth.decorators import login_required
# from django.core.validators import validate_email
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

from .models import Jobs, Apply, UserEmail, Board, Email


#from oauthlib import  *

#from requests_oauthlib import OAuth2Session
#from requests_oauthlib.compliance_fixes import linkedin_compliance_fix


def index(request):
    return render(request, 'jobs/index.html')

def success(request):

    if 'email' in request.GET and request.GET['email']:

        email = request.GET['email']

    #newsletter = request.POST.get('checkbox', '')
    data = """
    Hello there!

    I wanted to personally write an email in order to welcome you to our platform.\
     We have worked day and night to ensure that you get the best service. I hope \
    that you will continue to use our service. We send out a newsletter once a \
    week. Make sure that you read it. It is usually very informative.

    Cheers!
    ~ Harsha
        """
    user = UserEmail(email=email)
    user.save()
    #if newsletter == 'on':
    send_mail('Welcome!', data, "Harsha",
              [email], fail_silently=False)
    return render(request, 'jobs/success.html',{'email':email})

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'jobs/current_datetime.html', {'current_date': now})

def home_page(request):
    jobs = Jobs.objects.all()
    return render(request,'jobs/home_page.html',{'jobs':jobs})

def main(request):
    return render(request,'jobs/main.html')

def search(request):
    if 'sample' in request.GET and request.GET['sample']:
        message1 = 'You searched for: %r' % request.GET['sample']
        message2 = request.GET['sample']
        if not message2:
            error = False
        else:

            job = Jobs.objects.filter(jobtype__icontains=message2).values_list('jobtype','desc', 'description','requirements','location')

        #return HttpResponse(job.desc)
            return render(request,'jobs/search_result.html',{'jobs': job})
            return render(request, 'jobs/home_page.html', {'error': error})
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)

def search1(request):
    if 'search' in request.GET and request.GET['search']:
        message1=request.GET['job']
       # print 'job is' +message1
    #if 'job' in request.GET and request.GET['job']:
        message2=request.GET['sample']
       # print 'city is' +message2
        if not  message2:
            error = False
        else:
            job = Jobs.objects.filter(location__icontains=message2).values_list('jobtype', 'desc', 'description','requirements', 'location')
            return render(request, 'jobs/search_result.html', {'jobs': job})
            return render(request, 'jobs/home_page.html', {'error': error})
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)


def apply(request):

    if 'Apply' in request.GET and request.GET['Apply']:
        applyjob = request.GET['Apply']
    if 'email' in request.GET and request.GET['email']:
        email = request.GET['email']
        print email
        p1 = Email(email=email)
        p1.save()
        #return render(request, 'jobs/apply_job.html', {'apply for job': applyjob})
        return render(request, 'jobs/apply_job.html')

def store(request):
    if 'disconnect' in request.GET and request.GET['disconnect']:
        return render(request, 'jobs/apply.html')
    if 'sample' in request.GET and request.GET['sample']:
        signoff=request.GET['sample']

    if 'fname' in request.GET and request.GET['fname']:
        firstname = request.GET['fname']

    if 'lname' in request.GET and request.GET['lname']:
        lastname = request.GET['lname']

    if 'headline' in request.GET and request.GET['headline']:
        headline = request.GET['headline']

    if 'industry' in request.GET and request.GET['industry']:
        industry = request.GET['industry']

    if 'mob' in request.GET and request.GET['mob']:
        phone = request.GET['mob']

    if 'email' in request.GET and request.GET['email']:
        email = request.GET['email']

        #try:
            #validate_email('email')
            #valid_email=True
        #except validate_email.ValidationError:
            #valid_email=False
    if 'city' in request.GET and request.GET['city']:
        city = request.GET['email']
    if 'zip' in request.GET and request.GET['zip']:
        zipcode = request.GET['zip']
    if 'country' in request.GET and request.GET['country']:
        country = request.GET['country']
    if 'statepro' in request.GET and request.GET['statepro']:
        stateprovince = request.GET['statepro']

    if 'resume' in request.GET and request.GET['resume']:
        resume = request.GET['resume']

    #if 'g_resume' in request.GET and request.GET['g_resume']:
        #gresume = request.GET['g_resume']

    #if 'Login' in request.GET and request.GET['Login']:
       # linlogin = request.GET['Login']
       # print 'linkedin details',linlogin


        p1= Apply(signoff=signoff,firstname=firstname,lastname=lastname,headline=headline,industry=industry,mobile=phone,email=email,city=city,zipcode=zipcode,country=country,stateprovince=stateprovince, resume=resume)
        p1.save()

        data = """
            Hello there!

            Your Application is successfully submitted.
             we will getback to you as soon as possible.

            Cheers!
            ~ Harsha
                """
        send_mail('Welcome!', data, "Harsha",
                  [email], fail_silently=False)

        p2=Apply.objects.all().values_list('firstname','lastname','resume')
        return render(request,'jobs/thanks.html')


def home(request):
    boards=Board.objects.all()
    return  render(request,'jobs/home.html',{'boards':boards})


def login(request):
    return render_to_response('jobs/login.html')


@login_required(login_url='/')
def home1(request):
    return render_to_response('jobs/home1.html')

def home2(request):
    return render_to_response('jobs/home2.html')

def complete(request):
    if request.user.is_authenticated:
        linkedin_user = request.user.social_auth.get(provider='linkedin-oauth2')
        extra_data = linkedin_user.extra_data
        return render(request, 'jobs/apply_job1.html',{'data':extra_data})

def logout(request):
    return render(request,'jobs/apply.html')

def join(request):
    return  render(request,'jobs/join.html')

def disconnect(request):
    return render(request,'jobs/apply_job.html')

#from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
def google(request):
   ''' SCOPES = 'https://www.googleapis.com/auth/drive.readonly.metadata',
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)

    DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))
    files = DRIVE.files().list().execute().get('files', [])
    #for f in files:

       # print(f['name'], f['mimeType'])
    #return render(request,'jobs/googleresult.html',{'files':files})
    return render(request, 'jobs/googleresult.html', {'files': files})'''


   return render(request,'jobs/google.html')


