import inspect
import symtable

count = 10
def get_global_count():
    return count


def get_locals(func):
    source = inspect.getsource(func)
    top = symtable.symtable(source, "<string>", "exec")
    func = top.get_children()[0]  #since we are passing only the func code.
    return func.get_locals()

def get_globals():
    module = inspect.getmodule(get_globals)
    source = inspect.getsource(module)
    top = symtable.symtable(source, "<string>", "exec")
    return top.get_identifiers()

global_names = get_globals()


def test_scope_writing_globals():
    local_names = get_locals(test_scope_writing_globals)

    assert __ == ('count' in local_names)
    assert __ == ('count' in global_names)

    global count

    try:
        count = 40
        assert __ == count
        assert __ == get_global_count()
    finally:
        count = 10

    assert __ == get_global_count()