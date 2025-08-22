import pytest
import custom_sequence.polygon import Polygon

def test_polygon():
    vertices_number = 3
    circumradius = 1

    polygon = Polygon(vertices_number, circumradius)

    assert str(polygon) == f'Polygon(vertices_number=3, circumradius=1)'
    