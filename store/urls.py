from django.urls import path
from .views import index ,signup,login,cart
from Eshop import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index ,name='index'),
    path('signup/',signup ,name='signup'),
    path('login/',login,name="login"),
    path('cart/',cart,name='cart')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

