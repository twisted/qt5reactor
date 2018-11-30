import pytest
import twisted


@pytest.inlineCallbacks
def test_example():
    expected = 42

    d = twisted.internet.defer.Deferred()
    d.callback(expected)

    result = yield d

    assert result == expected
