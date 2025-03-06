class Input:
    def __init__(self, owner):
        if not isinstance(owner, LogicGate):
            raise TypeError("Owner must be a LogicGate")
        self._owner = owner

    @property
    def owner(self):
        return self._owner

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = bool(new_value)
        self.owner.evaluate()

    def __str__(self):
        try:
            return str(self.value)
        except AttributeError:
            return "(no value)"


class Output:
    def __init__(self):
        self._connections = []
        self._value = None

    @property
    def value(self):
        if hasattr(self, '_value'):
            return self._value
        raise AttributeError

    @value.setter
    def value(self, new_value):
        new_value_bool = bool(new_value)
        if hasattr(self, '_value') and self._value == new_value_bool:
            return
        self._value = new_value_bool
        for inp in self._connections:
            inp.value = self._value

    @property
    def connections(self):
        return self._connections

    def connect(self, input_):
        if not isinstance(input_, Input):
            raise TypeError("Input must be an instance of Input")
        if input_ not in self._connections:
            self._connections.append(input_)
            if hasattr(self, '_value'):
                input_.value = self._value

    def __str__(self):
        if hasattr(self, '_value'):
            return str(self._value)
        return "(no value)"


class LogicGate:
    def __init__(self, name):
        self._name = name
        self._output = Output()

    @property
    def name(self):
        return self._name

    @property
    def output(self):
        return self._output

    def evaluate(self):
        raise NotImplementedError


class UnaryGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input = Input(self)

    @property
    def input(self):
        return self._input

    def evaluate(self):
        if hasattr(self.input, '_value'):
            result = self.compute_result()
            self.output.value = result
        else:
            if hasattr(self.output, '_value'):
                del self.output._value

    def compute_result(self):
        raise NotImplementedError

    def __str__(self):
        return f"Gate '{self.name}': input={self.input}, output={self.output}."


class BinaryGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input0 = Input(self)
        self._input1 = Input(self)

    @property
    def input0(self):
        return self._input0

    @property
    def input1(self):
        return self._input1

    def evaluate(self):
        if hasattr(self.input0, '_value') and hasattr(self.input1, '_value'):
            result = self.compute_result()
            self.output.value = result
        else:
            if hasattr(self.output, '_value'):
                del self.output._value

    def compute_result(self):
        raise NotImplementedError

    def __str__(self):
        return f"Gate '{self.name}': input0={self.input0}, input1={self.input1}, output={self.output}."


class NotGate(UnaryGate):
    def compute_result(self):
        return not self.input.value


class AndGate(BinaryGate):
    def compute_result(self):
        return self.input0.value and self.input1.value


class OrGate(BinaryGate):
    def compute_result(self):
        return self.input0.value or self.input1.value


class XorGate(BinaryGate):
    def compute_result(self):
        return self.input0.value != self.input1.value


def test_input():
    not_gate = NotGate("test")
    input_ = not_gate.input
    print("Initially, input_ is:", input_)
    try:
        print(input_.value)
        print("Failed: input_.value exists before it's set, so that is literally impossible")
    except AttributeError:
        print("Succeeded: input_.value doesn't exist before it's set.")
    input_.value = True
    print("After set to True, input_ is:", input_)


def test_output():
    output = Output()
    print("Initially, output is:", output)
    try:
        print(output.value)
        print("Failed: output.value exists before it's set!")
    except AttributeError:
        print("Succeeded: output.value not set initially.")
    output.value = 5 
    print("After setting to 5:", output)
    output.value = 0 
    print("After setting to 0:", output)


def test_gates():
  
    not_gate = NotGate("not")
    print(not_gate)
    try:
        print(not_gate.output.value)
    except AttributeError:
        print("Output not set as expected.")
    not_gate.input.value = True
    print(not_gate.output.value)
    print(not_gate)
    not_gate.input.value = False
    print(not_gate)

    and_gate = AndGate("and")
    and_gate.input0.value = True
    and_gate.input1.value = True
    print(and_gate.output.value)
    and_gate.input1.value = False
    print(and_gate.output.value)

    or_gate = OrGate("or")
    or_gate.input0.value = False
    or_gate.input1.value = False
    print(or_gate.output.value)
    or_gate.input0.value = True
    or_gate.input1.value = False
    print(or_gate.output.value)
    or_gate.input0.value = True
    print(or_gate.output.value)

    xor_gate = XorGate("xor")
    xor_gate.input0.value = True
    xor_gate.input1.value = False
    print(xor_gate.output.value)
    xor_gate.input1.value = True
    print(xor_gate.output.value)


def test_connections():
  
    not1 = NotGate("not1")
    not1.input.value = False
    print(not1)

    not2 = NotGate("not2")
    not1.output.connect(not2.input)
    print("After connect:")
    print(not1)
    print(not2)

    not1.input.value = True
    print("After setting input to True:")
    print(not1)
    print(not2)

    and_gate = AndGate("and")
    not_gate = NotGate("not")
    and_gate.input0.value = True
    and_gate.input1.value = True
    and_gate.output.connect(not_gate.input)
    print("\nAND-NOT connection:")
    print(and_gate)
    print(not_gate)
    and_gate.input1.value = False
    print(and_gate)
    print(not_gate)


if __name__ == "__main__":
    test_input()
    print("\nTesting Output:")
    test_output()
    print("\nTesting Gates:")
    test_gates()
    print("Making sure it works:")
    test_connections()