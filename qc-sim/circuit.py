class Gate:
    def __init__(self, unitary, wire = None):
        self.unitary = unitary
        self.wire = wire

class Circuit:
    def __init__(self, gates, n_wires):
        self.gates = gates
        self.n_wires = n_wires
    def forward(self):
        for gate in self.gates:
            pass
