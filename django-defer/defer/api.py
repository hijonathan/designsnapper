from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

def defer(func, *args, **kwargs):
    config = {}
    for name in ('countdown', 'eta'):
        conf_name = '_%s' % name
        if conf_name in kwargs:
            config[name] = kwargs[conf_name]
    default_backend(func, args, kwargs, **config)

def task(_func=None, _countdown=None, _eta=None):
    def _task(func):
        def _defer(*args, **kwargs):
            if _countdown is not None:
                kwargs.setdefault('_countdown', _countdown)
            if _eta is not None:
                kwargs.setdefault('_eta', _eta)
            defer(func, *args, **kwargs)
        func.defer = _defer
        return func

    if _func:
        return _task(_func)
    return _task

def load_backend(path):
    module_name, attr_name = path.rsplit('.', 1)
    try:
        mod = import_module(module_name)
    except ImportError, e:
        raise ImproperlyConfigured('Error importing file backend module %s: "%s"' % (module_name, e))
    except ValueError, e:
        raise ImproperlyConfigured('Error importing file backend module. Is FILE_TRANSFER_BACKENDS a correctly defined list or tuple?')
    try:
        backend = getattr(mod, attr_name)
    except AttributeError:
        raise ImproperlyConfigured('Module "%s" does not define a "%s" file backend' % (module_name, attr_name))
    return backend

default_backend = load_backend(settings.DEFER_BACKEND)
