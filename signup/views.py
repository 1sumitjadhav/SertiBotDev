from django.shortcuts import render
import psycopg2 as pg2

fn=''
ln=''
s=''
em=''
pwd=''
# Create your views here.
def signupaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=pg2.connect(user="postgres",password="Success",database="postgres",host="localhost",port="5432")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="passwd":
                pwd=value
        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()


    return render(request,"signup_page.html")  

        

    
    