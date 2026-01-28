from solution import *
import math

def test_all():
    atlanta = City('Atlanta', 500000, 0.5)
    boston = City('Boston', 200000, 0.3)
    chicago = City('Chicago', 1000000, 0.7)
    denver = City('Denver', 300000, 0.4)
    el_paso = City('El Paso', 100000, 0.1)
    fargo = City('Fargo', 50000, 0.05)

    four_way_intersection = CityIntersection(
        CityIntersection(
            CityIntersection(
                None,
                None,
                atlanta,
                'FourWayIntersection',
            ),
            CityIntersection(
                None,
                None,
                boston,
                'FourWayIntersection',
            ),
            chicago,
            'FourWayIntersection',
        ),
        CityIntersection(
            CityIntersection(
                None,
                None,
                el_paso,
                'FourWayIntersection',
            ),
            None,
            denver,
            'FourWayIntersection',
        ),
        fargo,
        'FourWayIntersection',
    )
    visitor = TrafficAnalysisVisitor()

    four_way_intersection.accept(visitor)

    assert visitor.traffic_data['Chicago']['traffic_volume'] == 1000000 * \
        0.7 * 1.2, "Four-Way Intersection traffic calculation failed for Chicago."

    assert 'Atlanta' in visitor.traffic_data, "Atlanta not visited."
    assert 'Boston' in visitor.traffic_data, "Boston not visited."
    assert 'Denver' in visitor.traffic_data, "Denver not visited."
    assert 'El Paso' in visitor.traffic_data, "El Paso not visited."
    assert 'Fargo' in visitor.traffic_data, "Fargo not visited."

    roundabout_intersection = CityIntersection(
        None,
        None,
        boston,
        'Roundabout'
    )

    t_intersection = CityIntersection(
        None,
        None,
        denver,
        'TIntersection'
    )

    mixed_intersection = CityIntersection(
        roundabout_intersection,
        t_intersection,
        el_paso,
        'FourWayIntersection'
    )

    visitor = TrafficAnalysisVisitor()

    roundabout_intersection.accept(visitor)
    assert visitor.traffic_data['Boston']['traffic_volume'] == 200000 * \
        0.3 * 0.7, "Roundabout traffic calculation failed for Boston."

    t_intersection.accept(visitor)
    assert visitor.traffic_data['Denver']['traffic_volume'] == 300000 * \
        0.4 * 1.1, "T-Intersection traffic calculation failed for Denver."

    mixed_intersection.accept(visitor)
    assert visitor.traffic_data['El Paso']['traffic_volume'] == 100000 * \
        0.1 * 1.2, "Four-Way Intersection traffic calculation failed for El Paso."
    assert 'Boston' in visitor.traffic_data, "Boston not visited in mixed intersection."
    assert 'Denver' in visitor.traffic_data, "Denver not visited in mixed intersection."

    four_way_intersection.accept(visitor)
    assert 'Chicago' in visitor.traffic_data, "Chicago not visited in complex structure."
    assert 'Atlanta' in visitor.traffic_data, "Atlanta not visited in complex structure."
    assert 'Fargo' in visitor.traffic_data, "Fargo not visited in complex structure."

    simple_four_way = CityIntersection(
        None, None, atlanta, 'FourWayIntersection')
    simple_roundabout = CityIntersection(None, None, boston, 'Roundabout')
    simple_t_intersection = CityIntersection(
        None, None, chicago, 'TIntersection')

    nested_intersection_1 = CityIntersection(
        simple_four_way,
        simple_roundabout,
        denver,
        'Roundabout'
    )

    nested_intersection_2 = CityIntersection(
        simple_t_intersection,
        nested_intersection_1,
        el_paso,
        'TIntersection'
    )

    visitor = TrafficAnalysisVisitor()

    simple_four_way.accept(visitor)
    simple_roundabout.accept(visitor)
    simple_t_intersection.accept(visitor)

    assert visitor.traffic_data['Atlanta']['traffic_volume'] == 500000 * \
        0.5 * 1.2, "Four-Way Intersection traffic calculation failed for Atlanta."
    assert visitor.traffic_data['Boston']['traffic_volume'] == 200000 * \
        0.3 * 0.7, "Roundabout traffic calculation failed for Boston."
    assert visitor.traffic_data['Chicago']['traffic_volume'] == 1000000 * \
        0.7 * 1.1, "T-Intersection traffic calculation failed for Chicago."

    nested_intersection_1.accept(visitor)
    nested_intersection_2.accept(visitor)

    assert visitor.traffic_data['Denver']['traffic_volume'] == 300000 * 0.4 * \
        0.7, "Roundabout traffic calculation failed for Denver in nested intersection."
    assert visitor.traffic_data['El Paso']['traffic_volume'] == 100000 * 0.1 * \
        1.1, "T-Intersection traffic calculation failed for El Paso in nested intersection."

    assert 'Atlanta' in visitor.traffic_data, "Atlanta not visited in nested intersection."
    assert 'Boston' in visitor.traffic_data, "Boston not visited in nested intersection."
    assert 'Chicago' in visitor.traffic_data, "Chicago not visited in nested intersection."
    assert 'Denver' in visitor.traffic_data, "Denver not visited in nested intersection."
    assert 'El Paso' in visitor.traffic_data, "El Paso not visited in nested intersection."