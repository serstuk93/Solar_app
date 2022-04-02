# from datetime import datetime
# from geopy.geocoders import GoogleV3
# from geopy.point import Point
# geocoder = GoogleV3()
# geocoder.timezone(Point(40.7410861, -73.9896297241625), time=datetime.utcnow())
#
from datetime import datetime
print(datetime.utcnow())

from Sol_budik import UTCcalc
xy = UTCcalc()
xy.UTCcl("sydney")

print(xy)


