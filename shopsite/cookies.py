from django.conf import settings


def checkcookiesanddelete(request, response, cookie_key):
    cookie_key = request.get_signed_cookie(cookie_key, default=None, salt=settings.COOKIE_SALT_VALUE,
                                           max_age=settings.COOKIE_EXPIRE_TIME)
    response.delete_cookie(cookie_key)
    print(cookie_key)
    return response


def checkcookiesandcreate(request, response, cookie_key):
    cookie_key = request.get_signed_cookie(cookie_key, default=None, salt=settings.COOKIE_SALT_VALUE,
                                           max_age=settings.COOKIE_EXPIRE_TIME)
    response.set_signed_cookie('username', cookie_key, salt=settings.COOKIE_SALT_VALUE,
                               expires=settings.COOKIE_EXPIRE_TIME)
    return response