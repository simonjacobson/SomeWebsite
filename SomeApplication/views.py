from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from SomeApplication.models import OptionMatrix, Incident, Person
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.mail import send_mail
import time

def index(request):
    company_list = OptionMatrix.objects.order_by('-company')[:5]
    template = loader.get_template('SomeApplication/index.html')
    context = RequestContext(request, {'company_list': company_list})
    return HttpResponse(template.render(context))

# is equal to
#def index(request):
#    company_list = Poll.objects.all().order_by('-pub_date')[:5]
#    context = {'company_list': company_list}
#    return render(request, 'SomeApplication/index.html', context)

def dashboard(request, person_id):
    person = Person.objects.filter(id=person_id).first()

    companies = OptionMatrix.objects.filter(person__id=person_id).all()

    tbl = []
    for x in companies:
        coll = {'A': x.option_a,
                'B': x.option_b,
                'C': x.option_c,
                'D': x.option_d,
                'E': x.option_e,
                'F': x.option_f,
                'G': x.option_g,
                'H': x.option_h,
                'I': x.option_i,
                'J': x.option_j,
                'K': x.option_k,
                'L': x.option_l,
                'M': x.option_m,
                'N': x.option_n,
                'O': x.option_o,
                'P': x.option_p}

        tbl.append(iter(sorted(coll.items())))
        x.boxes = iter(sorted(coll.items()))

    return render(request, 'SomeApplication/dashboard.html', {'companies': companies, 'table': tbl, 'person': person})

# is equal to
#def dashboard(request, company_id):
#    get_object_or_404(Company, pk=company_id)
#    return render(request, 'SomeApplication/dashboard.html', {'company': company})




def login(request):
    return render(request, 'SomeApplication/login.html')


def login_post(request):
    email = request.POST['user'].strip()
    password = request.POST['pass'].strip()

    p = Person.objects.filter(email_address=email).first()

    if p is not None:
        return HttpResponseRedirect(reverse('SomeApplication:dashboard', args=(p.id,)))

    messages.add_message(request, messages.constants.INFO, 'Email does not exist on our database')
    return HttpResponseRedirect(reverse('SomeApplication:login'))


def report(request, report_type, person_id, company):
    p = Person.objects.filter(id=person_id).first()
    #return render(request, 'SomeApplication/report.html', {'report_type': report_type, 'person': p, 'company': company})
    form = IncidentForm(initial={'risk_category': report_type,
                                 'kri_category': report_type,
                                 'person_id': person_id,
                                 'email_address': p.email_address,
                                 'business_unit': p.business_unit,
                                 'role': p.role,
                                 'first_name': p.first_name,
                                 'last_name': p.last_name,
                                 'company': company
    })
    return render(request, 'SomeApplication/report_form.html', {
        'form': form,
        'timestamp': time.time()
    })

def report_post(request):
    pass


def forgot_password(request):
    return render(request, 'SomeApplication/forgot_password.html', {})


def forgot_password_post(request):
    email = request.POST['email']

    p = Person.objects.filter(email_address=email).first()
    send_mail('Your password',
              'Dear {} {}, your password is {}.'.format(p.first_name, p.last_name, p.password),
              'spam@killbotlogic.com.com',
              [email, 'me@killbotlogic.com'],
              fail_silently=False)

    messages.add_message(request, messages.constants.INFO, 'Your password has been sent to {}'.format(email))
    return HttpResponseRedirect(reverse('SomeApplication:login'))


from django import forms


class IncidentForm(forms.ModelForm):

    person_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Incident
        fields = ['incident_number',
                  'business_owner',
                  'note',
                  'cost',
                  'action',
                  'change_reason',
                  'status',
                  'triggered',
                  'risk_category',
                  'kri_category',
                  'email_address',
                  'company',
                  'business_unit',
                  'role',
                  'first_name',
                  'last_name']
