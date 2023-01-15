from django.contrib import admin
from django.urls import path, include 
from api import views
from rest_framework import routers
from django.views.generic.base import TemplateView
router = routers.DefaultRouter(trailing_slash=False)
router.register('matieredetails/$', views.Matiereview)
router.register('coursedetails/$', views.Test,'b')
router.register('tddetails/$', views.Tddetails,'td')
router.register('tpdetails/$', views.Tpdetails,'tp')
router.register('matierdetails/$', views.Matieredetails,'matier')
router.register('td', views.Tdview,'proftd')
router.register('tp', views.Tpview,'proftp')
router.register('filiere', views.filiereview,'proftp')
router.register('ajoutcours', views.Coursview,'ajout')

urlpatterns = [
    path('api', include(router.urls)), 
    # path('admin/', admin.site.urls),
    path('prof/', views.detail_Prof),
    path('ak/', views.myfiles),
    path('etd/update/', views.update.as_view(), name="Update"),
    path('prof/register/', views.RegisterprofAPI.as_view(), name='registerprof'),
    path('prof/login/', views.LoginprofAPI.as_view(), name='registerprof'),
    path('etd/register/', views.RegisteruserAPI.as_view(), name='registeretd'),
    path('etd/login/', views.LoginuserAPI.as_view(), name='registerprof'),

    path("", TemplateView.as_view(template_name="home.html"), name="home"),
        path("detail/<int:id>/", views.cour, name="detail"),
        path("detail/<int:id>/<str:titre>/<str:type>", views.edit_post, name="modifier"),
        
        path("detaildel/<int:id>/<str:titre>/<str:type>", views.delete_post, name="supprimer"),
        path("detailTD/<int:id>/", views.Tdd, name="detailTD"),
        path("detailTP/<int:id>/", views.Tpp, name="detailTP"),
         path("detail/<int:id>/uploadcours", views.uploadcours, name="uploadcours"),
         path("detailTD/<int:id>/uploadTD", views.uploadTD, name="uploadTD"),
         path("detailTP/<int:id>/uploadTP", views.uploadTP, name="uploadTP"),
    path('Logou/', views.main,name="logout"),
    path('login/', views.login_user,name="login"),
    path('matier/<int:id>/', views.matier,name="matier"),
    path('download/<str:type>/<str:titre>', views.download,name="download"),

    path('admin/', views.admin,name="admin"),
    path('adminetd/', views.adminetd,name="adminetd"),
       path('adminfil/', views.adminfil,name="adminfil"),
    path("proff/", views.uploadproff, name="uploadprof"),
     path("etdd/", views.uploadetdd, name="uploadetd"),
     path("fil/", views.uploadfil, name="uploadfil"),
    path("del/<int:id>/<str:type>", views.delete_prof, name="deleteadmin"),
    path("modif/<int:id>/<str:type>", views.edit_prof, name="modifieradmin"),
]

