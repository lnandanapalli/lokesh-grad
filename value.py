class Value:
    def __init__(self, data: int, _children: tuple = (), _op: str = "", label:str = ""):
        self.data = data
        self._prev = set(_children)
        self._op = _op
        self.label = label
    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other: "Value") -> "Value":
        return Value(self.data + other.data, (self, other), "+")

    def __mul__(self, other: "Value"):
        return Value(self.data * other.data, (self, other), "*")

if __name__ == "__main__":
    a = Value(2.0, label="a")
    b = Value(-3.0, label="b")
    c = Value(10.0, label="c")
    e = a * b
    e.label = "e"
    d = e + c
    d.label = "d"
    f = Value(-2.0, label="f")
    L = d * f
    L.label = "L"
    print(L)