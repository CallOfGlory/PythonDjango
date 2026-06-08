from django.shortcuts import render, redirect
from django.http import JsonResponse
from .controller import ExpenseController


def expense_list(request):
    expenses = ExpenseController.get_all_expenses()
    total = ExpenseController.get_total_expenses()
    return render(request, 'expense_tracker/expense_list.html', {
        'expenses': expenses,
        'total': total
    })


def add_expense(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        description = request.POST.get('description', '')

        ExpenseController.add_expense(name, amount, category, description)
        return redirect('expense_list')

    return render(request, 'expense_tracker/add_expense.html')


def delete_expense(request, expense_id):
    ExpenseController.delete_expense(expense_id)
    return redirect('expense_list')


def get_expenses_json(request):
    expenses = ExpenseController.get_all_expenses()
    data = {
        'expenses': [
            {
                'id': e.id,
                'name': e.name,
                'amount': str(e.amount),
                'category': e.category,
                'date': str(e.date),
                'description': e.description
            } for e in expenses
        ],
        'total': str(ExpenseController.get_total_expenses())
    }
    return JsonResponse(data)
