"""converginblockchain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include

from .views import home,trnxmngrloginaction,trnxviewtransaction,trnxviewpurchase
from .views import patient,patientregister,doctor,doctorregistration,adminlogin,txmanagerlogin,adminloginaction
from .views import viewadminpatientspage,viewadmindoctorspage,viewadmintransactionspage,logout,activatepatients,activatedoctors
from patients.urls import urlpatterns as patients_urlpattern
from patients.views import patientlogincheck,patientsendsymptoms,patientsymtomsanalysis,patientsymptomsview,checkandpay,transactionmanagement,patientpurchaseblkmodel
from doctors.views import doctorlogincheck,doctoranalyzesysmptoms,DoctorsSendPriscription,DoctorPriscription,purchaseviewbydoctor,doctorviewtransaction

urlpatterns = [
    #url(r'^patients/',include((patients_urlpattern,'patients'),namespace='patients'),name='patients'),    
    url(r'^admin/', admin.site.urls),
    url(r'^$',home, name="home"),
    url(r'^patient/', patient, name="patient"),
    url(r'^home/',home, name="home"),
    url(r'^patientregister/',patientregister, name="patientregister"),
    url(r'^doctor/',doctor, name="doctor"),
    url(r'^doctorregistration/',doctorregistration, name="doctorregistration"),
    url(r'^adminlogin/',adminlogin, name="adminlogin"),
    url(r'^txmanagerlogin/',txmanagerlogin, name="txmanagerlogin"),
    url(r'^adminloginaction/',adminloginaction,name="adminloginaction"),
    url(r'^viewadminpatientspage/',viewadminpatientspage,name="viewadminpatientspage"),
    url(r'^viewadmindoctorspage/',viewadmindoctorspage,name="viewadmindoctorspage"),
    url(r'^viewadmintransactionspage/',viewadmintransactionspage,name="viewadmintransactionspage"),
    url(r'^logout/',logout,name="logout"),
    #url(r'^activatepatients/',activatepatients,name="activatepatients")
    url(r'^activatepatients/$', activatepatients, name="activatepatients"),
    url(r'^activatedoctors/$', activatedoctors, name="activatedoctors"),
    url(r'^trnxmngrloginaction/',trnxmngrloginaction,name="trnxmngrloginaction"),
    url(r'^trnxviewtransaction/',trnxviewtransaction,name="trnxviewtransaction"),
    url(r'^trnxviewpurchase/',trnxviewpurchase,name="trnxviewpurchase"),

    url(r'^patientlogincheck/', patientlogincheck, name="patientlogincheck"),
    url(r'^patientsendsymptoms/', patientsendsymptoms, name="patientsendsymptoms"),
    url(r'^patientsymtomsanalysis/', patientsymtomsanalysis, name="patientsymtomsanalysis"),
    url(r'^patientsymptomsview/',patientsymptomsview, name="patientsymptomsview"),
    url(r'^checkandpay/',checkandpay, name="checkandpay"),
    url(r'^transactionmanagement/', transactionmanagement, name="transactionmanagement"),
    url(r'patientpurchaseblkmodel/',patientpurchaseblkmodel, name="patientpurchaseblkmodel"),

    url(r'^doctorlogincheck/',doctorlogincheck, name="doctorlogincheck"),
    url(r'^doctoranalyzesysmptoms/',doctoranalyzesysmptoms,name="doctoranalyzesysmptoms"),
    url(r'^DoctorsSendPriscription/',DoctorsSendPriscription, name="DoctorsSendPriscription"),
    url(r'^DoctorPriscription/',DoctorPriscription,name="DoctorPriscription"),
    url(r'^purchaseviewbydoctor/',purchaseviewbydoctor,name="purchaseviewbydoctor"),
    url(r'^doctorviewtransaction/',doctorviewtransaction,name="doctorviewtransaction"),

    

]
