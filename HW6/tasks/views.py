from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def current_datetime(request):
    now = datetime.now()
    formatted_datetime = now.strftime("%d.%m.%Y %H:%M:%S")
    html = f"""
    <html>
    <head>
        <title>Поточна дата та час</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
            }}
            .datetime {{
                font-size: 48px;
                color: #333;
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
        </style>
    </head>
    <body>
        <div class="datetime">{formatted_datetime}</div>
    </body>
    </html>
    """
    return HttpResponse(html)


def multiplication_table(request):
    html = """
    <html>
    <head>
        <title>Таблиця множення</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                padding: 20px;
                background-color: #f5f5f5;
            }
            h1 {
                text-align: center;
                color: #333;
            }
            table {
                margin: 20px auto;
                border-collapse: collapse;
                background: white;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            th, td {
                border: 1px solid #ddd;
                padding: 12px 15px;
                text-align: center;
            }
            th {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            tr:hover {
                background-color: #ddd;
            }
        </style>
    </head>
    <body>
        <h1>Таблиця множення від 1 до 10</h1>
        <table>
            <tr>
                <th>×</th>
    """

    for i in range(1, 11):
        html += f"<th>{i}</th>"

    html += "</tr>"

    for i in range(1, 11):
        html += f"<tr><th>{i}</th>"
        for j in range(1, 11):
            html += f"<td>{i * j}</td>"
        html += "</tr>"

    html += """
        </table>
    </body>
    </html>
    """
    return HttpResponse(html)


TASKS = [
    {"id": 1, "name": "homework", "description": "Виконати домашнє завдання з Django"},
    {"id": 2, "name": "shopping", "description": "Купити продукти в магазині"},
    {"id": 3, "name": "exercise", "description": "Зробити ранкову зарядку"},
    {"id": 4, "name": "reading", "description": "Прочитати 50 сторінок книги"},
    {"id": 5, "name": "coding", "description": "Написати код для нового проєкту"},
]


def task_list(request):
    html = """
    <html>
    <head>
        <title>Список задач</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            h1 {
                color: #333;
                text-align: center;
            }
            .task {
                background: white;
                margin: 10px 0;
                padding: 15px;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .task h3 {
                margin: 0 0 10px 0;
                color: #4CAF50;
            }
            .task p {
                margin: 5px 0;
                color: #666;
            }
            a {
                color: #2196F3;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>Список задач</h1>
    """

    for task in TASKS:
        html += f"""
        <div class="task">
            <h3>{task['name']}</h3>
            <p>{task['description']}</p>
            <p>
                <a href="/tasks/id/{task['id']}">Переглянути по ID</a> |
                <a href="/tasks/name/{task['name']}">Переглянути по назві</a>
            </p>
        </div>
        """

    html += """
    </body>
    </html>
    """
    return HttpResponse(html)


def task_by_id(request, task_id):
    task = next((t for t in TASKS if t['id'] == task_id), None)

    if task is None:
        html = """
        <html>
        <head>
            <title>Задача не знайдена</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                    background-color: #f5f5f5;
                }
                .error {
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    display: inline-block;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                }
                h1 {
                    color: #f44336;
                }
                a {
                    color: #2196F3;
                    text-decoration: none;
                    font-size: 18px;
                }
            </style>
        </head>
        <body>
            <div class="error">
                <h1>Задачу не знайдено</h1>
                <p>Задача з ID """ + str(task_id) + """ не існує.</p>
                <p><a href="/tasks/">Повернутися до списку задач</a></p>
            </div>
        </body>
        </html>
        """
        return HttpResponse(html, status=404)

    html = f"""
    <html>
    <head>
        <title>Задача: {task['name']}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            .task-detail {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #4CAF50;
                margin-top: 0;
            }}
            .info {{
                margin: 15px 0;
                color: #666;
            }}
            .label {{
                font-weight: bold;
                color: #333;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                color: #2196F3;
                text-decoration: none;
                font-size: 16px;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="task-detail">
            <h1>{task['name']}</h1>
            <p class="info"><span class="label">ID:</span> {task['id']}</p>
            <p class="info"><span class="label">Назва:</span> {task['name']}</p>
            <p class="info"><span class="label">Опис:</span> {task['description']}</p>
            <a href="/tasks/">← Повернутися до списку задач</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


def task_by_name(request, task_name):
    task = next((t for t in TASKS if t['name'] == task_name), None)

    if task is None:
        html = """
        <html>
        <head>
            <title>Задача не знайдена</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                    background-color: #f5f5f5;
                }
                .error {
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    display: inline-block;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                }
                h1 {
                    color: #f44336;
                }
                a {
                    color: #2196F3;
                    text-decoration: none;
                    font-size: 18px;
                }
            </style>
        </head>
        <body>
            <div class="error">
                <h1>Задачу не знайдено</h1>
                <p>Задача з назвою '""" + task_name + """' не існує.</p>
                <p><a href="/tasks/">Повернутися до списку задач</a></p>
            </div>
        </body>
        </html>
        """
        return HttpResponse(html, status=404)

    html = f"""
    <html>
    <head>
        <title>Задача: {task['name']}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            .task-detail {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #4CAF50;
                margin-top: 0;
            }}
            .info {{
                margin: 15px 0;
                color: #666;
            }}
            .label {{
                font-weight: bold;
                color: #333;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                color: #2196F3;
                text-decoration: none;
                font-size: 16px;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="task-detail">
            <h1>{task['name']}</h1>
            <p class="info"><span class="label">ID:</span> {task['id']}</p>
            <p class="info"><span class="label">Назва:</span> {task['name']}</p>
            <p class="info"><span class="label">Опис:</span> {task['description']}</p>
            <a href="/tasks/">← Повернутися до списку задач</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)
