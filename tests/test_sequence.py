import pytest
import custom_sequence.polygon import Polygon

def test_polygon():
    # Due to float operation property, we need to use isclose function in math module
    relative_tolerance = 0.001
    absolute_tolerance = 0.001

    vertices_number = 3
    circumradius = 1

    polygon = Polygon(vertices_number, circumradius)

    assert str(polygon) == f'Polygon(vertices_number=3, circumradius=1)'
    assert polygon.count_vertices == vertices_number, (f'Actual: {polygon.count_vertices},'
                                                        f'Expected: {vertices_number}')
    assert polygon.count_edges == vertices_number
    assert polygon.circumradius == circumradius
    assert math.isclose(polygon.interior_angle, 60)

    # Change the properties
    vertices_number = 4
    circumradius = 1

    polygon = Polygon(vertices_number, circumradius)
    assert math.isclose(polygon.interior_angle, 90)
    assert math.isclose(polygon.area, 2.0, 
                        rel_tol=relative_tolerance,
                        abs_tol=absolute_tolerance), (f'Actual: {polygon.area},'
                                                        f'Expected: 2.0')
    assert math.isclose(polygon.side_length, math.sqrt(2), 
                        rel_tol=relative_tolerance,
                        abs_tol=absolute_tolerance)

    assert math.isclose(polygon.perimeter, 4 * math.sqrt(2),
                        rel_tol=relative_tolerance,
                        abs_tol=absolute_tolerance)

    assert math.isclose(polygon.apothem, 0.707,
                        rel_tol=relative_tolerance,
                        abs_tol=absolute_tolerance)

    # Do more test
    vertices_number = 6
    circumradius = 2

    polygon = Polygon(vertices_number, circumradius)
    assert math.isclose(polygon.interior_angle, 120)
    assert math.isclose(polygon.area, 10.3923, 
                        rel_tol=relative_tolerance,
                        abs_tol=absolute_tolerance), (f'Actual: {polygon.area},'
                                                        f'Expected: 10.3923')
    assert math.isclose(polygon.side_length, 2, 
                        rel_tol=relative_tolerance,
                        abs_tol=absolute_tolerance)

    assert math.isclose(polygon.perimeter, 12,
                        rel_tol=relative_tolerance,
                        abs_tol=absolute_tolerance)

    assert math.isclose(polygon.apothem, 1.73205,
                        rel_tol=relative_tolerance,
                        abs_tol=absolute_tolerance)