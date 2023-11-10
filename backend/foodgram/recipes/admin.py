from django.contrib import admin

from recipes.models import (
    Ingredient, Tag, Recipe, IngredientAmount,
    FavoriteRecipe, ShoppingCart
)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'author', 'get_favorite')
    list_filter = ('author', 'name', 'tags')
    readonly_fields = ('get_favorite',)

    def get_favorite(self, obj):
        return obj.favorite.count()

    get_favorite.short_description = 'Избранное'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    list_filter = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug',)
    list_filter = ('name',)


@admin.register(IngredientAmount)
class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')