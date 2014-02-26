from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from SomeApplication.models import OptionMatrix, Incident, Person
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.contrib import messages


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
    email = request.POST['user']
    password = request.POST['pass']

    p = Person.objects.filter(email_address=email).first()

    if p is not None:
        if password == p.password:
            return HttpResponseRedirect(reverse('SomeApplication:dashboard', args=(p.id,)))

    messages.add_message(request, messages.constants.INFO, 'Email does not exist on our database')
    return HttpResponseRedirect(reverse('SomeApplication:login'))
    #company_list = OptionMatrix.objects.order_by('-company')[:5]
    #template = loader.get_template('SomeApplication/index.html')
    #context = RequestContext(request, {'company_list': company_list})
    #return HttpResponse(template.render(context))

def report(request, report_type, person_id, company):

    p = Person.objects.filter(id=person_id).first()
    return render(request, 'SomeApplication/report.html', {'report_type': report_type, 'person': p})
def report_post(request):

    pass