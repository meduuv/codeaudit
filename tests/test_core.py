from codeaudit.core import audit

def test_audit():
    result = audit("# TODO\n" + "x" * 101)
    assert result == {"lines": 2, "todos": 1, "long_lines": 1}
