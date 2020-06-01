from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password


from shopify.settings import BASE_URL


class Affiliate(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    code = models.CharField(max_length=25, blank=False, null=False)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Affiliate, self).save(*args, **kwargs)


# Send email when a new affiliate is created
@receiver(post_save, sender=Affiliate)
def affiliate_created(sender, instance, created, **kwargs):
    login = instance.name.split()[0]
    c = {'login': login, 'password': instance.password, 'site': BASE_URL+"/affiliate-login"}
    html_content = render_to_string('email/to_affiliate.html', c)
    if created:
        send_mail(
            'Affiliate Login',
            None,
            ['fareskato@gmail.com'],
            [instance.email],
            fail_silently=False,
            html_message=html_content
        )