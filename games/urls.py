from django.urls import path

from games.views import AboutUsView, HomePageView, MathFactsView, AnagramHuntView

app_name = 'games'
urlpatterns = [
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('', HomePageView.as_view(), name='homepage'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
]