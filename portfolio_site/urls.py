from django.contrib import admin
from django.urls import path, include 
from portfolio import views
#from blog import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('',views.home, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)