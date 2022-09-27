from django.urls import path
from .views import user_obj, user_obj
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('users/',include('users.urls'))
    path('' ,user_obj,name='users' ),
   
]


