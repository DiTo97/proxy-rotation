import pytest

from proxyrotation.common import batch_response_parsing, is_ipv4_address
from proxyrotation.modelling import Anonymity, Proxy


@pytest.fixture
def sample() -> Proxy:
    return Proxy("192.168.1.1", 8080, "US", Anonymity.weak, True)


@pytest.fixture
def response() -> str:
    return """\
<tr>
  <td>111.111.111.111</td><td>8080</td><td>CN</td><td class="hm">China</td><td>anonymous</td>
  <td class="hm">no</td><td class="hx">yes</td><td class="hm">1 min ago</td>
</tr>
<tr>
  <td>222.222.222.222</td><td>8080</td><td>NL</td><td class="hm">Netherlands</td><td>elite proxy</td>
  <td class="hm">yes</td><td class="hx">no</td><td class="hm">2 mins ago</td>
</tr>
"""


def test_is_ipv4_address():
    assert is_ipv4_address("192.168.1.1") is True
    assert is_ipv4_address("255.255.255.255") is True


def test_is_not_ipv4_address():
    assert is_ipv4_address("999.999.999.999") is False
    assert is_ipv4_address("not an IP") is False
    assert is_ipv4_address("") is False


def test_is_ipv4_address_with_address(sample: Proxy):
    assert is_ipv4_address(sample) is True


def test_batch_response_parsing(response: str):
    expected = {
        Proxy("111.111.111.111", 8080, "CN", Anonymity.medium, True),
        Proxy("222.222.222.222", 8080, "NL", Anonymity.high, False),
    }

    response = batch_response_parsing(response)
    assert response == expected


def test_batch_response_parsing_malformed():
    response = "<tr><td>malformed proxy address source</td></tr>"
    expected = set()

    response = batch_response_parsing(response)
    assert response == expected
