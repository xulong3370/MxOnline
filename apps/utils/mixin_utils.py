# coding=utf-8
__author__ = 'lianzhiyu'
__date__ = '2017/6/21 20:20'


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# method_decorator 用于转换装饰器，使得其能在类中使用
class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)