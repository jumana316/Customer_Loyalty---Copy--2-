# import pandas as pd
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import get_user_model
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from Dashboard.models import SaleAnalysis, ProfitAnalysis, TrxnAnalysis
from django.contrib.auth  import login

from datetime import date, datetime
from dateutil.relativedelta import *

from django.views import generic

def LandingPage(request):
    return render(request, 'landing.html')

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = SignupForm
    
    def get_success_url(self):
        return reverse("Customer:login")


# @login_required(login_url='/')
# def dashboard_with_pivot(request):
#     return render(request, 'dashboard.html')

@login_required
def UserDashboard(request):  
    return render(request, 'dashboard.html')

@login_required(login_url='login')
def date_filter(request):
    total_sales = SaleAnalysis.objects.all()
    
    startDate = request.GET.get('StartDate')
    endDate = request.GET.get('EndDate')
    
    sales_data = total_sales.filter(add_date__range=[startDate, endDate])
    
    for x in sales_data:
        qs_user = x.user
        qs_sale = x.sale
        print (qs_user, qs_sale)

    context = {
        "startDate":startDate,
        "endDate":endDate,
        "total_sales":total_sales,
        "sales_data":sales_data,
    }
    return render(request, 'dashboard.html', context)
    
def RewardsPage(request):
    form = RewardAdminForm
    current_user = request.user
    print(current_user)
    rewards = Reward.objects.filter(username=current_user)
    current_points = Reward.points
    # reward_catalogs = RewardCatalog.objects.all()
    context = {
        'rewards': rewards,
        'current_points': current_points,
        # 'reward_catalogs': reward_catalogs,
        'form' : form
    }
    return render(request, 'rewards.html', context)

def redeem_reward(request):
    form = RewardAdminForm
    user = request.user
    reward_catalog_id = 1  # replace 1 with the desired reward catalog id
    reward = redeem_reward(user, reward_catalog_id)
    
    context = {
        'form': form
    }
    if reward:
        # return redirect('UserDashboard')
        return redirect('rewards.html', context)




















    # # Create instance of DateChoiceForm
    # form = DateChoiceForm()  
    # if request.method == "POST":
    #     form = DateChoiceForm(request.POST)
    #     if form.is_valid:
    #         datetime_range = form.cleaned_data.get('datetime_range_with_format')
    #         start_date = datetime_range.start.date()
    #         end_date = datetime_range.stop.date()
    #         end_date = end_date + relativedelta(days=-1)
            
    #         # Filter SaleAnalysis, ProfitAnalysis, and TrxnAnalysis models based on the custom date range
    #         sale_data = SaleAnalysis.objects.filter(date__range=[start_date, end_date])
    #         profit_data = ProfitAnalysis.objects.filter(date__range=[start_date, end_date])
    #         trxn_data = TrxnAnalysis.objects.filter(date__range=[start_date, end_date])
            
            
    #         print(sale_data)
    #         print(profit_data)
    #         print(trxn_data)
    #         # Render the dashboard view with the filtered data
    #         form.save()
            
    #         start_date = start_date.date()
    #         end_date = end_date + relativedelta(days=-1)
    #         end_date = end_date.date()
    #         context = {
    #             'form': form,
    #             'sale_data': sale_data,
    #             'profit_data': profit_data,
    #             'trxn_data': trxn_data,
    #         }
    # context = {
    #     'form': form,
    # }






    # form = DateChoiceForm()  
    # if request.method == "POST":
    #     form = DateChoiceForm(request.POST)
    #     if form.is_valid:
    #         datetime_range = form.cleaned_data.get('datetime_range_with_format')
    #         Sale_data = SaleAnalysis.objects.filter(datetime_range)
    #         Profit_data = SaleAnalysis.objects.filter(datetime_range)
    #         Trxn_data = SaleAnalysis.objects.filter(datetime_range)
    #         form.save()
            
    #         print(Sale_data)
    #         print(Profit_data)
    #         print(Trxn_data)
            
    #     context = {
    #             'form': form,
    #             'Sale_data': Sale_data,
    #             'Profit_data': Profit_data,
    #             'Trxn_data': Trxn_data,
    #         }
    #     return render(request, 'dashboard.html', context)





