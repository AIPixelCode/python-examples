# Vehicle Inheritance Hierarchy

## Description

This program demonstrates class inheritance and multiple inheritance in Python by modeling different types of vehicles.

The implementation defines a hierarchy of vehicle classes, where common attributes are shared through inheritance while specialized vehicle types introduce their own properties. It also demonstrates constructor chaining using `super()` across multiple levels of inheritance.

## How It Works

The program begins with a base `Vehicle` class that stores the common attributes shared by all vehicles, including the name, price, seating capacity, and maximum speed.

Two specialized classes, `GroundVehicle` and `FlyingVehicle`, inherit from `Vehicle` and extend it with properties specific to ground and flying vehicles.

The `Airplane` class inherits from both `GroundVehicle` and `FlyingVehicle`, combining the characteristics of each parent class while introducing additional information such as the airline, crew size, and captain.

Finally, the `B707` class represents a specific airplane model by inheriting all functionality from the `Airplane` class.

## Example

The following example creates a Boeing 707 object by providing all required vehicle, ground vehicle, flying vehicle, and airplane attributes.

The resulting object contains information inherited from every class in the hierarchy, including its general vehicle properties, ground and flying characteristics, and airline-specific details.

## Source Code

**Files:** 2_vehicle_inheritance_hierarchy.py
---

#### Author: AiPixelCode
