from django.core.management import BaseCommand

from studyhub.models import Payment


class Command(BaseCommand):
    """
    Команда для заполнения базы данных Payment
    """

    def handle(self, *args, **options):
        payment_data = [
            {"payment_amount": 1000,
             "paid_course": 1,
             },
            {"payment_amount": 2000,
             "paid_course": 2,
             },
            {"payment_amount": 3000,
             "paid_course": 3,
             },
            {"payment_amount": 4000,
             "paid_course": 4,
             },
        ]

        payment_for_create = []

        for data in payment_data:
            payment_for_create.append(Payment(**data))

        Payment.objects.bulk_create(payment_for_create)
