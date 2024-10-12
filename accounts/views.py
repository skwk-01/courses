from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # フォームのデータからユーザーを作成
            auth_login(request, user)  # 自動的にログイン
            return redirect('home')  # ホームにリダイレクト
    else:
        form = UserRegisterForm()  # 空のフォームを作成
    return render(request, 'accounts/register.html', {'form': form})

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/account_confirm_delete.html'
    success_url = reverse_lazy('accounts:login')

    def get_object(self):
        return self.request.user
    
@login_required
def account_setting(request):
    return render(request, 'accounts/account_setting.html', {'user': request.user})

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy('accounts:password_change_done')