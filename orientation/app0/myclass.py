import json
from operator import itemgetter

def moyen(request):
    option_bac=float(request.session['option_bac'])

    if option_bac==1:
        #"lett":{"ar":4 , "ge":4 , "fr":4 , "an":4 , "ph":4}}
        notes=(float(request.GET['ar']),float(request.GET['ge']),float(request.GET['fr']),
                float(request.GET['an']),float(request.GET['ph']) )
        coef=(4,4,4,4,4)
    elif option_bac==2:
        # "eco":{"math":1 , "conta":4 , "Generale":4 ,"gestion":4 , "francais":4 , "anglais":3 },
        notes=(float(request.GET['ma']),float(request.GET['co']),float(request.GET['ec']),
                 float(request.GET['ge']),float(request.GET['fr']),float(request.GET['an']) )
        coef=(1,4,4,4,4,3)
    elif option_bac==3:
        #pc":{"math":5 ,"pc":5 ,"svt":5 ,"francais":3 ,"anglais":2 },
        notes=(float(request.GET['ma']),float(request.GET['ph']),float(request.GET['sc']),
                float(request.GET['fr']),float(request.GET['an']) )
        coef=(5,5,5,3,2)
    elif option_bac==4:
         #"math":{"math":6 , "pc":4 ,"svt":3 ,"francais":4 , "anglais":4 },
        notes=(float(request.GET['ma']),float(request.GET['ph']),float(request.GET['sc']),
                 float(request.GET['fr']),float(request.GET['an']) )
        coef=(6,4,3,4,4)
    elif option_bac==5:
        # "tech":{"math":5 , "pc":5 , "ing":5 , "francais":3 , "anglais":2 },
        notes=(float(request.GET['ma']),float(request.GET['ph']),float(request.GET['sc']),
         float(request.GET['fr']),float(request.GET['an']) )
        coef=(5,5,5,3,2)
    x=0
    for n,c in zip(notes,coef):
        x+=n*c
    return x/20

def input_loisir(request):
    ls=[]
    for i in range(1,22):
        x = request.GET.get('ch'+str(i), False)
        if x != False:
            ls.append(i)
    return tuple(ls)

def region(request):
    regions=((1,1),(2,2),(3,3),(4,4),(4,5),(4,6),(6,5),(5,6),(5,7),(6,7),(7,7),(6,8))
    input_reg_x=int(request.session['region'][0])
    input_reg_y=int(request.session['region'][1])
    dist=[]
    for reg in regions:
        dist.append(((reg[0]-input_reg_x)**2 +(reg[1]-input_reg_y)**2)**0.5)
    dist.sort()
    return list(set(dist))

def distance(request,db_region):
    input_reg_x,input_reg_y=int(request.session['region'][0]),int(request.session['region'][1])
    db_region_x,db_region_y=int(db_region[0]),int(db_region[1])
    return ((db_region_x-input_reg_x)**2 +(db_region_y-input_reg_y)**2)**0.5

def getFilieres(base_dir):
    with open(base_dir+'\\json\\loisir.json', 'r') as f:
        data=f.read()
        data=json.loads(data)['filieres']
        return data

def trier(lst):
    lst.sort(key=lambda x:x[0])



