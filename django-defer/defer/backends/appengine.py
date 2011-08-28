from djangoappengine.utils import on_production_server
from google.appengine.ext.deferred import defer as gae_defer

def defer(func, args, kwargs, **config):
    if not on_production_server:
        func(*args, **kwargs)
        return
    for name in ('countdown', 'eta'):
        if name in config:
            kwargs['_%s' % name] = config.pop(name)
    assert not config, 'Unsupported config: %s' % ', '.join(config.keys())
    gae_defer(func, *args, **kwargs)
