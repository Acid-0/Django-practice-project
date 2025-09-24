from django.urls import path,include

urlpatterns = [
    # path('', admin.site.urls),
	path('user/',include('api.controllers.user.urls'))
]