from django.shortcuts import render
from .models import Department
from accounts.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def department_list(request):
    department = get_object_or_404(Department)
    return render(request, 'department/list.html',
                    {'department':department})

@login_required
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    users = User.objects.filter(department_id=department.id, is_active=True,
                group_id=3)
    return render(request, 'department/department_detail.html',
                            {'pk':pk,
                            'department':department,
                            'users':users})
