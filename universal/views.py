from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'universal/home.html')

def contacts(request):
    return render(request, 'universal/contacts.html')

def awdocuments(request):
    return render(request, 'universal/awdocuments.html')

def guidesigt(request):
    return render(request, 'universal/guidesigt.html')

def guidesigv(request):
    return render(request, 'universal/home.html')

def igt(request):
    return render(request, 'universal/igt.html')

def igv(request):
    return render(request, 'universal/igv.html')

def ldmresources(request):
    return render(request, 'universal/ldmresources.html')

def notices(request):
    return render(request, 'universal/notices.html')

def opportunities(request):
    return render(request, 'universal/opportunities.html')

def projects(request):
    return render(request, 'universal/projects.html')

def visa_for_externals(request):
    return render(request, 'universal/visaforexternals.html')
