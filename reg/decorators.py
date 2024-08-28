# decorators.py
from functools import wraps

def with_lang(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        lang_value = request.headers.get('lang')
        if not lang_value:
            lang_value = "zh-CN"
        request.lang = lang_value
        return view_func(request, *args, **kwargs)
    return _wrapped_view
