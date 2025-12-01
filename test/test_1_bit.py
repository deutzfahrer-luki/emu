import pytest
from components import Bit, Input, Output


# --- Bit --------------------------------------------------------------------

def test_bit_initialization():
    b = Bit(True)
    assert b.value is True

    b = Bit(False)
    assert b.value is False


def test_bit_rejects_non_bool():
    with pytest.raises(TypeError):
        Bit("not a bool")

    with pytest.raises(TypeError):
        Bit(1)

    with pytest.raises(TypeError):
        Bit(None)


def test_bit_is_immutable():
    b = Bit(True)
    with pytest.raises(AttributeError):
        b.value = False  # no setter in Bit


# --- Input ------------------------------------------------------------------

def test_input_is_bit():
    i = Input(True)
    assert isinstance(i, Bit)
    assert i.value is True


def test_input_allows_setting_value():
    i = Input(True)
    i.value = False
    assert i.value is False


def test_input_rejects_non_bool():
    i = Input(True)
    with pytest.raises(TypeError):
        i.value = "abc"


# --- Output -----------------------------------------------------------------

def test_output_is_bit():
    o = Output(False)
    assert isinstance(o, Bit)
    assert o.value is False


def test_output_is_immutable_like_bit():
    o = Output(True)
    with pytest.raises(AttributeError):
        o.value = False


def test_output_rejects_non_bool_in_constructor():
    with pytest.raises(TypeError):
        Output("yes")
