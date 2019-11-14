from django.shortcuts import render, get_object_or_404
from .models import par
# Create your views here.
def par_das(request):
    parent_user=get_object_or_404(par, user=request.user)
    stud=parent_user.stu.all()
    return render(request, 'dash.html', {'student':stud})
