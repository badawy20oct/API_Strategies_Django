from django.contrib import admin
from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter
from .views import viewsetsBook

router = DefaultRouter()
router.register(r'books' , views.viewsetsBook)




urlpatterns = [

    #1 Pure Django Json No Model 
    path('django/PureDjanogJsonNoMdel' , views.Pure_Json),

    #2 Pure Django Json With Model 
    path('django/PureDjanogJsonWithModel' , views.Pure_Json_Model),
    
    #3 RESTFramework FBV 
        #list
    path('rest/fbv/list' , views.fbv_list),
        #pk 
    path('rest/fbv/<int:pk>' , views.fbv_pk),
    


    #4 RESTFramework CBV 
        #list
    path('rest/cbv/list' , views.cbv_list.as_view()),
        #pk 
    path('rest/cbv/<int:pk>' , views.cbv_pk.as_view()),



    #5 RESTFramework Mixins 
        #list
    path('rest/mixins/list' , views.mixins_list.as_view()),
        #pk 
    path('rest/mixins/<int:pk>' , views.mixins_pk.as_view()),


    #6 RESTFramework Generics 
    path('rest/generics/list' , views.generics_list.as_view()),
    path('rest/generics/<int:pk>' , views.generics_pk.as_view()),


    

    #6 RESTFramework ViewSet
    path('rest/viewset/' ,include(router.urls)),
    
]
