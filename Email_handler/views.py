from django.shortcuts import render
from cryptography.fernet import Fernet
from django.core.mail import EmailMessage, get_connection
import qrcode
import io
import random 
from . models import Certificates
# Create your views here.
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
                to = [data[4]]
                chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                cert_id = ""
                for i in range(10):
                    cert_id += random.choice(chars)
                qr_dummy = qrcode.make("https://www.google.com/"+cert_id)
                qr = qr_dummy
                qr.save('static/qr_code/'+cert_id+'.png')
                message = '''
                Hello {name} {lname},
                    Congo! You have successfully completed the course on {course}
                    You can download your certificate by scanning the qr code or 
                    by following the link http://127.0.0.1/certificate/ 

                    Thanking you 
                    CareTeam Pvt Ltd 
                '''.format(name=data[0],lname=data[2],course=data[5])  
                Email = EmailMessage(
                    'Certificate',
                    message,
                    'billing@mycareteam.tech',
                    to,
                    connection=connection
                )
                Email.attach_file('static/qr_code/'+cert_id+'.png')
                Email.send()
                Certificates.objects.create(
                    cert_id =cert_id,
                    fname = data[0],
                    midname = data[1],
                    lname = data[2],
                    Phone = data[3],
                    Email = data[4],
                    Course = data[5]
                )
            connection.close()
        return render(request,"email.html",{'entries':data_list})
    else :
        return render(request,"email.html")
