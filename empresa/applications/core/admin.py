from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','author', 'published', 'post_categories') #anadimos nuestra funcion pos_categories para que aparezca en la tabla de visualizacion
    ordering = ('author', 'published')
    search_fields = ('title','content','author__username','categories__name') #author__username para que busque por medio de la foreign key haciendo un filtro a su atributo uername
    date_hierarchy = 'published' #para que se vea la fecha encima del cuadro de la tabla
    list_filter = ('author__username', 'categories__name') #el filter es mejor hacerlo para cuando hay jooins

    #creamos una funcion para que concatene cada nombre de categoria con una ','
    #para que se vea en la tabla de visualizacion concatenados las categorias que tiene un registro
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    post_categories.short_description = "Categorias" # le cambiamos el nombree de la funcion post_cateogries en la tabla de visualizacion

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)