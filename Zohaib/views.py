from django.shortcuts import render
FILE_PATH = "messages.txt"


def home(request):
    return render(request ,'home.html')
def about(request):
    return render(request ,'about.html')
def contact(request):
    if request.method=="POST":
        n_ame=request.POST.get("name","").strip()
        e_mail=request.POST.get("email","").strip()
        mes_age=request.POST.get("message","").strip()
        with open("messages.txt","a") as file:
            file.write(f"{n_ame},{e_mail},{mes_age}\n")
    
        return render(request, 'contact.html', {'status': 'app ka message send hogya'})

        
        
    return render(request, 'contact.html')

    
