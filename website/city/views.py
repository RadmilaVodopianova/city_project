from django.http import HttpResponse


def index(request):
    return HttpResponse("""
        <h1>Одеса</h1>
        <h2>Головна</h2>
        <p>Ласкаво просимо на сайт про Одесу!</p>
        <p>Тут ви знайдете новини, цікаві факти,
        історію міста та контакти міських служб.</p>
    """)