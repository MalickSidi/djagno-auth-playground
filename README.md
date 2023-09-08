# Django Authentication

For testing multiple approaches for user auth in django
[Django Doc](https://docs.djangoproject.com/en/4.2/topics/auth/)


> Django authentication provides both authentication and authorization together and is generally referred to as the authentication system, as these features are somewhat coupled. [Using Django authentication system](https://docs.djangoproject.com/en/4.2/topics/auth/default/)

**User:**
- Proxy Models
- One To One Field
  - Extend user Model by connecting it to a profile Model
- Extend Abstract Base User
- Extend Abstract User

## Authentication Views
[MDN Guides | Django User auth and permissions](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#setting_up_your_authentication_views)

1. Make sure to add in the urls file: `include('django.contrib.auth.urls')`
2. Make sure you have a folder with name `registration` in the `templates` folder
