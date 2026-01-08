from fieldviz_mini import spiral_sink

def test_eval():
    field = spiral_sink()
    fx, fy = field.func(1.0, -1.0)
    assert isinstance(fx, float)
    assert isinstance(fy, float)
