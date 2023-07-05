from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, AnswerViewSet


router = DefaultRouter()

router.register('quiz', QuizViewSet)
router.register('answer', AnswerViewSet)
router.register('question', QuestionViewSet)


urlpatterns = router.urls

