from django.urls import path
from .views import ArticleView
app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
	path('tags/', ArticleView.as_view()),
    path('tags/<task_id>', ArticleView.as_view()),
]