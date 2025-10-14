from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .forms import SignUpForm # import signup มา
#import autencation form มาอันนี้ django ให้มาเป็นฟอร์มสำเร็จ
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
#import การใช้งานพร้อมเปลี่ยนชื่อไม่ให้มันซ้ำกันเดี๋ยวทำงานไม่ได้
from django.contrib.auth import authenticate , login as auth_login , logout as auth_logout 
from .models import Item,BorrowRequest  # เราไป import Item มาจากไฟล์ models เพื่อมาเรียกใช้งาน



# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request,"index.html",context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                messages.success(request, f"Welcome back ,{username}")
                return redirect('user')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request,"login.html", {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for {username}! You can now log in')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, "signup.html", {'form': form})

#รายละเอียดสิ่งของจะอยู่หน้านี้
def item_detail(request,item_id):
    item = get_object_or_404(Item, id = item_id)
    return render(request, "item_detail.html",{'item': item})

# อันนี้คือจะให้แค่ผู้ใช้งานที่ลงชื่อเข้าใช้เท่านั้นที่จะยืมของได้ ไม่งั้นจะโผล่ไปหน้าล็อคอิน
@login_required
def created_borrow_request(request,item_id):
    item = get_object_or_404(Item ,id=item_id)

    if request.method == "POST":
        form = BorrowRequestForm(request.POST)
        if form.is_valid():
            request_obj = form.save(commit=False)

            request_obj.requeter = request.user
            request_obj.item = item

            request_obj.save()
            messages.success(request,f'ส่งคำขอการยืม "{item.name}" เรียบร้อยแล้ว รอการอนุมัติ')
            return redirect('user_stautus')

# สถานะสำหรับผู้ใช้งาน
@login_required
def user_status(request):
    my_request = BorrowRequest.objects.filter(requester=request.user).order_by('-request_date')
    context = {'my_request': my_request}
    return render(request, 'user_status.html',context)

@login_required
def cancle_request(request, request_id):
    request_obj = get_object_or_404(
        BorrowRequest,
        id = request_id,
        requester = request.user,
        status = 'PENDING'
    )

    if request.method == 'POST':
        request_obj.status = 'CANCELLED'
        request_obj.save()
        messages.success(request,'ยกเลิกการยืมสำเร็จ')
    else:
        messages.warning(request,'กรุณายกเลิกผ่านฟอร์ม')
    
    return redirect('user_status')


@login_required
def user(request):
    return render(request,"user.html")
