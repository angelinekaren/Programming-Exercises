def calc_weight_on_planet(weight, surface_gravity=23.1):
    weight_on_planet = (weight / 9.8) * surface_gravity
    print(weight_on_planet)

calc_weight_on_planet(120, 9.8)
calc_weight_on_planet(120)
calc_weight_on_planet(120, 23.1)

