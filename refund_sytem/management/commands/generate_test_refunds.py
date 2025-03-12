import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from refund_sytem.models import CustomUser, RefundRequest


class Command(BaseCommand):
    help = "Создает 20 случайных запросов на возврат с разными датами"

    def handle(self, *args, **kwargs):
        status_choices = ["pending", "approved", "rejected"]
        account_type_choices = ["business", "private"]

        user = CustomUser.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR("Не найден ни один пользователь в базе!"))
            return

        for i in range(20):
            status = random.choice(status_choices)
            account_type = random.choice(account_type_choices)

            # Генерируем случайную дату за последние 30 дней
            random_days = random.randint(0, 30)
            order_date = date.today() - timedelta(days=random_days)

            refund_request = RefundRequest.objects.create(
                user=user,
                order_number=f"ORD{i + 1}",
                order_date=order_date,
                first_name=f"FirstName{i + 1}",
                last_name=f"LastName{i + 1}",
                phone_number=f"+1{random.randint(1000000000, 9999999999)}",
                email=f"user{i + 1}@example.com",
                country="CountryExample",
                address="123 Some St",
                postal_code="12345",
                city="CityName",
                products="Product1, Product2",
                reason="Refund request reason",
                bank_name="BankNameExample",
                account_type=account_type,
                iban=f"IBAN{random.randint(1000000000000000, 9999999999999999)}",
                iban_verified=random.choice([True, False]),
                status=status,
            )

            self.stdout.write(self.style.SUCCESS(
                f"Created refund request #{refund_request.id} "
                f"for user {user.username} with status {status}, "
                f"account type {account_type}, order date {order_date}"
            ))
