import time
import libraries.gps as gps
import libraries.imu as imu
import libraries.car as car
import libraries.bearings as bearings

car.send()
waypoint = [-27.855488, 153.150894]


while True:
    # Try and get GPS coordinates
    try:
        gps_success, coords = gps.getGPS()

        if not gps_success:
            print('GPS Error')
            continue

        # Get current coords long and lat
        # Calculate bearing
        coords = [coords.latitude, coords.longitude]
        coordsDirection = bearings.coord_bearing_degrees(
            coords[0], coords[1], waypoint[0], waypoint[1])
        coordsError = coordsDirection - imu.getCompass()
        car.steer(coordsError)
        car.send()
        print(coordsDirection, imu.getCompass(), coordsError)

    except KeyboardInterrupt:
        break

    time.sleep(0.001)
