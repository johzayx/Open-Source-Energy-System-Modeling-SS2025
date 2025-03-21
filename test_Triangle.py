from Triangle import angle_Alpha, side_b, side_c, area


def test_angle_Alpha():
    assert angle_Alpha(30, 80) == 60


def test_side_b():
    assert side_b(3, 30, 80) == 3


def test_side_c():
    assert side_c(3, 30, 80) == 2


def test_area():
    assert area(3, 5, 60) == 7
