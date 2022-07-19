import imp
from django.http import HttpResponse
from django.shortcuts import render
from cryptography.fernet import Fernet
from django.core.mail import EmailMessage, get_connection
import qrcode
import io


def homePage(request):
#    data={
#       'title' : 'Home Page'
#   }
    return render(request,"index.html")

def aboutUS(request):
    return HttpResponse("Welcome sumit")

def course(request):
    return HttpResponse("Welcome sumit course")


def userForm(request):
    return render(request,"userform.html")

def checkdata(request):
    if request.method == 'POST':
        file = request.FILES['data_file']
        file_obj = file.chunks()
        L = []
        for line in file_obj:
            L.append(line)
        stream = io.BytesIO(L[0])
        data_list = []
        for data in stream:
            pydata = data.decode('ISO-8859-1')
            fresh_data = pydata.replace("\r\n","")
            Entry = fresh_data.split(",")
            data_list.append(Entry)
        
        connection = get_connection()        
        with connection as connection: 
            for data in data_list:
                to = [data[5]]
                key = Fernet.generate_key()
                qr_dummy = qrcode.make("https://www.google.com/"+str(key))
                qr = qr_dummy
                qr.save('static/img/'+data[1]+'.png')  
                Email = EmailMessage(
                    'Certificate',
                    'Hello dear, We are successfull in sending this ',
                    'billing@mycareteam.tech',
                    to,
                    connection=connection
                )
                Email.attach_file('static/img/'+data[1]+'.png')
                Email.send()
            connection.close()
        return render(request,"email.html",{'entries':data_list})
    else :
        return render(request,"email.html")
