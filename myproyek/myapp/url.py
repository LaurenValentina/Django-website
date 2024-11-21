# from django.urls import path
# from . import views
# from django.contrib.auth.views import LoginView
# from django.contrib.auth.views import LogoutView

# #urlpatterns = [
# #    path('', views.hello_world, name='hello_world'),
# #]
# # from .views import register_user

# urlpatterns = [
#     # path('', views.halaman_utama, name='halaman_utama'),
#     path('halo/', views.my_view, name='my_view'),
#     path('produk_create/', views.produk_create, name='produk_create'),
#     path('daftar_produk/', views.daftar_produk, name='daftar_produk'),
#     path('tambah_produk/', views.tambah_produk, name='tambah_produk'),
#     path('kelola_produk/', views.kelola_produk, name='kelola_produk'),

#     # path('register/', register_user, name='register'),

# ]


# Import necessary modules
from django.contrib import admin  # Django admin module
from django.urls import path       # URL routing
from myapp.views import  * # Import views from the authentication app
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving

# Define URL patterns
urlpatterns = [
    path('home/', home, name="recipes"),      # Home page
    path("admin/", admin.site.urls),          # Admin interface
    path('login/', login_page, name='login_page'),    # Login page
    path('register/', register_page, name='register'),  # Registration page
]

# Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
