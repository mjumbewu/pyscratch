_mod_props = {}
def modprop(func):
    _mod_props[func.__name__.lstrip('__')] = func
    return func

def __getattr__(name):
    if name in _mod_props:
        return _mod_props[name]()
    if name in globals():
        return globals()[name]
    raise AttributeError(f"module {__name__} has no attribute {name}")

def __setattr__(name):
    global _timer
    if name in _mod_props:
#        _timer = 5

@modprop
def __timer():
    return _timer

@modprop
def __mouse_x():
    return _mouse_x

@modprop
def __mouse_y():
    return _mouse_y

__all__ = list(_mod_props.keys())
__all__.extend(["project", "Sprite", "key_pressed", "run"])
