from django.core.mail import send_mail
from django.contrib.auth.models import User


def send_sale_alert_email(user, product):
    subject = f"The artwork {product.name} is now on sale!"
    message = (
        f"Hi {user}, "
        f"You put '{product.name}' on your wishlist, and now "
        "it is on sale! Buy it at a discount whilst stocks last, "
        "at https://eponymous-bosch-b9b71a6bff59.herokuapp.com/wishlist/.")
    recipient_list = [user.email]
    send_mail(subject, message, 'sales@eponymousbosch.com', recipient_list)
