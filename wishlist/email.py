from django.core.mail import send_mail
from django.contrib.auth.models import User


def send_sale_alert_email(user, product):
    subject = f"The artwork {product.name} is now on sale!"
    message = (
        f"The product {product.name}, which is on your wishlist, "
        "is now on sale! Buy it at a discount whilst stocks last, "
        "at https://eponymous-bosch-b9b71a6bff59.herokuapp.com/")
    recipient_list = [user.email]
    send_mail(subject, message, 'eponymous_bosch@example.com', recipient_list)
