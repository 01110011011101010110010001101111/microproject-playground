def raw_probabilities(quantum_state, basis_vec=None):
    '''
    Assume the input quantum_state has some conjugate function
    '''
    if basis_vec is None:
        basis_vec = [1, 0]
    return (basis_vec.conjugate().dot(quantum_state))**2 
