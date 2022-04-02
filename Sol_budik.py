from geopy.geocoders import Nominatim
from time import strftime
from datetime import datetime, timedelta
from math import pi , cos , sin , acos , tan , radians, degrees , asin , copysign , atan2
from dateutil import tz

class UTCcalc:

    def UTCcl(self,adresa):

        from timezonefinder import TimezoneFinder
        from pytz import timezone
        geolocator = Nominatim(user_agent="anyName")
        tf = TimezoneFinder()

        coords = geolocator.geocode(adresa)
        self.timezone1 = tf.timezone_at(lng=coords.longitude, lat=coords.latitude)
        print("ajooj",self.timezone1)
        import pytz
        eastern = timezone(self.timezone1)
        print(eastern.zone)
        fmt = '%Y-%m-%d %H:%M:%S %Z%z'
        loc_dt = eastern.localize(datetime(2022, 3, 22, 11, 30, 0))
        loc_dt = eastern.localize(datetime.utcnow())
        naive = datetime.now()
        print("locdt",loc_dt)
        ams_dt = loc_dt.astimezone(eastern)
        ams_dt.strftime(fmt)
        print(ams_dt.strftime(fmt))
        #konvertuj na lokalny cas
        tmzn = pytz.timezone(self.timezone1)
        print(tmzn, "tmzn")
        aware1 = naive.astimezone(tmzn)
        lokltime = loc_dt.astimezone(tmzn)
        print(aware1,"upraveny cas")

