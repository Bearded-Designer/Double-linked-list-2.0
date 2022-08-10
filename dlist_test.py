import pytest
from Double_Linked import Double_Linked

dl = Double_Linked()


def test_answer():
    assert dl.insert_before(13)
    assert dl.insert_after(dl.head.next, 12)


def f():
    raise SystemExit(1)
