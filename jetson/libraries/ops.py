import math


def coord_bearing_degrees(lat1, long1, lat2, long2):
    """
    Calculates the bearing between two points. Returns in degrees.

    Formula:

    theta = atan2(sin(Δlong).cos(lat2),
                  cos(lat1).sin(lat2) - sin(lat1).cos(lat2).cos(Δlong))
    """
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    diffLong = math.radians(long1 - long2)

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
                                           * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)

    # We now have the initial beating but math.atan2 returns
    # values from -180 to 180 which isn't what we want for a compass
    # beating, solution is to normalize it
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing


def coord_bearing_radians(lat1, long1, lat2, long2):
    """
    Calculates the bearing between two points. Returns in radians.

    Formula:

    theta = atan2(sin(Δlong).cos(lat2),
                  cos(lat1).sin(lat2) - sin(lat1).cos(lat2).cos(Δlong))
    """
    deg = coord_bearing_degrees(lat1, long1, lat2, long2)
    return math.radians(deg)
