import pytest
from Double_Linked import Double_Linked


@pytest.fixture
def dl():
    return dl()


def test_answer():
    dl = Double_Linked()
    dl.insert_before(13)
    dl.insert_after(dl.head.next, 6)
    dl.printList(dl.head)
    assert dl.head.data == 13


def f():
    raise SystemExit(1)
