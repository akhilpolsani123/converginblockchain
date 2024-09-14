from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib import messages
from .forms import patientregistrationform,doctorregistrationform
from .models import patientregistrationmodel,docotrtregistrationmodel
from random import randint
from django.db.models import Sum,Max
from patients.models import transactionsstore
from django.db.models import Sum,Max
from patients.models import transactionsstore
from doctors.models import doctorreplaysysmptoms

def home(request):
    template = 'home.html'
    context = {}
    return render(request,template,context)

def patient(request):
    template = 'patient.html'
    context = {}
    return render(request,template,context)

def doctor(request):
    template = 'doctor.html'
    context = {}
    return render(request,template,context)


def patientregister(request):
    
    if request.method=='POST':
       
        form = patientregistrationform(request.POST)       
        if form.is_valid():
            print('Am Not Human but no humanity')
            form.save()   
            messages.success(request, 'You have been successfully registered')        
            return HttpResponseRedirect('patient')
        else:
            print("Invalid form")    
    else:
        form = patientregistrationform()
    return render(request,'patientregister.html',{'form':form})                


def doctorregistration(request):
    if request.method=='POST':
       
        form = doctorregistrationform(request.POST)       
        if form.is_valid():
            
            form.save()   
            messages.success(request, 'You have been successfully registered')        
            return HttpResponseRedirect('doctor')
        else:
            print("Invalid doctor Form")    
    else:
        form = doctorregistrationform()
    return render(request,'doctorregister.html',{'form':form})                



def adminlogin(request):
    return render(request,'adminlogin.html')
    


def txmanagerlogin(request):
    return render(request,'trxlogin.html')    

def trnxmngrloginaction(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'txmanager' and pswd == 'txmanager':
                return render(request,'admins/tranxhome.html')
            else:
                messages.success(request, 'Invalid login id and password')      
    return render(request,'trxlogin.html')


def adminloginaction(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return render(request,'admins/adminhome.html')
            else:
                messages.success(request, 'Invalid user id and password')      
    return render(request,'adminlogin.html')

def viewadminpatientspage(request):
    patientdata = patientregistrationmodel.objects.all()
    #return HttpResponse("Redirect to Admin View Patients")
    return render(request,'admins/viewppatientsdata.html',{'object':patientdata})

def viewadmindoctorspage(request):

    docotrtdata = docotrtregistrationmodel.objects.all()
    #return HttpResponse("Redirect to Admin View Patients")
    return render(request,'admins/viewdoctordata.html',{'object':docotrtdata})
    #return render(request,'adminactivateDoctors.html') 

def viewadmintransactionspage(request):
    ledbal = transactionsstore.objects.aggregate(Sum('ledgerbalance'))
    x = ledbal.get("ledgerbalance__sum")
    x = round(x,2)
    print("Total Ledger Balance ",x)
    id = request.session['docid']
    obj= transactionsstore.objects.last()
    print("The Last Transactin ID ",obj)
    print("Latest Ledger Balance ",obj.ledgerbalance)
        
    userdata = transactionsstore.objects.all()
    lststate = {
    'ledbalance':x
           
       }

    return render(request,"admins/viewadmintransactionspage.html",{'object':userdata,'dph':lststate,'dpdet':obj})

  # return HttpResponse("Redirect to Transaction Page")
    #return render(request,'adminaviewtransactions.html')        
def logout(request):
    return render(request,'home.html')      

def activatepatients(request):
    if request.method=='GET':
        pid = request.GET.get('pid')
        authkey = random_with_N_digits(8)
        status = 'activated'
        print("PID = ",pid,authkey,status)   
        patientregistrationmodel.objects.filter(id=pid).update(authkey=authkey , status=status)     
        patientdata = patientregistrationmodel.objects.all()
        #return HttpResponse("Redirect to Admin View Patients")
        return render(request,'admins/viewppatientsdata.html',{'object':patientdata})

def activatedoctors(request):
    if request.method=='GET':
        pid = request.GET.get('pid')
        authkey = random_with_N_digits(8)
        status = 'activated'
        print("PID = ",pid,authkey,status)   
        docotrtregistrationmodel.objects.filter(id=pid).update(authkey=authkey , status=status)     
        docotordata = docotrtregistrationmodel.objects.all()
        #return HttpResponse("Redirect to Admin View Patients")
        return render(request,'admins/viewdoctordata.html',{'object':docotordata})


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def patientsymptomsview(request):
    patientsysmptoms = patientsymptomsanalysis.objects.all()
    #return HttpResponse("Redirect to Admin View Patients")
    return render(request,'patients/viewppatientsdata.html',{'object':patientsysmptoms})

def trnxviewtransaction(request):
    if request.method=='GET':
        ledbal = transactionsstore.objects.aggregate(Sum('ledgerbalance'))
        x = ledbal.get("ledgerbalance__sum")
        x = round(x,2)
        print("Total Ledger Balance ",x)
        id = request.session['docid']
        obj= transactionsstore.objects.last()
        print("The Last Transactin ID ",obj)
        print("Latest Ledger Balance ",obj.ledgerbalance)
        userid = request.session['userid']
        userdata = transactionsstore.objects.filter(docid=id)
        lststate = {
            'ledbalance':x
            
        }

        return render(request,"admins/trnxviewtransac.html",{'object':userdata,'dph':lststate,'dpdet':obj})



def trnxviewpurchase(request):
    docdataset = doctorreplaysysmptoms.objects.filter(status='purchase')
    return render(request,"admins/trnxviewpurchase.html",{'object':docdataset})
