from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.core.mail import send_mail
from django.conf import settings

from cart.forms import CartAddProductForm
from .models import Member, Product, Game
from .forms import BackCallForm


def index(request):
    return render(request, 'savage_bcw/main.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'savage_bcw/about.html')


class ProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'savage_bcw/product/product.html', context)


class SelectedProductView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        cart_product_form = CartAddProductForm()
        context = {'product': product, 'cart_product_form': cart_product_form}
        return render(request, 'savage_bcw/product/selected-product.html', context)


class BackCallView(View):
    def get(self, request):
        form = BackCallForm()
        context = {'form': form}
        return render(request, 'savage_bcw/back-call.html', context)

    def post(self, request):
        if request.method == 'POST':
            form = BackCallForm(request.POST)
            if form.is_valid():
                firstname = request.POST.get('firstname')
                lastname = request.POST.get('lastname')
                email = request.POST.get('email')
                theme = request.POST.get('theme')
                text = request.POST.get('text')
                fullname = f'{firstname} {lastname}'
                send_mail(subject=theme, message=text, from_email=email, recipient_list=[settings.EMAIL_HOST_USER,])
                return redirect('home')
            else:
                return HttpResponse('invalid data')


class TeamView(View):
    def get(self, request):
        members = Member.objects.all()
        context = {'members': members}
        return render(request, 'savage_bcw/team/members.html', context)


class GameView(View):
    def get(self, request):
        games = Game.objects.all()
        context = {'games': games}
        return render(request, 'savage_bcw/team/teams.html', context)


class SelectedGameView(View):
    def get(self, request, game_id):
        game = get_object_or_404(Game, pk=game_id)
        members = Game.objects.get(pk=game_id).member.all()
        context = {'game': game, 'members': members}
        return render(request, 'savage_bcw/team/selected-game.html', context)


