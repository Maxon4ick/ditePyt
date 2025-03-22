import asyncio

import telegram
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from OnlineStore.settings import TELEGRAM_CHAT_ID, TELEGRAM_TOKEN
from cart.views import Cart
from .forms import OrderCreateForm
from .models import Order, OrderItem, ShippingAddress


@login_required
def checkout(request):
    """
    Представление чекаута.
    """
    cart = Cart.objects.get(user=request.user)
    form = OrderCreateForm()
    context = {'cart': cart, 'form': form}

    return render(request, 'checkout/checkout.html', context)


async def send_telegram_message(message):
    """
    Асинхронная функция для отправки сообщения в ТГ.
    """
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    chat_id = TELEGRAM_CHAT_ID
    await bot.send_message(chat_id=chat_id, text=message)



@login_required
def thank_you(request, order_id):
    """
    Страница благодарности за заказ.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)

    # Отравка в TG уведомления о заказе
    # Отпрака сообщения
    message = f" Новый заказ \nСостав заказа \n"
    for item in order.items.all():
        message += f"{item.quantity} x {item.item.title}\n"
    message += f"Привезти по адресу:\n{order.shipping_address}\n"
    asyncio.run(send_telegram_message(message))

    return render(request, 'checkout/thank_you.html', {'order': order})


@login_required
def create_order(request):
    """
    Создание экземпляров Order и ShippingAddress
    из формы и редирект в профиль пользователя,
    либо передаем форму обратно.
    """
    cart = get_object_or_404(Cart, user=request.user)

    if cart.items.exists() and request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                payment_method=form.cleaned_data['payment_method'],
                user=request.user,
            )

            ShippingAddress.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                address_line_1=form.cleaned_data['address_line_1'],
                address_line_2=form.cleaned_data['address_line_2'],
                order=order,
            )

            for cart_item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    item=cart_item.item,
                    quantity=cart_item.quantity,
                    price=cart_item.item.price
                )

            cart.clear()
            return redirect('checkout:thank_you', order_id=order.id)
    else:
        form = OrderCreateForm()
    messages.warning(
        request, 'Форма не была корректно обработана, введите данные еще раз')
    context = {'form': form, 'cart': cart}
    return render(request, 'checkout/checkout.html', context)
