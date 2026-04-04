# pytest test template (montana-py)

```py
import pytest

def test_do_thing_ok():
    assert do_thing("x") == "y"

def test_do_thing_invalid_input():
    with pytest.raises(ValueError, match="invalid"):
        do_thing("")
```

