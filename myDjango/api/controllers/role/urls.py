from .controller import post,get, get_all, deleteById
from django.urls import path

urlpatterns = [
    # path('', admin.site.urls),
	path('post', post ),
	path('get', get ),
	path('get-all', get_all ),
	path('delete', deleteById ),
]