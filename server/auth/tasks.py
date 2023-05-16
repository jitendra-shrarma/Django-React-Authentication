# Import default modules
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User


# Send email to all user with image attachment
def send_email_to_all_users_task():
    subject = 'Good morning User!'
    message = 'This is a test email.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email for user in User.objects.all()]
    html_content = render_to_string('email_template.html', {})
    msg = EmailMultiAlternatives(subject, message, from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")

    # add tracking pixel to html content
    tracking_pixel_url = 'http://yourdomain.com/tracking_pixel.gif?email={}'.format(user_email)
    html_content_with_tracking = html_content.replace('</body>', '<img src="{}"></body>'.format(tracking_pixel_url))
    msg.attach_alternative(html_content_with_tracking, "text/html")

    # send email
    try:
        msg.send()
        return True
    except:
        return False

