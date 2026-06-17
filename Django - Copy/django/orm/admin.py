from django.contrib import admin

from .models import *

admin.site.register(Author)
admin.site.register(Book)


# select_related  - work with foreign key and one to on e field  ,sql joins
# prefetch_relateed - work with many to many field ,multiple joins

admin.site.register(Department)
admin.site.register(Emp)

admin.site.register(Course)
admin.site.register(Student)