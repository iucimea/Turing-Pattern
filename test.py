import turing
from hypothesis import strategies as st
from hypothesis import settings
from hypothesis import given


@given(n=st.integers(1, turing.config_read('configuration.txt')[0]))
@settings(max_examples=1)
def test_starting_state(n):
    # Initializing the model with random concentration values"
    model = turing.starting_state(n)[0]
    # Test if the dimension of the lattice is n x n."
    assert len(model) == n
    assert len(model[0]) == n


if __name__ == "main":
    pass
