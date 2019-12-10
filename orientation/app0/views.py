from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import json 
import os 
import app0.myclass
from operator import itemgetter
# Create your views here.
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\app0\\static\\"

def index(request):
    request.session['index']=False
    request.session['note']=False
    request.session['loisir']=False 
    request.session['filieres']=app0.myclass.getFilieres(base_dir)   
    return render(request,"index.html")

def note(request):#re=request.GET.get('region', False)
    if not request.session['index']:
        op = request.GET['option_bac']
        re=request.GET['region']
        if (op!='Votre filiere du baccalauréat' and re!='Région où vous habitez') and (int(op) in [1,2,3,4,5] and int(re) in [11,22,33,45,46,65,56,57,67,77,68]):   
            request.session['index']=True
            request.session['option_bac']=op
            request.session['region']=re
            #filitre sur les option de bac
            dt=[]
            for filiere in request.session['filieres']:
                if int(op) in filiere['option_bac']:
                    dt.append(filiere)
            request.session['filieres']=dt
            return render(request,"note"+op+".html")#vers les notes
        else:
            return render(request,"index.html")
    else:
        return redirect('/index/') 

def loisir(request):
    if not request.session['note']:
        if request.GET['btn'][0]=='s':
            request.session['note']=True 
            m=app0.myclass.moyen(request)
            dt=[]
            for filiere in request.session['filieres']:
                ec=[]
                for ecole in filiere['ecoles']:
                    if int(ecole.split(" ")[2])<=m:
                        ec.append(ecole)
                if len(ec)!=0:
                    dt.append({'nom':filiere['nom'],'loisirs':filiere['loisirs'],'ecoles':ec})
            request.session['filieres']=dt
            return render(request,"loisir.html")
        elif request.GET['btn']=='p':
            return  redirect('/index/')
    else:
        return  redirect('/index/')


def result(request):
    #filtre sur les loisirs
    if not request.session['loisir']:
        request.session['loisir']=True 
        input_loisirs= app0.myclass.input_loisir(request)
        dt=[]
        for filiere in request.session['filieres']:
            c=0
            for loisir in input_loisirs:
                if loisir in filiere['loisirs']:
                    c+=1
            dt.append([c,filiere])
        dt.sort(key=itemgetter(0),reverse=True)
        
        dct=[]
        c=0
        regs=app0.myclass.region(request)
        
        for filiere in dt:
            for r in regs :
                for ecole in filiere[1]['ecoles']:
                    if r==app0.myclass.distance(request,ecole.split()[3]):
                        if c<3:
                            dct.append((c+1,{'filiere':filiere[1]['nom'],'ecole':ecole.split()[0],'ville':ecole.split()[1]}))
                            c+=1
        
        return render(request,"resultat.html",locals())
    else:
        return redirect('/index/')


    