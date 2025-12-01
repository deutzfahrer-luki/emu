import pytest
from components import Input, FullAdder16Bit, Sub16Bit

# ------------------------------
# Hilfsfunktion: int -> 16 Input Bits
# ------------------------------
def int_to_bits16(val: int) -> list[Input]:
    return [Input(bool((val >> i) & 1)) for i in range(16)]

# ------------------------------
# Hilfsfunktion: 16 Output Bits -> int
# ------------------------------
def bits16_to_int(bits: list) -> int:
    return sum(int(bit.value) << i for i, bit in enumerate(bits))


# ------------------------------
# FullAdder16Bit Tests
# ------------------------------
@pytest.mark.parametrize("a, b, carry_in, expected_sum, expected_carry", [
    (0x0000, 0x0000, False, 0x0000, False),
    (0xFFFF, 0x0001, False, 0x0000, True),  # overflow
    (0x1234, 0x4321, False, 0x5555, False),
    (0x8000, 0x8000, False, 0x0000, True),
])
def test_full_adder16bit(a, b, carry_in, expected_sum, expected_carry):
    adder = FullAdder16Bit()
    a_bits = int_to_bits16(a)
    b_bits = int_to_bits16(b)
    carry_bit = Input(carry_in)

    sum_bits, carry_out = adder(a_bits, b_bits, carry_bit)
    result = bits16_to_int(sum_bits)

    assert result == expected_sum
    assert carry_out.value == expected_carry


# ------------------------------
# Sub16Bit Tests
# ------------------------------
@pytest.mark.parametrize("a, b, expected_result, expected_borrow", [
    (0x0000, 0x0000, 0x0000, False),
    (0x0001, 0x0001, 0x0000, False),
    (0x0000, 0x0001, 0xFFFF, True),  # borrow
    (0x1234, 0x0010, 0x1224, False),
    (0x8000, 0x8001, 0xFFFF, True),  # borrow
])
def test_sub16bit(a, b, expected_result, expected_borrow):
    sub = Sub16Bit()
    a_bits = int_to_bits16(a)
    b_bits = int_to_bits16(b)

    result_bits, borrow = sub(a_bits, b_bits)
    result_int = bits16_to_int(result_bits)

    assert result_int == expected_result
    assert borrow.value == expected_borrow
