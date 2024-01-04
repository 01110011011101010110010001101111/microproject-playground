class Circuit:
    def __init__(self, gates, n_wires):
        self.gates = gates
        self.n_wires = n_wires
    def add_gate(self, unitary, wires):
        unitary_dim = len(unitary)
    def forward(self):
        for gate in self.gates:
            pass
