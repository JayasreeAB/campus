from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from .models import MaintenanceRequest

from .forms import MaintenanceForm,RegisterForm



def home(request):

    return render(request,'home.html')



def register(request):

    if request.method=="POST":

        form=RegisterForm(request.POST)

        if form.is_valid():

            user=form.save(commit=False)

            user.set_password(
                form.cleaned_data['password']
            )

            user.save()

            return redirect('login')

    else:
        form=RegisterForm()


    return render(
        request,
        'register.html',
        {'form':form}
    )



def user_login(request):

    if request.method=="POST":

        username=request.POST['username']

        password=request.POST['password']


        user=authenticate(
            username=username,
            password=password
        )


        if user:

            login(request,user)

            return redirect('my_requests')


    return render(request,'login.html')




def user_logout(request):

    logout(request)

    return redirect('login')





@login_required
def submit_request(request):

    if request.method=="POST":

        form=MaintenanceForm(request.POST)

        if form.is_valid():

            obj=form.save(commit=False)

            obj.user=request.user

            obj.save()

            return redirect('my_requests')


    else:

        form=MaintenanceForm()


    return render(
        request,
        'submit_request.html',
        {'form':form}
    )




@login_required
def my_requests(request):

    requests=MaintenanceRequest.objects.filter(
        user=request.user
    )


    category=request.GET.get('category')

    status=request.GET.get('status')

    priority=request.GET.get('priority')


    if category:
        requests=requests.filter(
            category=category
        )

    if status:
        requests=requests.filter(
            status=status
        )

    if priority:
        requests=requests.filter(
            priority=priority
        )


    return render(
        request,
        'my_requests.html',
        {'requests':requests}
    )





@login_required
def update_request(request,id):

    obj=get_object_or_404(
        MaintenanceRequest,
        id=id,
        user=request.user
    )


    form=MaintenanceForm(
        instance=obj
    )


    if request.method=="POST":

        form=MaintenanceForm(
            request.POST,
            instance=obj
        )

        if form.is_valid():

            form.save()

            return redirect('my_requests')


    return render(
        request,
        'submit_request.html',
        {'form':form}
    )





@login_required
def delete_request(request,id):

    obj=get_object_or_404(
        MaintenanceRequest,
        id=id,
        user=request.user
    )

    obj.delete()

    return redirect('my_requests')





@login_required
def admin_dashboard(request):

    requests=MaintenanceRequest.objects.all()


    if request.method=="POST":

        id=request.POST['id']

        status=request.POST['status']


        obj=MaintenanceRequest.objects.get(
            id=id
        )

        obj.status=status

        obj.save()


    return render(
        request,
        'admin_dashboard.html',
        {'requests':requests}
    )