from io import BytesIO

import weasyprint
from celery import task
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

from order.models import Order


# Create aysnc task in here

@task
def order_payment_success(order_id):
    """
    Task to send an e-mail notification when order is successfully paid
    """
    order = Order.objects.get(pk=order_id)
    subject = 'Congrations!! Your order {} has been paid sucessfully.'.format(order.id)
    message = 'Dear {}, \n\n The order {} has been paid successfully\
        we will process this order and deliver it to your hands soon'.format(order.order_receiver_name, order.id)
    email = EmailMessage(subject, message, 'admin@shopsite.com', [order.order_email, order.owner.mail])
    #generate PDF
    html = render_to_string('order/order_pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATICFILES_DIRS[0] + 'css/pdf_print.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach('order_{}.pdf'.format(order.id), out.getvalue(), 'application/pdf')
    return email

@task
def order_payment_pending(order_id):
    """
    Task to send an e-mail notification when order is waiting for a payment
    """
    order = Order.objects.get(pk=order_id)
    subject = 'Attentions!! Your order {} is still waiting for your payment.'.format(order.id)
    message = 'Dear {}, \n\n The order {} is still waiting for your payment\
                       Please pay this order within 15 mins, otherwise this order will\
                       be automatically deleted'.format(order.order_receiver_name, order.id)
    email = send_mail(subject, message, 'admin@shopsite.com', [order.order_email, order.owner.mail])
    return email