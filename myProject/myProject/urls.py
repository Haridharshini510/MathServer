from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('math/',views.power,name="math"),
    path('',views.power,name="mathroot")
]
