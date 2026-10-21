
from django.shortcuts import render
from datetime import datetime


def home(request):
    days = [
        "Понеділок",
        "Вівторок",
        "Середа",
        "Четвер",
        "П'ятниця",
        "Субота",
        "Неділя"
    ]

    colors = [
        "#2563eb",
        "#7c3aed",
        "#059669",
        "#ea580c",
        "#db2777",
        "#0891b2",
        "#b45309"
    ]

    today = datetime.now().weekday()

    context = {
        "day": days[today],
        "color": colors[today],
        "day_number": today
    }

    return render(request, "weekdays/home.html", context)
