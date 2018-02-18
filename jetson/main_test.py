import time
import libraries.gps as gps
import libraries.imu as imu
import libraries.car as car
import libraries.bearings as bearings
import libraries.pid as lpid
import libraries.cv as cv
from libraries.settings import *

centerOfTrack=[-27.8556425,153.151405]


waypoints = [[-27.8552175, 153.1511374],
            [-27.8554650, 153.1516188],
            [-27.8557407, 153.1520735],
            [-27.8560205, 153.1521694],
            [-27.8560920, 153.1519464],
            [-27.8559772, 153.1513396],
            [-27.8555771, 153.1508628],
            [-27.8553002, 153.1509104]]



        #[[-27.8552616667, 153.151291667],
            #[-27.8553216667, 153.151405],
            #[-27.8554266667, 153.151566667],
            #[-27.8555, 153.151725],
            #[-27.8555866667, 153.15189],
            #[-27.8557016667, 153.152083333],
            #[-27.855865, 153.152198333],
            #[-27.85597, 153.152228333],
            #[-27.8560216667, 153.152198333],
            #[-27.8560783333, 153.15216],
            #[-27.8561183333, 153.15206],
            #[-27.85611, 153.151958333],
            #[-27.856065, 153.151771667],
            #[-27.85603, 153.151628333],
            #[-27.8560016667, 153.151535],
            #[-27.85596, 153.151348333],
            #[-27.85584, 153.151086667],
            #[-27.8555833333, 153.150935],
            #[-27.8554083333, 153.150948333],
            #[-27.8553283333, 153.150986667],
            #[-27.8552716667, 153.151021667],
            #[-27.855235, 153.151121667]]

car.acceleration(1)





def follow_blob():
    while cv.are_blobs():
        car.steer(cv.get_biggest_blob_x())
        car.send()



def getCoords():
    gps_success = False
    while not gps_success:
        gps_success, coords = gps.getGPS()
    return coords

def follow_point(point):
    # Try and get GPS coordinates
    coords=getCoords()
    while bearings.coord_dist_meters(coords[0], coords[1], point[0], point[1]) > DIST_THRES_METER:
        # Get current coords long and lat
        coords=getCoords()
        if bearings.coord_dist_meters(coords[0], coords[1],centerOfTrack[0],centerOfTrack[1])>TRACK_RADIUS:#check if car is out of the track, if so stop car and wait
            car.stop()
            car.send()
            print("OUT OF TRACK, KILLING ALL SYSTEMS")
            input()
        
        
        ###########ADD BLOB IF STATMENT/DETECTION HERE
        if cv.are_blobs():
            follow_blob()
        ##  driveToBlob()   goto blob until blob dissapears then return to main loop
        
        # Calculate bearing
        coordsDirection = bearings.coord_bearing_degrees(coords[0], coords[1],  # Our location
                                                         point[0], point[1])   # waypoint location
        coordsAngleError = bearings.subtract_angles(coordsDirection,imu.getCompass())#calculate steering error
        
        #print("Current Compass: ",imu.getCompass()," Coord angle: ",coordsDirection," Steer Error: ",coordsAngleError," Distance to target: ",bearings.coord_dist_meters(coords[0], coords[1], point[0], point[1]))
        print("Steering error:",coordsAngleError)
        car.steer(coordsAngleError)
        
        
        car.send()
        time.sleep(0.01)


if __name__ == '__main__':
    while True:
        for point in waypoints:
            follow_point(point)
            print("FLOWING WAYPOINT:",point)

    #car.stop()
    #car.send()
