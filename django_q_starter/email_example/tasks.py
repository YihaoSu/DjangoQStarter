from django.core.mail import send_mail
from django.contrib.auth.models import User


def get_superuser_email_list():
    superuser_obj = User.objects.filter(is_superuser=True)
    email_list = [obj.email for obj in superuser_obj]
    return email_list


def send_test_email_to_superuser():
    """
    用來寄發測試信件給superuser。
    Django Q要填的欄位值:
    Func：django_q_starter.email_example.tasks.send_test_email_to_superuser
    Args：無
    """
    subject = '「測試信件」測試是否能正常發送信件'
    html_message = '測試是否能正常發送信件'
    email_list = get_superuser_email_list()
    print(email_list)

    response = send_mail(
        subject,
        '',
        'DjangoQStarter',
        email_list,
        fail_silently=False,
        html_message=html_message
    )
    print(response)
