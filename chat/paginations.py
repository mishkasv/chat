from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'elided_page': self.page.paginator.get_elided_page_range(number=self.page.number),
            'page_number':  self.page.number,
            'count': self.page.paginator.count,
            'results': data
        })