from django.shortcuts import render
from datetime import date
from .models import APTEST
from .models import project
# Create your views here.
def app_view(request):
    if request.method == 'POST':
      libelle=request.POST.get('libelle')
      ap=request.POST.get('ap')
      annee=request.POST.get('annee')
      if not libelle or not ap or not annee:
        print('error fo request ',libelle)
        return render(request,'myapp/insertion_op_table.html',{'error':'required field'})
      print('accepted in ',libelle)
      APTEST.objects.create(libelle=libelle,annee=annee,ap=ap)

      return render(request,'myapp/insertion_op_table.html',{'successs':'ajouter Projet'})

    return render(request,'myapp/insertion_op_table.html')
def proj_add(request):
    if request.method == 'GET':
        exist=request.GET.get('exist')
        nv=request.GET.get('nouvel')
        if exist:
            print('show me drop down')
            lis_proj=[
    {"name": "Project A", "type": "type1", "description": "Description for Project A"},
    {"name": "Project B", "type": "type1", "description": "Description for Project B"},
    {"name": "Project C", "type": "type2", "description": "Description for Project C"},
    {"name": "Project D", "type": "type2", "description": "Description for Project D"},
    {"name": "Project E", "type": "type3", "description": "Description for Project E"},
]
            print(lis_proj)
            return render(request,'myapp/insertion_pr_table.html',{'exist':exist,'project':lis_proj})
        if nv:
            print('new project show forms')
            return render(request,'myapp/insertion_pr_table.html',{'nouvel':nv})
        if not exist and not nv:
            return render(request,'myapp/insertion_pr_table.html')
    if request.method == 'POST':
        libl=request.POST.get('libelle_pr')
        numindv=request.POST.get('Num-indv')
        ap_act=request.POST.get('ap')
        dp_cml=request.POST.get('dp_cm')
        pec=request.POST.get('PEC')
        dp_prev=request.POST.get('dp_prev')
        current_date = date.today()
        if not libl or not numindv or not ap_act or not dp_cml or not pec or not dp_prev:
            print('errore request POST',libl)
        print('success')
        project.objects.create(Libelle=libl,num_indiv=numindv,AP_Act=ap_act,dp_cum=dp_cml,PEC=pec,dp_prev=dp_prev,date_chng=current_date)
        return render(request,'myapp/insertion_pr_table.html',{'successs':'ajouter Projet'})

        
        
