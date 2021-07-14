from django.shortcuts import render
from .forms import signupform,loginform,DailyUpdateForm,ClientDetailsField
from django.views.decorators.cache import cache_control
from django.http import HttpResponseRedirect
from .models import signup,DailyUpdate,ClientDetails
import datetime
# Create your views here.

@cache_control(no_cache=True,no_store=True,must_revalidate=True)
def home(request):
    return render(request,'home.html')

#@cache_control(no_cache=True,no_store=True,must_revalidate=True)
def exe_signup(request):
    submitted = False
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/signup?submitted=True')
            #return render(request,'login.html')
        else:
            return render(request,'signup.html',{'form':form,'submitted':submitted})
    
    else:
        form = signupform
        if 'submitted' in request.GET:
            submitted= True
        return render(request,'signup.html',{'form':form,'submitted':submitted})

@cache_control(no_cache=True,no_store=True,must_revalidate=True)
def login(request):
    if request.method == 'POST':
        
        userid = request.POST['Mobile']
        password = request.POST['Password']
        signup_data =signup.objects.all()
        for data in signup_data:
            if (data.Email == userid or data.Mobile == userid) and data.Password == password:
                return render(request,'exe_forms.html')
        else:
            form = loginform
            message = 'Authentication Failed'
            return render(request,'login.html',{'form':form,'message':message})
    
    else:
        form = loginform
        return render(request,'login.html',{'form':form})

def dailyupdate(request):
    
    submitted = False
    if request.method == 'POST':
        form = DailyUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dailyupdate?submitted=True')
        else:
            form = DailyUpdateForm
            submitted=False
            return render(request,'form1.html',{'form':form})
        
    else:
        date_data = DailyUpdate.objects.all()
        today_date = datetime.date.today()
        print('today_date',today_date)
        for date in date_data:
           if date.Date ==today_date:
               form = ClientDetailsField
               message = 'Daily Update already Filled Today,If you want to check Go through DAILY REPORT'
               return render(request,'form2.html',{'form':form,'message':message})
            

        else:
            form = DailyUpdateForm
            if 'submitted' in request.GET:
                submitted= True
            return render(request,'form1.html',{'form':form})

def clientdetails(request):
    if request.method=='POST':
        form = ClientDetailsField(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/clientdetails?submitted=True')
        return render(request,'form2.html',{'form':form})
    else:
        form = ClientDetailsField
        if 'submitted' in request.GET:
            submitted= True
        else:
            submitted = False
        return render(request,'form2.html',{'form':form,'submitted':submitted})

def dailyreport_page(request):
    values = DailyUpdate.objects.all()
    #values = 
    return render(request,'dailyreport.html',{'values':values})

def clientreport_page(request):
    values = ClientDetails.objects.all()
    return render(request,'clientreport.html',{'values':values})
