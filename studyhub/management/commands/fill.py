from django.core.management import BaseCommand

from studyhub.models import Payment, Course


class Command(BaseCommand):
    """
    Команда для заполнения базы данных Payment
    """

    def handle(self, *args, **options):
        payment_data = [
            {"payment_amount": 1000,
             "paid_course": Course.objects.get(pk=1),
             },
            {"payment_amount": 2000,
             "paid_course": Course.objects.get(pk=2),
             },
            {"payment_amount": 3000,
             "paid_course": Course.objects.get(pk=3),
             },
            {"payment_amount": 4000,
             "paid_course": Course.objects.get(pk=4),
             },
        ]

        payment_for_create = []

        for data in payment_data:
            payment_for_create.append(Payment(**data))

        Payment.objects.bulk_create(payment_for_create)
