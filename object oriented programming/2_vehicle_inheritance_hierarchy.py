class Vehicle:
    def __init__(self, name, price, number_of_seats, max_speed):
        self.name = name
        self.price = price
        self.number_of_seats = number_of_seats
        self.max_speed = max_speed


class GroundVehicle(Vehicle):
    def __init__(self, number_of_wheels, steering_wheel, **kwargs):
        super().__init__(**kwargs)
        self.number_of_wheels = number_of_wheels
        self.steering_wheel = steering_wheel


class FlyingVehicle(Vehicle):
    def __init__(self, fuel, number_of_fins, **kwargs):
        super().__init__(**kwargs)
        self.fuel = fuel
        self.number_of_fins = number_of_fins


class Airplane(GroundVehicle, FlyingVehicle):
    def __init__(self, airline, number_of_crew, captain, **kwargs):
        super().__init__(**kwargs)
        self.airline = airline
        self.number_of_crew = number_of_crew
        self.captain = captain


class B707(Airplane):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
