from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

def aboutUs(request):
    data={
        'title':'home new',
        'clist':['php','java','django'],
        'numbers':[],
        'student_details':[
            {'name':'abc','phone':'123'},
            {'name':'xyz','phone':'456'}
        ]
    }
    return render(request,"index.html",data)

def manj(request):
    return render(request,"manj.html")

def courseDetails(request, courseId):
    return HttpResponse(courseId) 

def user(request):
    # fins=0
    f1=0
    data={}
    try:
        # n1=int(request.GET['num1'])
        # n2=int(request.GET['num2'])
        # n1=request.GET.get('num1')
        # n2=request.GET.get('num2')
        if request.method=="POST":
           n1=int(request.POST.get('num1'))
           n2=int(request.POST.get('num2'))
           f1=n1+n2
        # print(n1+n2);
        # fins=n1+n2;
           data={
            'n1':n1,
            'n2':n2,
            'output':f1
                    }
        # return HttpResponseRedirect('/about-us')
        url="/about-us/?output={}".format(f1)
        return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"userform.html",data)     