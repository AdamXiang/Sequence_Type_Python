import math
import pytest
from custom_sequence.polygon import Polygon

REL_TOL = 1e-3
ABS_TOL = 1e-3


@pytest.mark.parametrize(
    "vertices, circumradius, expected",
    [
        # vertices, circumradius, (interior_angle, area, side_length, perimeter, apothem)
        (3, 1, (60, None, None, None, None)),                  # Triangle
        (4, 1, (90, 2.0, math.sqrt(2), 4 * math.sqrt(2), 0.707)),  # Square
        (6, 2, (120, 10.3923, 2, 12, 1.73205)),                 # Hexagon
    ],
)
def test_polygon_properties(vertices, circumradius, expected):
    polygon = Polygon(vertices, circumradius)

    # Unpack expected values
    interior_angle, area, side_length, perimeter, apothem = expected

    # Interior angle
    if interior_angle is not None:
        assert math.isclose(polygon.interior_angle, interior_angle, rel_tol=REL_TOL, abs_tol=ABS_TOL)

    # Area
    if area is not None:
        assert math.isclose(polygon.area, area, rel_tol=REL_TOL, abs_tol=ABS_TOL)

    # Side length
    if side_length is not None:
        assert math.isclose(polygon.side_length, side_length, rel_tol=REL_TOL, abs_tol=ABS_TOL)

    # Perimeter
    if perimeter is not None:
        assert math.isclose(polygon.perimeter, perimeter, rel_tol=REL_TOL, abs_tol=ABS_TOL)

    # Apothem
    if apothem is not None:
        assert math.isclose(polygon.apothem, apothem, rel_tol=REL_TOL, abs_tol=ABS_TOL)


def test_polygon_str():
    polygon = Polygon(3, 1)
    assert str(polygon) == "Polygon(vertices_number=3, circumradius=1)"


def test_polygon_vertex_and_edge_counts():
    polygon = Polygon(5, 10)
    assert polygon.count_vertices == 5
    assert polygon.count_edges == 5
    assert polygon.circumradius == 10
