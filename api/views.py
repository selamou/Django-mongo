
from rest_framework.decorators import api_view
from django.http import HttpResponse

from api.forms import PostCours, PostTd, PostTp
from .models import EtudientProfile, Filiere, Matiere,Cours, ProfProfile, Td, Tp, User
from .serializer import  MatiereSerializer,CoursSerializer, ProfDserilizer, RegisterprofSerializer, RegisteruserSerializer, TdSerializer, TpSerializer, filierSerializer, loginSerializer, loginprofSerializer, loginuserSerializer, updateseriliser
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from django.http import *
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
@login_required(login_url='/login/')
def edit_post(request, id,titre,type):
    if type=="cours":
        Cou = get_object_or_404(Cours, titre=titre)

        if request.method == 'GET':
            context = {'form': PostCours(instance=Cou), 'Appartient': id,'id':id ,'type':type}
            return render(request,'modifier.html',context)
        if request.method == "POST":
                a=Matiere.objects.get(id=request.POST["Appartient"])

                Cours.objects.get(titre=request.POST["titre"]).delete()
                Cours.objects.create(titre=request.POST["titre"],description=request.POST["description"],pdf_cours=request.FILES['pdf_cours'],Appartient=a)

                return redirect('detail' ,id=id ) 
    elif type=="TD":
        t = get_object_or_404(Td, titre=titre)

        if request.method == 'GET':
            context = {'form': PostTd(instance=t), 'Appartient': id,'id':id,'type':type}
            return render(request,'modifier.html',context)
        if request.method == "POST":
            k = get_object_or_404(Td, titre=titre)
            pdf_TD_correction = request.FILES.get('pdf_TD_correction', False)
            pdf_TD = request.FILES.get('pdf_TD', False)
            if pdf_TD_correction == False:
                if pdf_TD ==False:
                    print("vide") 

                else: 
                    print("vide1")
                    a=Matiere.objects.get(id=request.POST["Appartient"])
                    Td.objects.create(titre=request.POST["titre"],description=request.POST["description"],pdf_TD=request.FILES['pdf_TD'],pdf_TD_correction=k.pdf_TD_correction,Appartient=a)

                    Td.objects.get(titre=request.POST["titre"]).delete()
                    
            else:
                if pdf_TD ==False:
                    print("vide2")
                    a=Matiere.objects.get(id=request.POST["Appartient"])
                    Td.objects.get(titre=request.POST["titre"]).delete()
                    Td.objects.create(titre=request.POST["titre"],description=request.POST["description"],pdf_TD=k.pdf_TD,pdf_TD_correction=request.FILES['pdf_TD_correction'],Appartient=a)

                    
                    
                else:
                    print("aucune changement") 

            return redirect('detailTD' ,id=id)
    elif type=="TP":
            t = get_object_or_404(Tp, titre=titre)

            if request.method == 'GET':
                context = {'form': PostTp(instance=t), 'Appartient': id,'id':id ,'type':type}
                return render(request,'modifier.html',context)
            if request.method == "POST":
                    a=Matiere.objects.get(id=request.POST["Appartient"])
                    pdf_TP = request.FILES.get('pdf_TP', False)
                    if pdf_TP==False:
                        print('vide')
                    else: 
                        Tp.objects.get(titre=request.POST["titre"]).delete()
                        Tp.objects.create(titre=request.POST["titre"],description=request.POST["description"],pdf_TP=request.FILES['pdf_TP'],Appartient=a)



                    return redirect('detailTP' ,id=id )  

@login_required(login_url='/login/')      
def delete_post(request, id,titre,type):

    if type=="cours":
                Cours.objects.get(titre=titre).delete()
                return redirect('detail' ,id=id ) 
    elif type=="TD":
            
            Td.objects.get(titre=titre).delete()
            return redirect('detailTD' ,id=id)
    elif type=="TP":
                    print("bll")
                    Tp.objects.get(titre=titre).delete()
                    return redirect('detailTP' ,id=id ) 

@login_required(login_url='/login/')
def uploadTD(request,id):
    if request.method == "POST":
            a=Matiere.objects.get(id=request.POST["Appartient"])
            if request.POST['pdf_TD_correction'] =='':
                Td.objects.create(titre=request.POST["titre"],description=request.POST["description"],pdf_TD=request.FILES['pdf_TD'],Appartient=a)

            else:
                print(request.FILES['pdf_TD'])
                Td.objects.create(titre=request.POST["titre"],description=request.POST["description"],pdf_TD=request.FILES['pdf_TD'],pdf_TD_correction=request.FILES['pdf_TD_correction'],Appartient=a)

            return redirect('detailTD' ,id=id)
    else:
        form = PostTd()
    return render(request,'uploadcours.html',{'form':form,'id':id,'type':"TD"})
