from django.urls import path
from . import views

app_name='student'

urlpatterns=[
    path('<int:course_id>',views.student, name="studentMain"),
    path('<int:question_id>/',views.sdetail, name="sdetail"),
    path('post/questions/<int:course_id>',views.postQuestions,name="postQuestions"),
    path('post/questions/<int:course_id>/<quest>',views.postQuestions2),
    path('ask/questions/<int:course_id>',views.askQuestion,name="askQuestion"),
    path('write/comment/<int:question_id>/',views.writeComment, name="writeComment"),
    path('like/<int:question_id>/<int:id>',views.like, name="like"),
    path('like2/<int:question_id>/<int:id>/<int:course_id>',views.like2, name="like2"),

]