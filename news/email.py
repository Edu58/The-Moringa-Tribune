from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_welcome_email(name, receiver):
    subject = 'Welcome to the Moringa Tribune Newletter'
    sender = 'edwin@moringaschool.com'

    text_content = render_to_string('news/news-email.txt', {'name', name}, ctx)
    html_context = render_to_string('news/news-email.html', {'name', name}, ctx)

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_context, 'text/html')
    msg.send()
