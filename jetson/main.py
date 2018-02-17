import numpy as np
import time
import libraries.settings as lsettings
import libraries.gps as gps
import libraries.imu as imu
import libraries.car as car
import libraries.bearings as bearings
import libraries.pid as lpid

import libraries.geometry as geo

# Lat, Long
waypoints = [[-27.855488, 153.150894], [-27.855488, 153.150894]]

pid_cross = lpid.PID(P=2.0, I=0.001, D=0.001)
pid_steer = lpid.PID(P=1.5, T=0.001, D=0.002)

car.send()
car.acceleration(25)


def follow_point(point1, point2):
    gps_success = False
    while not gps_success:
        gps_success, coords = gps.getGPS()

    # Last point
    if point2 is None:
        point2 = point1

    dist_to_p1 = coord_dist_meters(point1[0], point1[1], coord[0], coord[1])
    dist_to_p2 = coord_dist_meters(point2[0], point2[1], coord[0], coord[1])

    while dist_to_p1 < lsettings.DIST_THRES_METER or dist_to_p2 < lsettings.DIST_THRES_METER:
        # Calculate cross track distance
        cross_track_dist = geo.cross_track_distance(
            point1[0],
            point1[1],
            point2[0],
            point2[1],
            coord[0],
            coord[1]
        )

        # Update PID
        pid_cross.update(cross_track_dist)

        # Get desired error
        desired_heading = pid_cross.predict()

        # Get current coords long and lat
        # Calculate bearing
        actual_heading = bearings.coord_bearing_degrees(coords[0], coords[1],  # Our location
                                                        point[0], point[1])    # waypoint location

        # Get yaw rate of change
        yaw_roc = imu.get_yaw_roc()

        # Second PID
        error_heading = (actual_heading + desired_heading) - imu.getCompass()

        pid_steer.update(error_heading, delta_term=yaw_roc)

        # Steering
        steering_tuned = pid_steer.predict()
        car.steer(steering_tuned)
        car.send()

        # 30 updates per second
        time.sleep(0.033)

        # Check position
        gps_success = False
        while not gps_success:
            gps_success, coords = gps.getGPS()

        dist_to_p1 = coord_dist_meters(
            point1[0], point1[1], coord[0], coord[1])
        dist_to_p2 = coord_dist_meters(
            point2[0], point2[1], coord[0], coord[1])


if __name__ == '__main__':
    for point1, point2 in zip(waypoints, waypoints[1:] + None):
        follow_point(point1, point2)

    car.stop()
    car.send()