class CalcSol:

    def calculations(self, positionAA):

        x = strftime("%a, %d %b %Y %H:%M:%S")
        rok = int(strftime("%y"))
        mesiac = int(strftime("%m"))
        den = int(strftime("%d"))
        den_v_roku = int(strftime("%j"))
        cas_zona = int(strftime("%z"))
        hodina = int(strftime("%H"))
        minuta =int(strftime("%M"))
        sekunda  = int(strftime("%S"))
        print(den)
        print(x)
        print("cas zona",strftime("%z"))

        if strftime("%z")[0]=="+":
            cas_zona = int(strftime("%z")[1:3])
            print("c1",cas_zona)
        else:
            cas_zona = -abs(int(strftime("%z")[1:3]))
            print("c",cas_zona)
        self.tzzzz= cas_zona
        print(rok, mesiac, den , cas_zona, den_v_roku, hodina)
        fr_rok = (2 * pi / 365) * ( den_v_roku -1 + (hodina -12 / 24))
        print(fr_rok)
        cas= (strftime("%H:%M:%S"))
        cas_val = (int(cas[0:2])*60+int(cas[3:5]))/24/60
        print(cas_val,  "Cas val")
        print(cas )
        print("cas",cas[0:2])
        geolocator = Nominatim(user_agent="Sol_budik")
        location = geolocator.geocode(positionAA)
        if location == None:
            print("nespravna lokacia")
            return None
        else:
             print(location)
        print(location.address)
        print((location.latitude, location.longitude))
        svet_sirka = location.longitude
        # eq_time = 229.18* radians(0.000075+ 0.001868* cos(fr_rok) - 0.032077* sin(fr_rok)
        #                    -0.014615*cos(2*(fr_rok))-0.040849*sin(2*(fr_rok)))
        # decl_ang= 0.006918-0.399912*cos(fr_rok)+0.070257*sin(fr_rok)-0.006758*cos(2*fr_rok)+\
        #           0.000907*sin(2*fr_rok)-0.002697*cos(3*fr_rok)+0.00148*sin(3*fr_rok)
        # print(decl_ang)
        # print("eq time", eq_time)
        #
        # solarny_cas = eq_time + 4*svet_sirka - 60*cas_zona
        # print("time offset",solarny_cas)
        # tst= hodina *60 + minuta  +sekunda/60 + solarny_cas
        #
        # sol_hod_uhol = (tst /4)-180
        # sol_zenit = sin(location.latitude)* sin(decl_ang)+cos(location.latitude)*cos(decl_ang)*cos(sol_hod_uhol)
        #
        # sol_azimut = (- sin(location.latitude)* sol_zenit - sin(decl_ang))/cos(location.latitude)*sin(sol_zenit)
        #
        # print(sol_zenit,sol_azimut)
        #
        # ha = ( (cos(90.833)/(cos(location.latitude)*cos(decl_ang)))-tan(location.latitude)*tan(decl_ang)  )
        # sunrise= 720-4*(location.longitude+ ha) - eq_time
        # snoon = 720-4*(location.longitude) - eq_time
        # print(ha)
        # print("sun",sunrise,snoon)
        #
        #
        # t1 = (23.45)* sin( 360/degrees(365)*(70+284))
        # t2= (284+75)* (360/365)
        # t3 = sin(t2)
        # t4 = 23.45*(360*(80-70)/degrees(365))
        # print(t1, t2 ,t3,t4)
        # print(degrees(decl_ang))
        # #t5 = degrees(asin(sin(radians(R2))*sin(radians(P2))))



        date_time_str = f'{den}/{mesiac}/{rok} {hodina}:{minuta}:{sekunda}'
        date_time_str_sol = f'{hodina}:{minuta}:{sekunda}'
        print(date_time_str)
        print(type(date_time_str))
        print(date_time_str_sol)
        date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
        print('The type of the date is now', type(date_time_obj))
        print(date_time_obj)
        date_time_sol=datetime.strptime(date_time_str_sol, '%H:%M:%S')

        print(date_time_sol)
        time_delta_base =  timedelta (hours=int(strftime("%H")), minutes=int(strftime("%M")), seconds=int(strftime("%S")))
        time_delta_seconds = time_delta_base.total_seconds()
        print("base", time_delta_base )
        time_delta_base = time_delta_base*2
        print("base2", time_delta_base )
        print("1x", time_delta_seconds)
        time_delta_seconds= time_delta_seconds *2
        print("2x",time_delta_seconds)

        date1= JD = 367 * rok - 7 * (rok + (mesiac + 9)/12)/4 + 275 * mesiac/9 + den + 1721014
        print(date1)
        def get_julian_datetime(date):
            """
            Convert a datetime object into julian float.
            Args:
                date: datetime-object of date in question

            Returns: float - Julian calculated datetime.
            Raises:
                TypeError : Incorrect parameter type
                ValueError: Date out of range of equation
            """

            # Ensure correct format
            if not isinstance(date, datetime):
                raise TypeError('Invalid type for parameter "date" - expecting datetime')
            elif date.year < 1801 or date.year > 2099:
                raise ValueError('Datetime must be between year 1801 and 2099')

            # Perform the calculation
            julian_datetime = 367 * date.year - int((7 * (date.year + int((date.month + 9) / 12.0))) / 4.0) + int(
                (275 * date.month) / 9.0) + date.day + 1721013.5 + (
                                  date.hour + date.minute / 60.0 + date.second / pow(60,
                                                                                          2)) / 24.0 - 0.5 * copysign(
                1, 100 * date.year + date.month - 190002.5) + 0.5

            return julian_datetime

        #example_datetime = datetime(2022, 3, 11, 7, 30, 0)
        example_datetime = date_time_obj
        print (get_julian_datetime(example_datetime))
        julian_den = get_julian_datetime(example_datetime)

        jul_rok = (julian_den-2451545)/36525
        print(jul_rok, "jul rok ")

        geomMeanLongSundeg = float(280.46646+jul_rok*(36000.76983+jul_rok*0.0003032)%360)
        print("geomMeanlongSun OK ", geomMeanLongSundeg)
        geomMeanAnomSundeg = 357.52911+jul_rok*(35999.05029-0.0001537*jul_rok)
        print("geomMeanAnomSun OK  ", geomMeanAnomSundeg)
        eccentEarthOrbit= 0.016708634-jul_rok*(0.000042037+0.0000001267*jul_rok)
        print("eccentEarthOrbit OK", eccentEarthOrbit)
        sunEqofCtr=sin(radians(geomMeanAnomSundeg))*(1.914602-jul_rok*(0.004817+0.000014*jul_rok))+sin(radians(2*geomMeanAnomSundeg))*(0.019993-0.000101*jul_rok)+sin(radians(3*geomMeanAnomSundeg))*0.000289
        print("sunEqofCtr OK",sunEqofCtr)

        sunTrueLongdeg= geomMeanLongSundeg+ sunEqofCtr
        print('sunTrueLongdeg OK ',sunTrueLongdeg)
        sunTrueAnomdeg= geomMeanAnomSundeg + sunEqofCtr
        print('sunTrueAnomdeg OK ', sunTrueAnomdeg)
        test_long = location.latitude
        print(type(test_long))
        sun_rad_vector_AUs= (1.000001018*(1-eccentEarthOrbit*eccentEarthOrbit))/(1+eccentEarthOrbit*cos(radians(sunTrueAnomdeg)))
        sun_app_long_deg = sunTrueLongdeg-0.00569-0.00478*sin(radians(125.04-1934.136*jul_rok))
        mean_obliq_ecliptic_deg =23+(26+((21.448-jul_rok*(46.815+jul_rok*(0.00059-jul_rok*0.001813))))/60)/60
        obliq_corr_deg =mean_obliq_ecliptic_deg+0.00256*cos(radians(125.04-1934.136*jul_rok))
        sun_rt_ascen_deg =degrees(atan2(cos(radians(obliq_corr_deg))*sin(radians(sun_app_long_deg)),cos(radians(sun_app_long_deg))))
        print("!!!!!!!!",
            degrees(
            atan2(
                cos(radians(obliq_corr_deg)) * sin(radians(sun_app_long_deg)), (cos(radians(sun_app_long_deg)))
            )
            ))
        print(

                    cos(radians(obliq_corr_deg)) * sin(radians(sun_app_long_deg)), (cos(radians(sun_app_long_deg)))
                )

        print(degrees(atan2(cos(radians(obliq_corr_deg)) * sin(radians(sun_app_long_deg)), (cos(radians(sun_app_long_deg))))))
        sun_declin_deg =degrees(asin(sin(radians(obliq_corr_deg))*sin(radians(sun_app_long_deg))))
        var_y =tan(radians(obliq_corr_deg/2))*tan(radians(obliq_corr_deg/2))
        eq_of_time_minutes =4*degrees(var_y*sin(2*radians(geomMeanLongSundeg))-2*eccentEarthOrbit*sin(radians(geomMeanAnomSundeg))+4*eccentEarthOrbit*var_y*sin(radians(geomMeanAnomSundeg))*cos(2*radians(geomMeanLongSundeg))-0.5*var_y*var_y*sin(4*radians(geomMeanLongSundeg))-1.25*eccentEarthOrbit*eccentEarthOrbit*sin(2*radians(geomMeanAnomSundeg)))
        ha_sunrise_deg=degrees(acos(cos(radians(90.833))/(cos(radians(location.latitude))*cos(radians(sun_declin_deg)))-tan(radians(location.latitude))*tan(radians(sun_declin_deg))))
        print(ha_sunrise_deg, "ha_sunrise_deg")
        print(
            sun_rad_vector_AUs,"sun_rad_vector_AUs OK ",sun_app_long_deg ,"sun_app_long_deg OK",mean_obliq_ecliptic_deg, "mean_obliq_ecliptic_deg OK ",
        )
        print(
            obliq_corr_deg,"obliq_corr_deg", sun_rt_ascen_deg,"sun_rt_ascen_deg ", sun_declin_deg,"sun_declin_deg  ", var_y,"var_y  ",
            eq_of_time_minutes,"eq_of_time_minutes  ",
        )
        solar_noon_LST=(720-4*location.longitude-eq_of_time_minutes+cas_zona*60)/1440
        print(solar_noon_LST, "solar_noon_LST")
        sunrise_time_LST=solar_noon_LST-ha_sunrise_deg*4/1440
        print(sunrise_time_LST,"Sunrise")
        sunset_time_LST=solar_noon_LST+ha_sunrise_deg*4/1440
        print(sunset_time_LST, "sunset_time_LST")
        sunlight_duration_minutes=8*ha_sunrise_deg
        print(sunlight_duration_minutes, "sunlight_duration_minutes")
        print("eq",eq_of_time_minutes)
        print(type(cas))
        true_solar_time_min=(cas_val*1440+eq_of_time_minutes+4*location.longitude-60*1)%1440
        print(true_solar_time_min,"true_solar_time_min")
        if true_solar_time_min/4<0:
            hour_angle_deg=true_solar_time_min/4+180
        else:
            hour_angle_deg = true_solar_time_min / 4 - 180
        solar_zenith_angle_deg=degrees(acos(sin(radians(location.latitude))*sin(radians(sun_declin_deg))+cos(radians(location.latitude))*cos(radians(sun_declin_deg))*cos(radians(hour_angle_deg))))
        solar_elevation_angle_deg=90-solar_zenith_angle_deg
        if solar_elevation_angle_deg>85:
            approx_atmospheric_refraction_deg=0
        elif solar_elevation_angle_deg>5:
            approx_atmospheric_refraction_deg=(58.1/tan(radians(solar_elevation_angle_deg))-0.07/pow(tan(radians(solar_elevation_angle_deg)),3)+0.000086/pow(tan(radians(solar_elevation_angle_deg)),5))/3600
        elif solar_elevation_angle_deg>-0.575:
            approx_atmospheric_refraction_deg =(1735+solar_elevation_angle_deg*(-518.2+solar_elevation_angle_deg*(103.4+solar_elevation_angle_deg*(-12.79+solar_elevation_angle_deg*0.711))))/3600
        else:
            approx_atmospheric_refraction_deg =-20.772 /tan(radians(solar_elevation_angle_deg)) / 3600

        # IF(AE2>85;0;IF(AE2>5;58,1/TAN(RADIANS(AE2))-0,07/POWER(TAN(RADIANS(AE2));3)+0,000086/POWER(TAN(RADIANS(AE2));5);
        #  IF(AE2>-0,575;1735+AE2*(-518,2+AE2*(103,4+AE2*(-12,79+AE2*0,711)));-20,772/TAN(RADIANS(AE2)))))/3600
        solar_elevation_corrected_for_atm_refraction_deg= solar_elevation_angle_deg+ approx_atmospheric_refraction_deg

        if hour_angle_deg>0:
            solar_azimuth_angle_deg_cwfrom_N=(degrees(acos(((sin(radians(location.latitude))*cos(radians(solar_zenith_angle_deg)))-sin(radians(sun_declin_deg)))/(cos(radians(location.latitude))*sin(radians(solar_zenith_angle_deg)))))+180%360)
        else:
            solar_azimuth_angle_deg_cwfrom_N=(540-degrees(acos(((sin(radians(location.latitude))*cos(radians(solar_zenith_angle_deg)))-sin(radians(sun_declin_deg)))/(cos(radians(location.latitude))*sin(radians(solar_zenith_angle_deg)))))%360)

        # IF(AC2>0;MOD(DEGREES(ACOS(((SIN(RADIANS($B$3))*COS(RADIANS(AD2)))-SIN(RADIANS(T2)))/(COS(RADIANS($B$3))*SIN(RADIANS(AD2)))))+180;360);
        # MOD(540-DEGREES(ACOS(((SIN(RADIANS($B$3))*COS(RADIANS(AD2)))-SIN(RADIANS(T2)))/(COS(RADIANS($B$3))*SIN(RADIANS(AD2)))));360))

        sunrise_time_LST= str(timedelta(days=sunrise_time_LST, seconds=0))[0:9]
        print("split", sunrise_time_LST)
        print(type(sunrise_time_LST))
        sunrise_time_LST= sunrise_time_LST.split(":",maxsplit=2)
        sunrise_time_LST=":".join(sunrise_time_LST[0:2])
        print("split", sunrise_time_LST)
        print(type(sunrise_time_LST))
        sunset_time_LST = str(timedelta(days=sunset_time_LST, seconds=0))[0:9]
        sunset_time_LST = sunset_time_LST.split(":", maxsplit=2)
        sunset_time_LST = ":".join(sunset_time_LST[0:2])
        solar_noon_LST = str(timedelta(days=solar_noon_LST, seconds=0))[0:9]
        solar_noon_LST = solar_noon_LST.split(":", maxsplit=2)
        solar_noon_LST = ":".join(solar_noon_LST[0:2])

        rerere= str("sabinooov")
        resres= [location.address, location.latitude, location.longitude,
                geomMeanLongSundeg, geomMeanAnomSundeg, eccentEarthOrbit,
                sunEqofCtr,sunTrueLongdeg, sunTrueAnomdeg,
                sun_app_long_deg, mean_obliq_ecliptic_deg,
                obliq_corr_deg, sun_rt_ascen_deg, sun_declin_deg,
                eq_of_time_minutes,ha_sunrise_deg, solar_noon_LST,
                sunrise_time_LST, sunset_time_LST,sunlight_duration_minutes,
                date_time_str
                ]
        resres = [ str(x) for x in resres]
        print(len(resres))
        return resres

            #str(location)
           # "tu som ",
          #  type(str(location)),



d = CalcSol()
d.calculations("sabinov")

#my_locat= CalcSol("sabinov")
#my_locat.calculations("sabinov")