@login_required(login_url='/login/')
def uploadTP(request,id):
    if request.method == "POST":
            a=Matiere.objects.get(id=request.POST["Appartient"])
            print(request.FILES['pdf_TP'])
            Tp.objects.create(titre=request.POST["titre"],description=request.POST["description"],pdf_TP=request.FILES['pdf_TP'],Appartient=a)

            return redirect('detailTP' ,id=id)
    else:
        form = PostTp()
    return render(request,'uploadcours.html',{'form':form,'id':id,'type':"TP"})
@login_required(login_url='/login/')
def download(request,type,titre):
        if type=="cours":
            queryset = Cours.objects.get(titre=titre)  
            response = HttpResponse(queryset.pdf_cours, content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=%s' % queryset.pdf_cours
            return response
        elif type=="pdf_TD":
            queryset = Td.objects.get(titre=titre)
            response = HttpResponse(queryset.pdf_TD, content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=%s' % queryset.pdf_TD
            return response
        elif type=="pdf_TD_correction":
                queryset = Td.objects.get(titre=titre)
                response = HttpResponse(queryset.pdf_TD_correction, content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename=%s' % queryset.pdf_TD_correction
                return response
        elif type=="pdf_TP":
            queryset = Tp.objects.get(titre=titre)  
            response = HttpResponse(queryset.pdf_TP, content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=%s' % queryset.pdf_TP
            return response

@login_required(login_url='/login/')
def uploadcours(request,id):
    if request.method == "POST":
            a=Matiere.objects.get(id=request.POST["Appartient"])
            print(request.FILES['pdf_cours'])
            Cours.objects.create(titre=request.POST["titre"],description=request.POST["description"],pdf_cours=request.FILES['pdf_cours'],Appartient=a)

            return redirect('detail' ,id=id)
    else:
        form = PostCours()
    return render(request,'uploadcours.html',{'form':form,'id':id,'type':"Cours"})
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            a = User.objects.get(username=username)
            print(a)
            if ProfProfile.objects.filter(user=a):
                login(request, user)
                return redirect('matier' ,id=a.id)
            else:
                print(user)
                return HttpResponse("user not ok")
        else:
                return HttpResponse("user dont exist")                
    return render(request, 'registration/login.html')
@login_required(login_url='/login/')
def matier(request,id):

    matier = Matiere.objects.filter(prof=id)
    print(matier)

    return render(request,'matier.html',{'matier':matier})
@login_required(login_url='/login/')
def cour(request,id):

    Cor = Cours.objects.filter(Appartient=id)
    print(Cor)
    if not Cor :
        print("vide")
    else:
        print("not vide")

    return render(request,'cours.html',{'cour':Cor,'id':id})
@login_required(login_url='/login/')
def Tdd(request,id):

    Cor = Td.objects.filter(Appartient=id)
    print(Cor)
    if not Cor :
        print("vide")
    else:
        print("not vide")

    return render(request,'td.html',{'TD':Cor,'id':id})
@login_required(login_url='/login/')
def Tpp(request,id):

    Cor = Tp.objects.filter(Appartient=id)
    print(Cor)
    if not Cor :
        print("vide")
    else:
        print("not vide")

    return render(request,'tp.html',{'TP':Cor,'id':id})

@login_required(login_url='/login/')
def main(request):
    logout(request)
    return HttpResponseRedirect('/')

# Create your views here.
# @login_required(login_url='/login/')
@api_view(['GET'])
def myfiles(request ):
        parser_classes = ( MultiPartParser,)
        serializer_class = CoursSerializer
        if request.GET.get('type', None)=="cours":
            queryset = Cours.objects.get(titre=request.GET.get('titre', None))  
            response = HttpResponse(queryset.pdf_cours, content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=%s' % queryset.pdf_cours
            return response
        elif request.GET.get('type', None)=="td":
            queryset = Td.objects.get(titre=request.GET.get('titre', None))
            if request.GET.get('pdf', None)=="pdf_TD":
                response = HttpResponse(queryset.pdf_TD, content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename=%s' % queryset.pdf_TD
                return response
            elif request.GET.get('pdf', None)=="pdf_TD_correction":
                response = HttpResponse(queryset.pdf_TD_correction, content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename=%s' % queryset.pdf_TD_correction
                return response
        elif request.GET.get('type', None)=="tp":
            parser_classes = ( MultiPartParser,)
            serializer_class = TpSerializer
            queryset = Tp.objects.get(titre=request.GET.get('titre', None))  
            response = HttpResponse(queryset.pdf_TP, content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=%s' % queryset.pdf_TP
            return response


        
class filiereview(viewsets.ModelViewSet):
    queryset = Filiere.objects.all()
    serializer_class = filierSerializer
class Matiereview(viewsets.ModelViewSet):
        queryset = Matiere.objects.all()
        serializer_class = MatiereSerializer
class Coursview(viewsets.ModelViewSet):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

class Tdview(viewsets.ModelViewSet):
    queryset = Td.objects.all()
    serializer_class = TdSerializer
class Tpview(viewsets.ModelViewSet):
    queryset = Tp.objects.all()
    serializer_class = TpSerializer



@api_view(['Get','Post'])
def detail_Prof(request):
        if request.method == "GET":
                prof=User.objects.get(id=request.GET.get('prof', None))
                d=ProfDserilizer(prof, many=False)
                return Response(d.data)
        if request.method == "Post":
                prof=User.objects.get(id=request.data['userid'])
                d=ProfDserilizer(prof, many=False)
                return Response(d.data)
class Matieredetails(viewsets.ViewSet):
    def list(self,request):
            if request.GET.get('filiere', None) is None :
                slug = request.GET.get('prof', None)
                queryset = Matiere.objects.filter(prof=slug)
            else :
                slug = request.GET.get('filiere', None)
                queryset = Matiere.objects.filter(filiere=slug)
            
            serializer_class = MatiereSerializer(queryset, many=True)
            if serializer_class.data == []:
                print('empty')
                return Response({'empty':'0'})
            else :
                return Response(serializer_class.data)
class Tpdetails(viewsets.ViewSet):
    def list(self,request):
       # if request.method == "GET":
            slug = request.GET.get('Appartient', None)
            queryset = Tp.objects.filter(Appartient=slug)
            serializer_class = TpSerializer(queryset, many=True)
            if serializer_class.data == []:
                print('empty')
                return Response({'empty':'0'})
            else :
                print(queryset)
                serializer_class = TpSerializer(queryset, many=True)
                return Response(serializer_class.data)
class Tddetails(viewsets.ViewSet):
    def list(self,request):
            slug = request.GET.get('Appartient', None)
            queryset = Td.objects.filter(Appartient=slug)
            serializer_class = TdSerializer(queryset, many=True)
            if serializer_class.data == []:
                print('empty')
                return Response({'empty':'0'})
            else :
                print(queryset)
                serializer_class = TdSerializer(queryset, many=True)
                return Response(serializer_class.data) 
        #(queryset, many = True)
class Test(viewsets.ViewSet):
    
    #permission_classes = (IsAuthenticated,)
    def list(self,request):
       # if request.method == "GET":
            slug = request.GET.get('Appartient', None)
            queryset = Cours.objects.filter(Appartient=slug)
            serializer_class = CoursSerializer(queryset, many=True)
            print(serializer_class.data)
            if serializer_class.data == []:
                print('empty')
                return Response({'empty':'0'})
            else :
                for i in range(len(serializer_class.data)):
                    # serializer_class.data[i]['pdf_cours']=
                    serializer_class.data[i]['pdf_cours']=str(queryset[i].pdf_cours)
                    print(serializer_class.data)
                return Response(serializer_class.data)
        #elif request.method == "POST":
            print("post")
        #elif request.method == "PUT":
            print("Put")
        #elif request.method == "DELETE":
            print("delete")
            #@action(detail=True, methods=['post'])
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import UserSerializer, RegisterSerializer




from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView



class RegisterprofAPI(generics.GenericAPIView):
    serializer_class = RegisterprofSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        a = User.objects.create_user(username=request.POST['username'],email= request.POST['email'],password= request.POST['password'],phone= request.POST['phone'])
        print(a)
        user = ProfProfile.objects.create(user=a)
        return Response({
        "user": "aded"
        })

class LoginprofAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = loginprofSerializer

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(user)
        a = User.objects.get(username=user)
        print(a)
        if ProfProfile.objects.filter(user=a):
            k=ProfProfile.objects.get(user_id=a.id)
            print("ok")
            print(k.user_id)
            return Response({
            "userid":k.user_id
            })
        else :
            return Response({
            "non_field_errors": [
        "prof dont exist"
    ]
            })



class RegisteruserAPI(generics.GenericAPIView):
    serializer_class = RegisteruserSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        a = User.objects.create_user(username=request.POST['user.username'],email= request.POST['user.email'],password= request.POST['user.password'],NNI= request.POST['user.NNI'])
        print(a)
        b = Filiere.objects.get(id=request.POST['id_filiere'])
        print(b)
        user = EtudientProfile.objects.create(user=a,id_filiere=b)
        print(user)
        return Response({
        "token": "aded"
        })

class LoginuserAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = loginuserSerializer

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['username']
        a = User.objects.get(username=user)
        print(a)
        if EtudientProfile.objects.filter(user=a):
            k=EtudientProfile.objects.get(user=a)
            print(k.id_filiere.nom_Filiere)
            return Response({
            "nom_Filiere":k.id_filiere.id,
            "fname":a.first_name,
            "lname":a.last_name,
            "NNI":a.NNI,
            })
        else:
            print(user)
            return Response({
            "non_field_errors": [
        "student dont exist"
    ]
            })
from django.shortcuts import get_object_or_404 
class update(generics.GenericAPIView):
    serializer_class = updateseriliser
    def post(self, request):
                username=request.POST['username']
                fname=request.POST['first_name']
                lname=request.POST['last_name']
                myuser=get_object_or_404(User,username=username)
                myuser.first_name=fname 
                myuser.last_name=lname
                myuser.username=username
                myuser.save()
                return Response({
                "ok": [
            "Your account has been updated successfully"
        ]
                })
                
