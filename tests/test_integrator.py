from fieldviz_mini import spiral_sink
from fieldviz_mini.integrators import integrate_streamline

def test_streamline_runs():
    field = spiral_sink()
    traj = integrate_streamline(field, 1.0, 1.0, steps=10)
    assert traj.shape == (11, 2)
