def raw_probabilities(basis_vec, quantum_state):
    '''
    Assume the input quantum_state has some conjugate function
    '''
    return abs(quantum_state.conjugate() * basis_vec)**2 
