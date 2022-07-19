from django.shortcuts import render
import psycopg2 as pg2

em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em,pwd #make em,pwd global
    if request.method=="POST":
        m=pg2.connect(user="postgres",password="Success",database="postgres",host="localhost",port="5432")#connect to database
        cursor=m.cursor#cursor will do indexing
        d=request.POST
        for key,value in d.items():
            if key=="email":#take email
                em=value
            if key=="password":#take pwd
                pwd=value
        c="select * from users where email='{}' and password='{}' ".format(em,pwd) #sql query
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,"error.html")
        else:
            return render(request,"welcome.html")

        


    return render(request,"login.html")  

        

    
    