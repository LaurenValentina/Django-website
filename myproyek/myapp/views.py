from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produk
from .forms import ProdukForm

def hello_world(request):
    return HttpResponse("Hello, World!")

def daftar_produk(request):
    produk = Produk.objects.all()  # Mengambil semua data produk
    return render(request, 'nama_aplikasi/daftar_produk.html', {'produk': produk})

def halaman_utama(request):
    return render(request, 'halaman_utama.html', {})

def my_view(request):
    return HttpResponse("Halo, ini adalah tanggapan dari server!")
# Create your views here.

def produk_create(request):
    # Buat instance ProdukForm tanpa menangani POST
    form = ProdukForm()
    return render(request, 'produk_form.html', {'form': form})

def daftar_produk(request):
    produk = Produk.objects.all()  # Mengambil semua data produk
    return render(request, 'daftar_produk.html', {'produk': produk})

def tambah_produk(request):
    if request.method == 'POST':  # Memeriksa apakah request adalah POST
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()  # Menyimpan data ke database
            return redirect('daftar_produk.html')  # Redirect ke halaman daftar produk
    else:
        form = ProdukForm()  # Membuat form kosong untuk GET request
    return render(request, 'tambah_produk.html', {'form': form})    

# views.py
def kelola_produk(request, produk_id=None):
    if produk_id:  # Jika ada ID produk, ambil data untuk pengeditan
        produk = Produk.objects.get(id=produk_id)
        form = ProdukForm(instance=produk)
    else:
        produk = None
        form = ProdukForm()

    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('daftar_produk')

    return render(request, 'kelola_produk.html', {'form': form})



# from django.shortcuts import render, redirect
# from .forms import UserForm

# def register_user(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()  # Simpan user ke database
#             return redirect('login')  # Redirect ke halaman login setelah berhasil
#     else:
#         form = UserForm()
#     return render(request, 'register.html', {'form': form})


# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

# Define a view function for the home page
def home(request):
    return render(request, 'home.html')

# Define a view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/home/')
    
    # Render the login page template (GET request)
    return render(request, 'login.html')

# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
        
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')
    
    # Render the registration page template (GET request)
    return render(request, 'register.html')

