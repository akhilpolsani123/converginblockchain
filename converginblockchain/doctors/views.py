from django.shortcuts import render,HttpResponse
from converginblockchain.models import docotrtregistrationmodel
from django.contrib import messages
from patients.models import patientsymptomsanalysis
from converginblockchain.models import patientregistrationmodel
import datetime
import time
from .models import doctorreplaysysmptoms
from django.db.models import Sum,Max
from patients.models import transactionsstore
# Create your views here.

def doctorlogincheck(request):
    if request.method == "POST":
        usid = request.POST.get('loginid')
        pswd = request.POST.get('password')
        try:
            check = docotrtregistrationmodel.objects.get(loginid=usid, password=pswd)
            request.session['docid'] = check.id
            request.session['loggeddoc'] = check.doctorname
            status = check.status
            print("Doc  id ",check.id)
            if status == "activated":
               return render(request,'doctors/doctorspage.html')
            else:
                messages.success(request, 'Your Account Not at activated')           
                return render(request,'doctor.html')

            return render(request,'doctors/doctorspage.html')
        except Exception as e:
            print('Exception is ',str(e))
    messages.success(request, 'Invalid Login Details')           
    return render(request,'doctor.html')

def doctoranalyzesysmptoms(request):
    patientsysmptoms = patientsymptomsanalysis.objects.all()
    return render(request,"doctors/doctoranalyzesysmptoms.html",{'object':patientsysmptoms}) 

def DoctorsSendPriscription(request):
    if request.method=='GET':
        id = request.GET.get('id')
        patientid = request.GET.get('patientid')
        print("ID ",id,"Patient ID",patientid)
        sts = 'waiting'
        patientsysmptoms = patientsymptomsanalysis.objects.filter(id=id,status=sts)
        patientAuth = patientregistrationmodel.objects.filter(id=patientid)
        #authkey = patientAuth.authkey
        #return HttpResponse("View Priscription")
        return render(request,"doctors/writepricription.html",{'object':patientsysmptoms,'object1':patientAuth})  

def DoctorPriscription(request):
    if request.method=='POST':
       
        patientid = request.POST.get("patientid")
        sysid = request.POST.get('sysid')
       # print('Sysmptoms ID is =  ',sysid)

        prescription1 = request.POST.get('priscription1')
        prescription2 = request.POST.get('priscription2')
        prescription3 = request.POST.get('priscription3')
        price = request.POST.get('price')
        symptmodel = patientsymptomsanalysis.objects.get(id=sysid)
        patientAuth = patientregistrationmodel.objects.get(id=patientid)
        patinetname = symptmodel.patinetname
        email= symptmodel.email
        patinetallsymptoms= symptmodel.patinetallsymptoms
        diseasname= symptmodel.diseasname
        descriptions= symptmodel.descriptions
        createdon= symptmodel.createdon
        city          =patientAuth.city
        mobile          =patientAuth.mobile
        
        blkchMoney = int(price)/10
        #print('Word to Remember ',createdon,type(createdon))
        docid = request.session['docid']
        doctorname =request.session['loggeddoc'] 
        ts = time.time()
        responsedate = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        
        #requestDate = time.mktime(datetime.datetime.strptime(createdon, '%Y-%m-%d %H:%M:%S').timetuple())#datetime.datetime.fromtimestamp(createdon).strftime('%Y-%m-%d %H:%M:%S')
        requestdate =  createdon.strftime('%Y-%m-%d %H:%M:%S')  #datetime.datetime.utcfromtimestamp(time.mktime(createdon.timetuple()))
       # print('Word to Remember ',createdon,type(createdon),type(requestdate),'Good Health ',type(responsedate))
        sts = 'waiting'
        doctorreplaysysmptoms.objects.create(patientid=patientid,sysid=sysid,patinetname=patinetname,docid=docid,doctorname=doctorname,email=email,mobile=mobile,city=city,patinetallsymptoms=patinetallsymptoms,diseasname=diseasname,descriptions=descriptions,reqdate=requestdate,prescription1=prescription1,prescription2=prescription2,prescription3=prescription3,price=price,blkchMoney=blkchMoney,respdate=responsedate,status=sts)
        patientsymptomsanalysis.objects.filter(id=sysid).update(status='given',docname=doctorname)

        #print('Black Chain money ',blkchMoney)
        #print("First Prescription is ",prescription1)
        #print("Second Prescription is ",prescription2)
        #print("Third Prescription is ",prescription3,"Patient ID ",patientid)
       
    patientsysmptoms = patientsymptomsanalysis.objects.all()
    return render(request,"doctors/doctoranalyzesysmptoms.html",{'object':patientsysmptoms}) 

def purchaseviewbydoctor(request):
    id = request.session['docid']
    docdataset = doctorreplaysysmptoms.objects.filter(docid=id,status='purchase')
    return render(request,"doctors/purchaseviewbydoctor.html",{'object':docdataset})


def doctorviewtransaction(request):
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

        return render(request,"doctors/doctorviewtransaction.html",{'object':userdata,'dph':lststate,'dpdet':obj})

        