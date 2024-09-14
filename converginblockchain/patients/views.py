from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib import messages
from random import randint
from converginblockchain.models import patientregistrationmodel
from doctors.models import doctorreplaysysmptoms
from django.db.models import Sum,Max

from nltk.corpus import wordnet 
from .models import patientsymptomsanalysis,blkchainapproach,transactionsstore
import datetime
import time
import random
# Create your views here.
class NaiveBayes:
     def __init__(self, name, symptoms):
         self.name = name
         self.symptoms = symptoms


known_diseases = [
   NaiveBayes('cold', set("sorethroat|runnynose|congestion|cough|aches".split("|"))),
   NaiveBayes('flu', set("fever|headache|muscleaches|returningfever".split("|"))),
   NaiveBayes('ebola', set("tiredness|death|bruisingover90%fbody|blackblood".split("|"))),
   NaiveBayes('spondylosis', set("Tingling|numbness|weakness|Abnormalreflexes|musclespasms".split("|"))),
   NaiveBayes('alcohol', set("antisocialbehaviour|impulsivity|self-harm|loneliness".split("|"))),
   NaiveBayes('stroke', set("Numbness|arm|Confusion|Difficultyspeaking|difficultywalking|slurredspeech".split("|"))),
   NaiveBayes('respiratory', set("phlegm|fever|difficultybreathing|abluetinttotheskin|chestpain|wheezing".split("|"))),
   NaiveBayes('pulmonary', set("dyspnea|Fatigue|faintingspells|Chestpressure|Swelling".split("|"))),
   NaiveBayes('bronchus', set("Coughwithblood|Wheezing|Shortnessofbreath|Chestpain|Flushing".split("|"))),
   NaiveBayes('Diabetes', set("thirstandhunger|urination|Weightlossorgain|Fatigue|Nausea|Blurredvision".split("|"))),
   NaiveBayes('Alzheimer', set("Memoryloss|Visionloss|Misplacingitems|Difficultymakingdecisions|meaninglessrepetition ".split("|"))),
   NaiveBayes('Dehydration', set("vomiting|sweating|Individuals|drymouth|lethargy|dizziness".split("|"))),
   NaiveBayes('Tuberculosis', set("Coughing|Chestpain|weightloss|Fatigue|Fever|Night sweats|Chills".split("|"))),
   NaiveBayes('Cirrhosis', set("jaundice|Weakness|Lossofappetite|Itching|Easybruising|darkurine".split("|"))),
   NaiveBayes('Plague', set("diarrhoea|nausea|nausea|malaise|delirium|shortnessofbreath|tenderlymphnode".split("|"))),
   
   ]

def patientlogincheck(request):
    if request.method == "POST":
        usid = request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            check = patientregistrationmodel.objects.get(loginid=usid, password=pswd)
            request.session['userid'] = check.id
            request.session['loggeduser'] = check.name
            print("patient id ",check.id)
            status = check.status
            if status == "activated":
                return render(request,'patients/patientpage.html')
            else:
                messages.success(request, 'Your Account Not at activated')           
                return render(request,'patient.html')

            return render(request,'patients/patientpage.html')
        except:
            pass
    messages.success(request, 'Invalid User id and password')           
    return render(request,'patient.html')

def patientsendsymptoms(request):
    return render(request,'patients/patientsendsymptoms.html')

def patientsymtomsanalysis(request):
    if request.method == "POST":
        symptoms = request.POST.get('symptoms')
        userid = request.session['userid'] #request.POST.get('id')
        username = ''
        email = ''
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        try:
            check = patientregistrationmodel.objects.get(id=userid)
            username = check.name
            email = check.email
            storsympto = symptoms
            #print("patient id ",check.email,symptoms)
            symptoms = symptoms.lower()
            symptoms = symptoms.split(",")

            possible = []
            for symptom in symptoms:
                for disease in known_diseases:
                     if symptom in disease.symptoms:
                        possible.append(disease.name)

            if possible:
                #print("You may have these diseases:",len(possible) )
                #print(*possible)
                for x in possible:
                    print('Disease is = ',x)
                    syn = wordnet.synsets(x) 
                    description = ''
                    #print(type(syn))
                    if len(syn)!=0:
                        description = syn[0].definition() 
                        #print(*syn[0].examples())
                        print(description)
                        #var =  patientsymptomsanalysis.objects.create(patintid=userid,patinetname=username,email=email,patinetallsymptoms=storsympto,diseasname=x,descriptions=description,createdon=st)
                        
                        #print('Var ve type ',type(var))
                    else:
                        description = 'No Data found'

                    patientsymptomsanalysis.objects.create(patintid=userid,patinetname=username,email=email,patinetallsymptoms=storsympto,diseasname=x,descriptions=description)
                    print('Desc',description)
            else:
                messages.success(request,"Good news! You're going to have a disease named after you!")

            messages.success(request, 'Thanking you for sending your sysmptoms we will get back you soon') 
            return render(request,'patients/patientsendsymptoms.html')
        except Exception  as e:
            #pass
            print(str(e))
    messages.success(request, 'There is a problam in analysing your sysmptoms')           
    return render(request,'patients/patientsendsymptoms.html')

