from django.http import HttpResponse
from django.shortcuts import render
def start(request):
    return HttpResponse ('welcome to myweb')
def mid(request):
    return HttpResponse ('i am ayyan')
def end(request):
    return HttpResponse ('contact us')

def homep(request):
    return render(request,'practice.html')
def resultprac(request):
    namep=request.GET['namprac']
    messag=f'HI {namep} welcome to website'
    return render(request,'practice2.html',{'mess':messag})


def student(request):
    students={
        'ali':78,
        'ahmad':92,
        'usman':45,
        'ayan':86,
        'hamza':59,
        'zain':67
    }
    avg=sum(students.values())/len(students.values())
    avg2=round(avg,2)
    mx=max(students.values())
    lw=min(students.values())
    std_pass=0
    std_fail=0
    dict_pass={}
    dict_grades={}
    grade_count={'A':0,'B':0,'C':0,'D':0,'F':0}
    for salu in students.values():
        if salu>=60:
            std_pass+=1
        else:
            std_fail+=1
    for name,marks in students.items():
        if marks>=60:
            dict_pass[name.upper()]=min(marks+5,100)
    for name2,marks2 in students.items():
        if marks2>=90:
            grade='A'
            dict_grades[name2.upper()]=grade
            grade_count[grade]+=1
        elif marks2>=80:
            grade='B'
            dict_grades[name2.upper()]=grade
            grade_count[grade] +=1
        elif marks2>=70:
            grade='C'
            dict_grades[name2.upper()]=grade
            grade_count[grade] +=1
        elif marks2>=60:
            grade='D'
            dict_grades[name2.upper()]=grade
            grade_count[grade] +=1
        else:
             grade='F'
             dict_grades[name2.upper()]=grade
             grade_count[grade] +=1
    return render(request,'prac.html',{'average':avg2,'max':mx,'lowest':lw,'passed':std_pass,'passers':dict_pass,'grades':dict_grades,'numofgrade':grade_count})



