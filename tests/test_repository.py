import pytest

from proxyrotation.common import has_async
from proxyrotation.repository import from_name, abc_Repository


def test_from_name_async():
    if not has_async:
        pytest.skip("should install async dependencies")
    
    repository = from_name("async")
    assert isinstance(repository, abc_Repository)


def test_from_name_sequential():
    repository = from_name("sequential")
    assert isinstance(repository, abc_Repository)


def test_invalid_from_name():
    with pytest.raises(ImportError):
        from_name("invalid")
