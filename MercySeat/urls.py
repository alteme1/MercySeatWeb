from django.urls import path, include
from .views import Home

urlpatterns = [
    # Uncomment the next line to enable the admin:    
    path('', Home.as_view(), name='home')
    #path('admin/', admin.site.urls)
]

