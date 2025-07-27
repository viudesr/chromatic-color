from chromatic_color import ChromaticColor


def test_white_record():
    ccolor = ChromaticColor(255, 255, 255)
    assert ccolor.get_rgb() == (255, 255, 255)