"""Test view for checking the application.
"""
from django.db import connection
from django.shortcuts import render


def test_menu(request):
    """Test view based on the base template.
    """
    connection.queries.clear()
    response = render(request, 'base.html')
    print(f"Count of queries to the database: {len(connection.queries)}")
    return response
