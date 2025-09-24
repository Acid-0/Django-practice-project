from .views import view_post,view_get, view_get_all
from django.urls import path

urlpatterns = [
    # path('', admin.site.urls),
	path('post', view_post ),
	path('get', view_get ),
	path('get-all', view_get_all ),
]