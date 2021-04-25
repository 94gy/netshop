from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View

from userapp.models import UserInfo





class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        #获取请求参数
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd', '')

        #插入数据库
        user = UserInfo.objects.create(uname=uname, pwd=pwd)

        if user:
            #将用户对象存放在session对象中
            request.session['user'] = user
            return HttpResponseRedirect('/user/center')
        return HttpResponseRedirect("/user/register/")

class CheckUnameView(View):
    def get(self, request):
        uname = request.GET.get('uname', '')
        #根据用户名去数据库中查询
        userList = UserInfo.objects.filter(uname=uname)
        flag = False
        if userList:
            flag = True
        return JsonResponse({'flag':flag})


class CenterView(View):
    def get(self, request):
        return render(request, 'center.html')
    pass