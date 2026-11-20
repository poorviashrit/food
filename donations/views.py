from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.db.models import Q
from .models import Donation

class FoodBridgeLoginView(LoginView):
    template_name = 'donations/login.html'
    redirect_authenticated_user = True

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Your account has been created. Welcome to FoodBridge!')
        return redirect('home')
    return render(request, 'donations/register.html', {'form': form})

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('home')
    return render(request, 'donations/logout.html')

def home(request):
    items = Donation.objects.all()
    q = request.GET.get('q','').strip()
    category = request.GET.get('category','')
    status = request.GET.get('status','all')
    if q: items = items.filter(Q(food_name__icontains=q)|Q(pickup_location__icontains=q)|Q(donor_name__icontains=q))
    if category: items = items.filter(category=category)
    if status != 'all': items = items.filter(status=status)
    all_items = Donation.objects.all()
    return render(request,'donations/home.html',{'donations':items,'q':q,'category':category,'status':status,'categories':Donation.CATEGORIES,'total':all_items.count(),'available':all_items.filter(status='Available').count(),'claimed':all_items.filter(status='Claimed').count(),'collected':all_items.filter(status='Collected').count()})

@login_required
@require_POST
def create_donation(request):
    fields = ['donor_name','food_name','category','quantity','pickup_location','contact','best_before']
    if any(not request.POST.get(x,'').strip() for x in fields):
        messages.error(request,'Please complete all required fields.')
        return redirect('home')
    Donation.objects.create(**{x:request.POST[x].strip() for x in fields},notes=request.POST.get('notes','').strip())
    messages.success(request,'Thank you! Your donation is now listed.')
    return redirect('home')

@login_required
@require_POST
def claim_donation(request,pk):
    item=get_object_or_404(Donation,pk=pk)
    if item.status=='Available':
        item.status='Claimed'; item.save(update_fields=['status'])
    return redirect('home')

@login_required
@require_POST
def mark_collected(request,pk):
    item=get_object_or_404(Donation,pk=pk)
    if item.status=='Claimed':
        item.status='Collected'; item.save(update_fields=['status'])
    return redirect('home')

@login_required
@require_POST
def delete_donation(request,pk):
    get_object_or_404(Donation,pk=pk).delete()
    messages.success(request,'Donation listing deleted.')
    return redirect('home')
