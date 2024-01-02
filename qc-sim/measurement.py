def raw_probabilities(quantum_state, basis_vec=None):
    '''
    Assume the input quantum_state has some conjugate function
    '''
    if basis_vec is None:
        basis_vec = [1, 0]
    return (basis_vec.conjugate().dot(quantum_state))**2 

def measure(quantum_state, basis):
    """
    Returns (probability, updated_state)
    """
    projected_quantum_state = basis @ quantum_state
    prob = quantum_state.conjugate() @ projected_quantum_state
    return prob, projected_quantum_state / prob**0.5

def expected_value(quantum_state, observable):
    """
    computes probability given an observable
    """
    return quantum_state.conjugate() @ observable @ quantum_state
