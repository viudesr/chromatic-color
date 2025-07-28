import pytest
from chromatic_color import ChromaticColor


def test_white_record():
    ccolor = ChromaticColor(255, 255, 255)
    assert ccolor.get_rgb() == (255, 255, 255)

def test_grey_record():
    ccolor = ChromaticColor(128, 128, 128)
    assert ccolor.get_rgb() == (128, 128, 128)

def test_black_record():
    ccolor = ChromaticColor(0, 0, 0)
    assert ccolor.get_rgb() == (0, 0, 0)

def test_red_record():
    ccolor = ChromaticColor(255, 0, 0)
    assert ccolor.get_rgb() == (255, 0, 0)

def test_blue_record():
    ccolor = ChromaticColor(0, 255, 0)
    assert ccolor.get_rgb() == (0, 255, 0)

def test_green_record():
    ccolor = ChromaticColor(0, 0, 255)
    assert ccolor.get_rgb() == (0, 0, 255)

def test_zero_red():
    ccolor = ChromaticColor(0, 255, 255)
    assert ccolor.get_rgb() == (0, 255, 255)

def test_zero_green():
    ccolor = ChromaticColor(255, 0, 255)
    assert ccolor.get_rgb() == (255, 0, 255)

def test_zero_blue():
    ccolor = ChromaticColor(255, 255, 0)
    assert ccolor.get_rgb() == (255, 255, 0)

def test_negative_red():
    with pytest.raises(ValueError):
        ChromaticColor(-1, 255, 255)

def test_negative_blue():
    with pytest.raises(ValueError) as excinfo:
        ChromaticColor(255, -1, 255)
    assert excinfo.type is ValueError

def test_negative_green():
    with pytest.raises(ValueError) as excinfo:
        ChromaticColor(255, 255, -1)
    assert excinfo.type is ValueError

def test_toobig_red():
    with pytest.raises(ValueError) as excinfo:
        ChromaticColor(256, 255, 255)
    assert excinfo.type is ValueError

def test_toobig_blue():
    with pytest.raises(ValueError) as excinfo:
        ChromaticColor(255, 256, 255)
    assert excinfo.type is ValueError

def test_toobig_green():
    with pytest.raises(ValueError) as excinfo:
        ChromaticColor(255, 255, 256)
    assert excinfo.type is ValueError

def test_dec_red():
    with pytest.raises(TypeError) as excinfo:
        ChromaticColor(128.5, 255, 255)
    assert excinfo.type is TypeError

def test_dec_blue():
    with pytest.raises(TypeError) as excinfo:
        ChromaticColor(255, 128.5, 255)
    assert excinfo.type is TypeError

def test_dec_green():
    with pytest.raises(TypeError) as excinfo:
        ChromaticColor(255, 255, 128.5)
    assert excinfo.type is TypeError
