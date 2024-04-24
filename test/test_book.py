import pytest


@pytest.mark.parametrize(
    "want",
    [
        "dcba",
        "",
        "a",
        "4321",
        "54321",
        "654321",
    ],
)
def test_dummy_test(want):
    assert want == want
