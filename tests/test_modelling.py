from dataclasses import asdict

import pytest

from proxyrotation.common import Anonymity, Proxy


@pytest.fixture
def sample() -> Proxy:
    return Proxy("192.168.1.1", 8080, "US", Anonymity.high, True)


def test_anonymity_from_string():
    assert Anonymity.from_string("elite proxy") == Anonymity.high
    assert Anonymity.from_string("anonymous") == Anonymity.medium
    assert Anonymity.from_string("transparent") == Anonymity.weak
    assert Anonymity.from_string("unknown") == Anonymity.unknown
    assert Anonymity.from_string("a1b2c3d4e5") == Anonymity.unknown
    assert Anonymity.from_string("") == Anonymity.unknown


def test_address_asdict(sample: Proxy):
    assert asdict(sample) == {
        "host": "192.168.1.1",
        "port": 8080,
        "countrycode": "US",
        "anonymity": "elite proxy",
        "secure": True,
    }
