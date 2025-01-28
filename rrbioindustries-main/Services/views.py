from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import StockList, Member, Attendance ,Salary
from django.utils.timezone import now 
from datetime import datetime
from .forms import AttendanceForm, MemberForm
from django.utils.dateparse import parse_date


def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect("login")

    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required
def home(request):
    if request.user.is_anonymous:
        data = {
            'title': "RR BIO INDUSTRIES"
        }
        return redirect("home", data)
    return render(request, "home.html")


@login_required
def credit_note(request):
    return render(request, "credit_note.html")


@login_required
def stock(request):
    return render(request, "stock.html")


@login_required
def invoice(request):
    return render(request, "invoice.html")



@login_required
def stock_list(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        opening = float(request.POST.get('opening', 0))
        daily_use = float(request.POST.get('daily_use', 0))
        balance = opening - daily_use

        stock = StockList(date=date, opening=opening, daily_use=daily_use, balance=balance)
        stock.save()

        return redirect('stock')

    today_date = datetime.today().strftime('%Y-%m-%d')

    return render(request, "stock.html", {'today_date': today_date})



@login_required
def attendance_form(request):
    members = Member.objects.all()
    if request.method == 'POST':
        for member in members:
            date_str = request.POST.get(f'date_{member.id}')
            time_in_str = request.POST.get(f'time_in_{member.id}')
            time_out_str = request.POST.get(f'time_out_{member.id}')
            attendance_status = request.POST.get(f'attendance_{member.id}')

            date = parse_date(date_str)
            if attendance_status == 'present':
                # Only record time_in and time_out if present
                time_in = time_in_str
                time_out = time_out_str
                present = True

                Attendance.objects.create(
                    member=member,
                    date=date,
                    time_in=time_in,
                    time_out=time_out,
                    present=present
                )
            elif attendance_status == 'absent':
                # Don't record time_in and time_out if absent
                Attendance.objects.create(
                    member=member,
                    date=date,
                    present=False
                )
        
        return redirect('attendance_form')  # Redirect back to the form after submission

    return render(request, 'attendance_form.html', {'members': members})


@login_required
def salary_page(request):
    current_month = now().date().replace(day=1)
    daily_wage = 100  # This can be fetched from Member model if needed
    members = Member.objects.all()

    salaries = []
    for member in members:
        salary = calculate_salary(member, current_month, daily_wage)
        salaries.append(salary)

    return render(request, 'salary_page.html', {'salaries': salaries})
@login_required
def salary_page(request):
    # Get the current month
    current_month = now().date().replace(day=1)

    # Define the daily wage for the calculation (could be part of member data)
    daily_wage = 100  # For example, $100 per day

    # Get all members
    members = Member.objects.all()

    # Calculate salary for each member
    salaries = []
    for member in members:
        salary = calculate_salary(member, current_month, daily_wage)
        salaries.append(salary)

    return render(request, 'salary_page.html', {'salaries': salaries})






@login_required
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # Check if the user already exists
            if User.objects.filter(username=name).exists():
                return render(request, 'add_member.html', {'form': form, 'error': 'User already exists!'})
            form.save()
            return redirect('attendance_form')
    else:
        form = MemberForm()
    return render(request, 'add_member.html', {'form': form})


@login_required
def save_member(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        new_member = Member.objects.create(name=name)
        return redirect('attendance_form')

    return render(request, 'add_member.html')



@login_required
def check_member(request, member_name):
    try:
        member = Member.objects.get(name=member_name)
        return JsonResponse({'exists': True})
    except Member.DoesNotExist:
        return JsonResponse({'exists': False})



@login_required
def daily_production(request):
    return render(request, "daily_production.html")

@login_required
def raw(request):
    return render(request, "raw.html")




