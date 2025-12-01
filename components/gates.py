from components.bit import Input, Output


class Gate:
    def __call__(self, *inputs: Input) -> Output:
        raise NotImplementedError("Subclasses must implement __call__()")

    @staticmethod
    def _validate_inputs(inputs, min_count=1, max_count=None):
        if len(inputs) < min_count:
            raise ValueError(f"Expected at least {min_count} input(s), got {len(inputs)}")
        if max_count is not None and len(inputs) > max_count:
            raise ValueError(f"Expected at most {max_count} input(s), got {len(inputs)}")
        for inp in inputs:
            if not isinstance(inp, Input):
                raise TypeError(f"Expected Input instance, got {type(inp).__name__}")


class And(Gate):
    def __call__(self, *inputs: Input) -> Output:
        self._validate_inputs(inputs, min_count=1)
        return Output(all(inp.value for inp in inputs))


class Or(Gate):
    def __call__(self, *inputs: Input) -> Output:
        self._validate_inputs(inputs, min_count=1)
        return Output(any(inp.value for inp in inputs))


class Xor(Gate):
    def __call__(self, *inputs: Input) -> Output:
        self._validate_inputs(inputs, min_count=1)
        result = sum(inp.value for inp in inputs) % 2 == 1
        return Output(result)


class Not(Gate):
    def __call__(self, *inputs: Input) -> Output:
        self._validate_inputs(inputs, min_count=1, max_count=1)
        return Output(not inputs[0].value)
