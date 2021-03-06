from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('carte/', views.carte, name="carte"),

    path('account/', include("django.contrib.auth.urls")),
    path('singup/', views.SignUp.as_view(), name="signup"),
    path('logout/', views.logout_request, name="logout"),

    path('ingredient/', views.IngredientList.as_view(), name="ingredientlist"),
    path('ingredient/delete/<pk>', views.IngredientDelete.as_view(), name="ingredientdelete"),
    path('ingredient/create', views.IngredientCreate.as_view(), name="ingredientcreate"),
    path('ingredient/update/<pk>', views.IngredientUpdate.as_view(), name="ingredientupdate"),

    path('menuitem/', views.MenuItemView, name="menuitemlist"),
    path('menuitem/delete/<pk>', views.MenuItemDelete.as_view(), name="menuitemdelete"),
    path('menuitem/create', views.MenuItemCreate.as_view(), name="menuitemcreate"),
    path('menuitem/update/<pk>', views.MenuItemUpdate.as_view(), name="menuitemupdate"),

    path('reciperequirement/create', views.RecipeRequirementCreate.as_view(), name="reciperequirementcreate"),
    path('reciperequirement/update/<pk>', views.RecipeRequirementUpdate.as_view(), name="reciperequirementupdate"),
    path('reciperequirement/delete/<pk>', views.RecipeRequirementDelete.as_view(), name="recipedelete"),

    path('purchase/', views.PurchasesList.as_view(), name="purchaselist"),
    path('purchase/create', views.PurchasesCreate.as_view(), name="purchasecreate"),

    path('profit/', views.Profit, name="profit"),
]