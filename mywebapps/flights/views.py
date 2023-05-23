from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

#to import Student Table class from models.py
from flights.models import Flight

#to import class from forms.py
from . forms import AgentProfile

# Create your views here.
def Flight_Details(request):

    flight1 = ['USA', 'UK', 10]
    flight2 = ['Canada', 'Franch', 30]
    flight3 = ['USA', 'Germany', 40]
    flight4 = ['Franch', 'Germany', 70]
    flight5 = ['Italy', 'Norway', 120]

    flight_count = {'fg1' : flight1, 'fg2' : flight2, 'fg3' : flight3, 
                    
                    'fg4' : flight4, 'fg5' : flight5}

    return render(request,'flights/flightdetails.html', flight_count)

#table view
def client_info(request):
    
    c_info = Flight.objects.all()

    return render(request, 'flights/clientsinfo.html', {'client' : c_info })

#for form API

def agent_info(request):

    if request.method == "POST":

        agent_frm = AgentProfile(request.POST)
    
    else:

        agent_frm = AgentProfile(auto_id= 'agent_%s', label_suffix=":", 
                             initial={'Last_name' : 'your last name',
                                      'First_name':'your first name',
                                      'email': 'agents@email.com'}) #from forms.py
        
        '''agent_frm.order_fields(field_order=['acode', 'Last_name', 
                                        'email','password', 'First_name', 'mobile', 
                                        'textarea', 'checkbox'])'''

    return render(request, 'flights/agentsinfo.html',{'agents' : agent_frm })

