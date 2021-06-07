"""restproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from school import views,teacher,calculate,studentsresult,login,authlogin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from knox import views as knox_views

#router=routers.DefaultRouter()
#router.register(r'school',views.studentslist)

urlpatterns = [
    #path('',include('school.urls')),
    path('admin/', admin.site.urls),
   # path('', include(router.urls)),
    path('', views.studentslist),
    path('delete/<int:pk>', views.studentdetail),
    # path('search/<str:s_name>',views.studentbyname),
    path('search/',views.sear.as_view()),
    path('year',views.yearview),
    path('months/<str:nam>',views.monthsview),
    path('paymonth/<int:roll>/<int:yerr>',views.updateview),
    path('teacher',teacher.teacheroverall),
    path('searchteacher/',teacher.searchteacher.as_view()),
    path('tpayment/<str:tnam>',teacher.teacherpaymentview),
    path('tupdate/<str:tnam>/<int:tyear>/<int:pk>',teacher.updateteacherpayments),
    path('calc/<int:year>',calculate.allmoneyfromstudents),
    path('result/<int:sroll>',studentsresult.getstudentresult),
    path('postresult/<int:sroll>/<int:year>/<str:subject>/<str:sstandard>',studentsresult.postresult),
    path('subjects',studentsresult.getsubjects),
    path('standards',studentsresult.getstandards),
    path('subjectsbyid/<int:pk>',studentsresult.getsubjectsbyid),
    path('standardsbyid/<int:pk>',studentsresult.getstandardsbyid),
    
    #path('login/<str:usernam>/<slug:passw>', login.login),
    path('register', authlogin.RegisterAPI.as_view(), name='register'),
    path('login', authlogin.LoginAPI.as_view(), name='login'),
    path('logout', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),
     

    
    
    
]
urlpatterns = format_suffix_patterns(urlpatterns)