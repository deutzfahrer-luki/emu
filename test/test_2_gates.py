import pytest
from components.bit import Input, Output
from components.gates import And, Or, Xor, Not


# -----------------------------------------------------------
# AND GATE
# -----------------------------------------------------------

def test_and_gate_basic():
    gate = And()
    a, b, c, d = Input(True), Input(True), Input(False), Input(True)

    # 2 inputs
    assert gate(Input(True), Input(True)).value is True
    assert gate(Input(True), Input(False)).value is False

    # 4 inputs
    assert gate(a, b, c, d).value is False

    # all False
    assert gate(Input(False), Input(False), Input(False)).value is False


def test_and_gate_requires_at_least_one_input():
    gate = And()
    with pytest.raises(ValueError):
        gate()  # no input


def test_and_gate_rejects_wrong_type():
    gate = And()
    with pytest.raises(TypeError):
        gate(Input(True), "not an input")


# -----------------------------------------------------------
# OR GATE
# -----------------------------------------------------------

def test_or_gate_basic():
    gate = Or()
    a, b, c = Input(False), Input(False), Input(True)

    assert gate(a, b).value is False
    assert gate(a, b, c).value is True
    assert gate(Input(True), Input(False), Input(False)).value is True


def test_or_gate_requires_at_least_one_input():
    gate = Or()
    with pytest.raises(ValueError):
        gate()


def test_or_gate_rejects_wrong_type():
    gate = Or()
    with pytest.raises(TypeError):
        gate(Input(True), 123)


# -----------------------------------------------------------
# XOR GATE
# -----------------------------------------------------------

def test_xor_gate_basic():
    gate = Xor()
    a, b, c, d = Input(True), Input(True), Input(False), Input(True)

    # 2 inputs
    assert gate(Input(True), Input(False)).value is True
    assert gate(Input(True), Input(True)).value is False

    # 4 inputs (3 True -> odd parity)
    assert gate(a, b, c, d).value is True

    # 3 inputs (even parity)
    assert gate(Input(True), Input(True), Input(False)).value is False


def test_xor_gate_requires_at_least_one_input():
    gate = Xor()
    with pytest.raises(ValueError):
        gate()


def test_xor_gate_rejects_wrong_type():
    gate = Xor()
    with pytest.raises(TypeError):
        gate(Input(True), None)


# -----------------------------------------------------------
# NOT GATE
# -----------------------------------------------------------

def test_not_gate_basic():
    gate = Not()

    assert gate(Input(True)).value is False
    assert gate(Input(False)).value is True


def test_not_gate_requires_exactly_one_input():
    gate = Not()

    with pytest.raises(ValueError):
        gate()

    with pytest.raises(ValueError):
        gate(Input(True), Input(False))


def test_not_gate_rejects_wrong_type():
    gate = Not()
    with pytest.raises(TypeError):
        gate("not an input")
