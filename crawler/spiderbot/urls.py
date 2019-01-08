from django.urls import path, include
from . import views


from . import views
urlpatterns = [
                path('webpage', views.crawl_web_page,name='crawler'),
                

]