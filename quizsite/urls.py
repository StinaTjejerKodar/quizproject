
from django.contrib import admin
from django.urls import path
from quiz import views


urlpatterns = [
	
	path("", views.startsida, name="start_sida"),
	
	path("quiz/<int:quiz_number>/", views.quiz, name="quiz_page"),
	
	path("quiz/<int:quiz_number>/question/<int:question_number>/", views.question, name="question_page"),
	
	path("quiz/<int:quiz_number>/results/" , views.results, name="results_page"),

	path('admin/', admin.site.urls),

	path("quiz/<int:quiz_number>/question/<int:question_number>/answer/", views.answer, name="answer_page"),
	
	]

