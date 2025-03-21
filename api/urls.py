from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UsersViewSet, InfoViewSet, SearchKeyListMazurova, SearchKeyListGolovackogo,
                    SearchKeyListKozhara, SearchKeyListBorodina, SearchKeyListNovopolesskaya,
                    SearchKeyListHataevicha, SearchKeyListStarochernigovskaya, SearchKeyListTelegina,
                    ViewOpenAccident, ViewCheckAccident, ViewCloseAccident
                    )

router = DefaultRouter()
router.register(r'пользователи', UsersViewSet, basename='users')
router.register(r'info_текущий месяц', InfoViewSet, basename='actualmonth')
router.register(r'ключи_мазурова', SearchKeyListMazurova, basename='keys_mazurova')
router.register(r'ключи_головацкого', SearchKeyListGolovackogo, basename='keys_golovackogo')
router.register(r'ключи_кожара', SearchKeyListKozhara, basename='keys_kozhara')
router.register(r'ключи_бородина', SearchKeyListBorodina, basename='keys_borodina')
router.register(r'ключи_хатаевича', SearchKeyListHataevicha, basename='keys_hataevica')
router.register(r'ключи_новополесская', SearchKeyListNovopolesskaya, basename='keys_novopolesskaya')
router.register(r'ключи_старочерниговская', SearchKeyListStarochernigovskaya, basename='keys_starochernigovskaya')
router.register(r'ключи_телегина', SearchKeyListTelegina, basename='keys_telegina')
router.register(r'открытые инциденты', ViewOpenAccident, basename='open_accident')
router.register(r'инциденты в статусе проверки', ViewCheckAccident, basename='check_accident')
router.register(r'закрытые инциденты', ViewCloseAccident, basename='close_accident')

urlpatterns = [
    path('', include(router.urls)),
]