def patientsymptomsview(request):
    userid = request.session['userid']
    patientsysmptoms = patientsymptomsanalysis.objects.filter(patintid=userid)
    return render(request,"patients/patientsymptomsview.html",{'object':patientsysmptoms})  

def checkandpay(request):
    if request.method=='GET':
        sysid = request.GET.get('pid')
        #sysmpotmsid = int(sysid)
        #reqDate = request.GET.get('createdate')
        #print("SysmpID ",sysid)
        #print(type(sysmpid),type(sysmpotmsid))
       
        check = doctorreplaysysmptoms.objects.get(sysid=sysid)
        docname = check.doctorname
        print("Doctor Name ",docname)
        return render(request,"patients/checkandpay.html",{'object':check})  

def transactionmanagement(request):
    if request.method=='POST':
        docname     = request.POST.get('doctorname')
        docid       = request.POST.get('docid')
        patientname = request.POST.get('patientname')
        patientid   = request.POST.get('patientid')
        dieses      = request.POST.get('dieses')
        sysid       = request.POST.get('sysid')
        price       = request.POST.get('price')
        nameoncard  = request.POST.get('nameoncard')
        cvv         = request.POST.get('cvv')
        cardnumber  = request.POST.get('cardnumber')
        month       = request.POST.get('month')
        year        = request.POST.get('year')

        ledbalance = float(price)/10
        expiredate = month+'/'+year
        trnxid =  random.randint(100000000000,999999999999)

        print('Post Method Workd Fine ',docname,"= ",docid)
        print('Thanking you for Purchase ',trnxid ,'Expire Date ',expiredate)
        blkchainapproach.objects.create(docname=docname,docid=int(docid),patientname=patientname,patientid=int(patientid),disease=dieses,price=float(price),sysmptid=int(sysid),ledgerbalance=ledbalance,tranxid=trnxid )
        transactionsstore.objects.create(docid=int(docid),patientid=int(patientid),nameoncard=nameoncard,cvv=int(cvv),cardnumber=cardnumber,expiredate=expiredate,tranxid=trnxid,price=float(price),ledgerbalance=ledbalance)
        #Update the payment section
        doctorreplaysysmptoms.objects.filter(sysid=sysid).update(status='purchase')
        ledbal = transactionsstore.objects.aggregate(Sum('ledgerbalance'))
        print("Led balance ",ledbal)
        #patientsymptomsanalysis.objects.filter(id=sysid).update(status='given',docname=doctorname)
        #patientsymptomsanalysis.objects.filter(id=sysid).update(status='given',docname=doctorname)
        #patientsymptomsanalysis.objects.filter(id=sysid).update(status='given',docname=doctorname)
        #patientsymptomsanalysis.objects.filter(id=sysid).update(status='given',docname=doctorname)
        messages.success(request,"Thnking you for Purchase keep updates for our news at Dp")
        
        #print("Return Data type ",type(ledbal))        
        x = ledbal.get("ledgerbalance__sum")
        x = round(x,2)
        ctx = {
            'tranxid': trnxid,
            'ledbala': x
        }
        print('Response Dictonary ',ctx)
        return render(request,"patients/paidsheet.html",{'object':ctx}) 
    #return HttpResponse('Its Works')           

def patientpurchaseblkmodel(request):
    if request.method=='GET':
        ledbal = transactionsstore.objects.aggregate(Sum('ledgerbalance'))
        x = ledbal.get("ledgerbalance__sum")
        x = round(x,2)
        print("Total Ledger Balance ",x)
        obj= transactionsstore.objects.last()
        print("The Last Transactin ID ",obj)
        print("Latest Ledger Balance ",obj.ledgerbalance)
        userid = request.session['userid']
        userdata = transactionsstore.objects.filter(patientid=userid)
        lststate = {
            'ledbalance':x
            
        }

        return render(request,"patients/patientpurchaseblkmodel.html",{'object':userdata,'dph':lststate,'dpdet':obj})
    