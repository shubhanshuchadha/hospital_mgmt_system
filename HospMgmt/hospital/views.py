from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import *

# Create your views here.

#display the about page
def about(request):
    return render(request, 'about.html')

#display the contact page
def contact(request):
    return render(request, 'contact.html')

#Home Page
def index(request): 

    #if user has not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    #For displaying the number of doctors, patients, and appointments
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()
    d = 0
    p = 0
    a = 0
    for i in doctors:
        d += 1
    for i in patients:
        p += 1
    for i in appointments:
        a += 1

    d1 = {'d':d,'p':p,'a':a}
    return render(request, 'index.html', d1)

#Login Page
def Login(request):
    error = None
    if request.method == 'POST':

        #Receive entered username and password
        u = request.POST["uname"]
        p = request.POST["pwd"]

        #Authenticate and login user
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "No"
            else:
                error = "Yes"
        except:
            error = "Yes"

    d = {'error' : error}
    return render(request, 'login.html', d)

#Logout Function
def Logout(request):

    #if not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    #logout user
    logout(request)

    #Go to login page
    return redirect('/admin_login/')

#View doctors
def view_doctor(request):

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    #Take all objects doctor objects and send them in a dictionary
    doc = Doctor.objects.all()
    d = {'doc':doc}

    #Render the page
    return render(request, 'view_doctor.html', d)

#Add doctors
def add_doctor(request):
    error = None

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    if request.method == 'POST':

        #Get doctor data
        n = request.POST["name"]
        c = request.POST["contact"]
        s = request.POST["special"]
        t = request.POST["type"]

        try:
            #Create a doctor object
            Doctor.objects.create(name=n, mobile=c, special=s, type_of_doctor=t)
            error = "No"
        except:
            error = "Yes"

    #Render page
    d = {'error' : error}
    return render(request, 'add_doctor.html', d)

#Delete doctors
def delete_doctor(request, pid):

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    #delete doctor with given id
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()

    #Go to view_doctors page
    return redirect('/view_doctor/')

#Edit doctor
def edit_doctor(request, pid):
    error = None

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    doc = Doctor.objects.get(id=pid)

    if request.method == 'POST':

        #Get doctor data
        n = request.POST["name"]
        c = request.POST["contact"]
        s = request.POST["special"]
        t = request.POST["type"]
        
        try:
            #Create a doctor object
            doc.name = n
            doc.mobile = c
            doc.special = s
            doc.type_of_doctor = t
            doc.save()
            error = "No"
        except:
            error = "Yes"

    #Render page
    d = {'error' : error, "doc":doc}
    return render(request, 'edit_doctor.html', d)

#View Patients
def view_patient(request):

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    #Send all patient objects to page to be rendered
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request, 'view_patient.html', d)

#Add patients
def add_patient(request):
    error = None

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    if request.method == 'POST':

        #Get all details
        n = request.POST["name"]
        g = request.POST["gender"]
        c = request.POST["contact"]
        a = request.POST["address"]

        try:
            #create patient object
            Patient.objects.create(name=n, mobile=c, gender=g, address=a)
            error = "No"
        except:
            error = "Yes"

    #Render the page
    d = {'error' : error}
    return render(request, 'add_patient.html', d)

#Delete patients
def delete_patient(request, pid):

    #Send user to login page if not logged in
    if not request.user.is_staff:
        return redirect('/admin_login/')

    #Delete patient whose id is given
    patient = Patient.objects.get(id=pid)
    patient.delete()

    #Render the page
    return redirect('/view_patient/')

#Edit patient
def edit_patient(request, pid):
    error = None

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    pat = Patient.objects.get(id=pid)

    if request.method == 'POST':

        #Get all details
        n = request.POST["name"]
        g = request.POST["gender"]
        c = request.POST["contact"]
        a = request.POST["address"]
        
        try:
            #create patient object
            pat.name = n
            pat.gender = g
            pat.mobile = c
            pat.address = a
            pat.save()
            error = "No"
        except:
            error = "Yes"

    #Render the page
    d = {'error' : error, "pat":pat}
    return render(request, 'edit_patient.html', d)

#View appointment
def view_appointment(request):

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    #send all objects to page
    app = Appointment.objects.all()
    d = {'app':app}
    return render(request, 'view_appointment.html', d)

#Add appointment
def add_appointment(request):
    error = None

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    #Take all doctors and patients and send them to the page
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    if request.method == 'POST':

        #Receive details
        d = request.POST["doctor"]
        p = request.POST["patient"]
        d1 = request.POST["date1"]
        t1 = request.POST["time1"]
        doctor1 = Doctor.objects.filter(name=d).first()
        patient1 = Patient.objects.filter(name=p).first()
        try:

            #Create appointment
            Appointment.objects.create(doctor=doctor1, patient=patient1, date1=d1, time1=t1)
            error = "No"
        except:
            error = "Yes"

    #Send dictionary to the page
    d = {'doctor':doctors,'patient':patients,'error' : error}
    return render(request, 'add_appointment.html', d)

#Delete appointment
def delete_appointment(request, pid):

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    #Delete appointment
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('/view_appointment/')

#Edit appointment
def edit_appointment(request, pid):
    error = None

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    appoint = Appointment.objects.get(id=pid)

    #Take all doctors and patients and send them to the page
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    

    if request.method == 'POST':

        #Receive details
        d = request.POST["doctor"]
        p = request.POST["patient"]
        d1 = request.POST["date1"]
        t1 = request.POST["time1"]
        doctor1 = Doctor.objects.filter(name=d).first()
        patient1 = Patient.objects.filter(name=p).first()
        try:

            #Edit appointment
            
            appoint.doctor = doctor1
            appoint.patient = patient1
            appoint.date1 = d1
            appoint.time1 = t1
            appoint.save()
            error = "No"
        except:
            error = "Yes"

    #Send dictionary to the page
    d = {'doctor':doctors,'patient':patients,'error' : error, "appoint":appoint}
    return render(request, 'edit_appointment.html', d)

#View medicine
def view_medicine(request):

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    #send all objects to page
    med = Medicine.objects.all()
    d = {'med':med}
    return render(request, 'view_medicine.html', d)

#Add medicine
def add_medicine(request):
    error = None

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    if request.method == 'POST':

        #Get all details
        n = request.POST["name"]
        mfd = request.POST["mfd"]
        ed = request.POST["ed"]
        q = request.POST["q"]

        try:
            #create medicine object
            Medicine.objects.create(name=n, manufacturing_date=mfd, expiry_date=ed, quantity=q)
            error = "No"
        except:
            error = "Yes"

    #Render the page
    d = {'error' : error}
    return render(request, 'add_medicine.html', d)

#Delete medicine
def delete_medicine(request, pid):

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    #Delete appointment
    medicine = Medicine.objects.get(id=pid)
    medicine.delete()
    return redirect('/view_medicine/')

#Edit medicine
def edit_medicine(request, pid):
    error = None

    #If user is not logged in, send to login page
    if not request.user.is_staff:
        return redirect('/admin_login/')

    med = Medicine.objects.get(id=pid)

    if request.method == 'POST':

        #Get all details
        n = request.POST["name"]
        mfd = request.POST["mfd"]
        ed = request.POST["ed"]
        q = request.POST["q"]
        
        try:
            #edit medicine object
            med.name = n
            med.manufacturing_date = mfd
            med.expiry_date = ed
            med.quantity = q
            med.save()
            error = "No"
        except:
            error = "Yes"

    #Render the page
    d = {'error' : error, "med":med}
    return render(request, 'edit_medicine.html', d)

