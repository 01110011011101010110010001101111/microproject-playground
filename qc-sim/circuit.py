import numpy as np

gates = {
    "h": 1 / 2**0.5 * np.array([[1, 1], [1, -1]]),
    "x": np.array([[0, 1], [1, 0]])
}

class Circuit:
    def __init__(self, n_wires, gates = frozenset()):
        self.gates = gates
        self.n_wires = n_wires
        self.matrix_state = np.eye(2*n_wires)
    def add_gate(self, gate_name, wires):
        arr = []
        for wire in range(self.n_wires):
            if wire == wires:
                arr.append(gates[gate_name])
            else:
                arr.append(np.eye(2))
        val = arr[0]
        for a in arr[1:]:
            val = np.kron(val, a)
        self.matrix_state = val @ self.matrix_state
        return self.matrix_state
    def forward(self, input_state):
        return self.matrix_state @ input_state