# def SignupPage(request):
#     form = SignupForm()
#     if request.method =="POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form.cleaned_data
#             return redirect("/")
#         else:
#             # Add an error message to the form if the passwords don't match
#             form.add_error('c_password', "Passwords do not match.")
#     context ={
#         "form": SignupForm()
#     }
#     return render(request, 'signup.html', context)


# @login_required 
# def LoginPage(request):
#     form = LoginForm()
#     if request.method =="POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             # email = form.cleaned_data['email']
#             phone = form.cleaned_data['phone']
#             password = form.cleaned_data['password']
# #             user = signup.objects.filter(phone=phone, password=password)
#             if user is not None:
#                 login(request, user)
#         return redirect('UserDashboard/')
#     context={
#         "form": LoginForm()
#     }
#     return render(request, 'login.html', context)











    # form = DateChoiceForm()
    # Start_date = request.POST.get('Start date')
    # End_date = request.POST.get('End date')
    # if 'form1' in request.POST:
    #         if form.is_valid():
    #             selectedDate1 = form.cleaned_data["Start date"]
    #             selectedDate2 = form.cleaned_data["End date"]
    #             start = datetime(selectedDate1)
    #             end = datetime(selectedDate2)
    #             filterYearMonth = CustomerDashboard.objects.filter(date__gte=start).filter(date__lte=end)

    #         else:
    #             filterYearMonth = CustomerDashboard.objects.all()

    # else:
    #     form = DateChoiceForm()
    #     filterYearMonth = CustomerDashboard.objects.all()

    # context = {
    #     'filterYearMonth': filterYearMonth,
    #     'form': form,
    # }

    # return render(request, 'dashboard.html', context)

















    # data_form = DateChoiceForm(request.GET or None)
    
    # if data_form.is_valid():
    #     date_range = data_form.cleaned_data['date_range']
        
    #     if date_range == 'today':
    #         start_date = datetime.now().date()
    #         end_date = start_date
    #     elif date_range == 'yesterday':
    #         end_date = datetime.now().date() - timedelta(days=1)
    #         start_date = end_date
    #     elif date_range == 'monthly':
    #         end_date = datetime.now().date()
    #         start_date = end_date.replace(day=1)
    #     elif date_range == 'yearly':
    #         end_date = datetime.now().date()
    #         start_date = end_date.replace(day=1, month=1)
    #     else:
    #         start_date = data_form.cleaned_data['start_date']
    #         end_date = data_form.cleaned_data['end_date']
        
    #     sale_data = SaleAnalysis.objects.filter(sale_date__range=[start_date, end_date])
    #     profit_data = ProfitAnalysis.objects.filter(profit_date__range=[start_date, end_date])
    #     txn_data = TrxnAnalysis.objects.filter(transaction_date__range=[start_date, end_date])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
# @login_required
# def LoginPage(request):
#     # form = LoginForm()
#     if request.method =="POST":
#         form = LoginForm(request.POST) 
#         if form.is_valid():
#             # email = form.cleaned_data['email']
#             u_email = form.cleaned_data.get('u_email')
#             password = form.cleaned_data.get('password')
#             # user = signup.objects.filter(u_email, password)
#             user = authenticate(request, u_email = u_email, password = password)
#             # user = signup.objects.filter(u_email=u_email, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f' welcome {u_email} !!')
#                 return redirect('UserDashboard')
#             else:
#                 messages.error(request, f'Invalid username or password.')
#         else:
#             messages.error(request, f'Invalid username or password.')
#     else:
#         form = LoginForm(initial={'request': request})
#     context={
#         "form": LoginForm()
#     }
#     return render(request, 'login.html', context)