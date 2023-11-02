from django.urls import path
from .views import SportTypeViewSet, SportTypeViewSett, TournamentTypeViewSet, TournamentTypeViewSett
urlpatterns = [
    path('tournamenttypes/', TournamentTypeViewSet.as_view()),
    path('tournamenttypes/<int:pk>', TournamentTypeViewSett.as_view()),
    path('sporttypes/', SportTypeViewSet.as_view()),
    path('sporttypes/<int:pk>', SportTypeViewSett.as_view()),

]
