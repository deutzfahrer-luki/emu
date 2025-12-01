from components import And, Or, Xor, Not, Input, Output


class HalfAdder:
    def __init__(self) -> None:
        self._xor = Xor()
        self._and = And()

    def __call__(self, a: Input, b: Input) -> tuple[Output, Output]:
        sum_bit = self._xor(a, b)
        carry_bit = self._and(a, b)
        return sum_bit, carry_bit


class FullAdder:
    def __init__(self) -> None:
        self._ha1 = HalfAdder()
        self._ha2 = HalfAdder()
        self._or = Or()

    def __call__(self, a: Input, b: Input, carry_in: Input) -> tuple[Output, Output]:
        sum1, carry1 = self._ha1(a, b)
        sum2, carry2 = self._ha2(Input(sum1.value), carry_in)
        final_carry = self._or(Input(carry1.value), Input(carry2.value))
        return sum2, final_carry


class FullAdder16Bit:
    def __init__(self) -> None:
        self._adders = [FullAdder() for _ in range(16)]

    def __call__(self, a_bits: list[Input], b_bits: list[Input], carry_in: Input = Input(False)) -> tuple[list[Output], Output]:
        if len(a_bits) != 16 or len(b_bits) != 16:
            raise ValueError("Both input lists must have exactly 16 Input objects")
        
        result_bits = []
        carry = carry_in

        for i in range(16):
            sum_bit, carry_out = self._adders[i](a_bits[i], b_bits[i], carry)
            result_bits.append(sum_bit)
            carry = Input(carry_out.value)

        return result_bits, Output(carry.value)


class Sub16Bit:
    def __init__(self) -> None:
        self._adders = [FullAdder() for _ in range(16)]
        self._not_gate = Not()

    def __call__(self, a_bits: list[Input], b_bits: list[Input]) -> tuple[list[Output], Output]:
        if len(a_bits) != 16 or len(b_bits) != 16:
            raise ValueError("Both input lists must have exactly 16 Input objects")
        
        result_bits = []
        carry = Input(True)
        for i in range(16):
            b_inverted = self._not_gate(b_bits[i])
            sum_bit, carry_out = self._adders[i](a_bits[i], Input(b_inverted.value), carry)
            result_bits.append(sum_bit)
            carry = Input(carry_out.value)

        borrow = Output(not carry.value)
        return result_bits, borrow
