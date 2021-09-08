# Full Stack React & Django - Traversy Media 

## Basic REST API 
- Install `pipenv install django djangorestframework django-rest-knox` in your pipenv shell 
- Next run `django-admin startproject leadmanager` in your pipenv shell 
- Then run in your pipenv shell `cd leadmanager/` then `python manage.py startapp leads`
- In our leadmanage/settings.py we add 'leads' and 'rest_framework' under INSTALLED_APPS and change our database to postgres under DATABASES
- Creating a model in models.py
  <code>
  class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
  </code>
- To make migrations run `python manage.py makemigrations leads` then `python manage.py migrate`
- With the rest_framework we run the serializer
- Create a `serializers.py` in your leads folder 
  - See page for part 1 branch for this one 