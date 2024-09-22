from django.shortcuts import render

# Create your views here.
def sum(request):
    if request.method=="POST":
        num1=int(request.POST.get('txtnumber1'))
        num2=int(request.POST.get('txtnumber2'))
        result=num1 + num2
        return render(request,'Basics/Sum.html',{'sum':result})
    else:
        return render(request,'Basics/Sum.html')

def sumofThree(request):
    if request.method=="POST":
        numb1=int(request.POST.get('txtnumber1'))
        numb2=int(request.POST.get('txtnumber2'))
        numb3=int(request.POST.get('txtnumber3'))
        if (numb1>=numb2 and numb1>=numb3):
            largest=numb1
        elif(numb2>=numb1 and numb2>=numb3):
            largest = numb2
        else :
            largest = numb3  
        if (numb1<=numb2 and numb1<=numb3):
            Smallest=numb1
        elif(numb2<=numb1 and numb2<=numb3):
            Smallest = numb2
        else :
            Smallest = numb3
        return render(request,'Basics/sumofThree.html',{'smallest':Smallest,'sumofThree':largest})
        
    else:
        return render(request,'Basics/sumofThree.html')