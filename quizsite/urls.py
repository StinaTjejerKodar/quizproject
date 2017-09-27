from django.urls import path
from quiz import views

urlpatterns = [
	path("", views.startpage),
	path("quiz/<int:quiz_number>/", views.quiz),
	path("quiz/<int:quiz_number>/question/<int:question_number>/" , view.question),
	path("quiz/<int:quiz_number>/results/<int:results_number>/" , view.results)

