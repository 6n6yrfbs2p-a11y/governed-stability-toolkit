"""
Core quantities for governed stability:
- phi_dot: energy descent
- psi_dot: information ascent
- lambda_dot: structural/meaning growth
- sigma_dot: closure (balance)
"""

def phi_dot(state):
    """Placeholder for energy descent rate."""
    raise NotImplementedError("Define Φ̇ for your system here.")

def psi_dot(state):
    """Placeholder for information ascent rate."""
    raise NotImplementedError("Define Ψ̇ for your system here.")

def lambda_dot(state):
    """Placeholder for structural/meaning growth rate."""
    raise NotImplementedError("Define Λ̇ for your system here.")

def sigma_dot(state):
    """Placeholder for closure condition."""
    # Typically ~ phi_dot + psi_dot + lambda_dot (or more structured)
    raise NotImplementedError("Define Σ̇ for your system here.")
