from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import car_chase_simulation

def test_car_chase_basic():
    car = {
        'weight': 1500,
        'tire_friction': 1.0,
        'aerodynamic_profile': 0.35
    }
    surface = {
        'friction_coefficient': 0.9
    }
    weather = {
        'wind_speed': 0,
        'rain_intensity': 0
    }
    speed = 30
    other_objects = [ 
        {'position': 100}
    ]
    result = car_chase_simulation(car, surface, weather, speed, other_objects)
    assert result['final_speed'] < speed
    assert result['potential_collision'] == False

def test_car_chase_with_collision():
    car = {
        'weight': 1500,
        'tire_friction': 1.0,
        'aerodynamic_profile': 0.35
    }
    surface = {
        'friction_coefficient': 0.9
    }
    weather = {
        'wind_speed': 0,
        'rain_intensity': 0
    }
    speed = 30
    other_objects = [ 
        {'position': 15}
    ]
    result = car_chase_simulation(car, surface, weather, speed, other_objects)
    assert result['final_speed'] < speed
    assert result['potential_collision'] == True

def test_car_chase_with_wind():
    car = {
        'weight': 1500,
        'tire_friction': 1.0,
        'aerodynamic_profile': 0.35
    }
    surface = {
        'friction_coefficient': 0.9
    }
    weather = {
        'wind_speed': 10,
        'rain_intensity': 0
    }
    speed = 30
    other_objects = [ 
        {'position': 100}
    ]
    result = car_chase_simulation(car, surface, weather, speed, other_objects)
    assert result['final_speed'] < speed
    assert result['potential_collision'] == False

def test_car_chase_with_rain():
    car = {
        'weight': 1500,
        'tire_friction': 1.0,
        'aerodynamic_profile': 0.35
    }
    surface = {
        'friction_coefficient': 0.9
    }
    weather = {
        'wind_speed': 0,
        'rain_intensity': 0.5
    }
    speed = 30
    other_objects = [ 
        {'position': 100}
    ]
    result = car_chase_simulation(car, surface, weather, speed, other_objects)
    assert result['final_speed'] < speed
    assert result['potential_collision'] == False