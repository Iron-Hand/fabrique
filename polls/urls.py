from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.authtoken import views as auth_views
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('polls/', views.PollsList.as_view()),
    path('poll/', views.PollCreate.as_view()),
    path('poll/<int:pk>', views.PollDetail.as_view()),
    path('question/', views.QuestionList.as_view()),
    path('question/<int:pk>', views.QuestionDetail.as_view()),
    path('question_types/', views.QuestionTypeList.as_view()),
    path('answer/', views.AnswerList.as_view()),
    path('user/<int:pk>', views.UserDetail.as_view()),
    path('auth/', auth_views.obtain_auth_token),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi/', get_schema_view(
        title="polls",
        description="API for polls app",
        version="0.0.1"
    ), name='openapi-schema'),
]

urlpatterns = format_suffix_patterns(urlpatterns)