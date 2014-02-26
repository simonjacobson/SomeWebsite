from django.shortcuts import render
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

def dashboard(request, company_id):
    try:
        company = OptionMatrix.objects.get(pk=company_id)
    except:
        raise Http404

    boxes = {'A': company.option_a,
             'B': company.option_b,
             'C': company.option_c,
             'D': company.option_d,
             'E': company.option_e,
             'F': company.option_f,
             'G': company.option_g,
             'H': company.option_h,
             'I': company.option_i,
             'J': company.option_j,
             'K': company.option_k,
             'L': company.option_l,
             'M': company.option_m,
             'N': company.option_n,
             'O': company.option_o,
             'P': company.option_p}

    return render(request, 'SomeApplication/dashboard.html', {'company': company, 'boxes': iter(sorted(boxes.items()))})

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
            c = OptionMatrix.objects.first()
            return HttpResponseRedirect(reverse('SomeApplication:dashboard', args=(c.id,)))



    messages.add_message(request, messages.constants.INFO, 'Hello world.')
    return HttpResponseRedirect(reverse('SomeApplication:login'))
    #company_list = OptionMatrix.objects.order_by('-company')[:5]
    #template = loader.get_template('SomeApplication/index.html')
    #context = RequestContext(request, {'company_list': company_list})
    #return HttpResponse(template.render(context))