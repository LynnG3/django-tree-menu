from django.shortcuts import render


def test_menu(request):
    """тестовое представление на основе базового шаблона. """
    return render(request, 'base.html')
