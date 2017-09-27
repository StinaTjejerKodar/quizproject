from django.shortcuts import render

# Create your views here.

def startsida(request):
		return render(request, "startsida.html")

def quiz(request, quiz_number):
		return render(request, "quiz.html")

def question(request, quiz_number, question_number):
		return render(request, "question.html")

def results(request, quiz_number):
		return render(request, "results.html")



