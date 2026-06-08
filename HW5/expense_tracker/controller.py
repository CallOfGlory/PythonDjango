from .models import Expense
from django.db.models import Sum


class ExpenseController:
    @staticmethod
    def add_expense(name, amount, category, description=''):
        expense = Expense.objects.create(
            name=name,
            amount=amount,
            category=category,
            description=description
        )
        return expense

    @staticmethod
    def delete_expense(expense_id):
        try:
            expense = Expense.objects.get(id=expense_id)
            expense.delete()
            return True
        except Expense.DoesNotExist:
            return False

    @staticmethod
    def get_all_expenses():
        return Expense.objects.all().order_by('-date')

    @staticmethod
    def get_total_expenses():
        total = Expense.objects.aggregate(total=Sum('amount'))['total']
        return total if total else 0
