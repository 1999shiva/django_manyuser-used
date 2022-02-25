from django import views
from django.urls import path
from Usercreation.views import  Register_Users,login_user,OrganizationView,CampignsView

urlpatterns = [
    path('login/', login_user),
    path('register/', Register_Users),
    path('organization/',OrganizationView.as_view()),
    path('campigns/<str:Email_Address>',CampignsView,name="Listofcampigns"),
]

