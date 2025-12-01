class Bit:
    def __init__(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("value must be a bool")
        self._value = value

    @property
    def value(self) -> bool:
        return self._value


class Input(Bit):
    @Bit.value.setter
    def value(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("value must be a bool")
        self._value = value


class Output(Bit):
    pass
