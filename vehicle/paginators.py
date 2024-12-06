from rest_framework.pagination import PageNumberPagination


#11.5
class VehiclePaginator(PageNumberPagination):
    page_size = 10
