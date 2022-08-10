from geopy.geocoders import Nominatim
from time import strftime
from datetime import datetime, timedelta
from math import pi, cos, sin, acos, tan, radians, degrees, asin, copysign, atan2

# from dateutil import tz
import re
import pytz
from timezonefinder import TimezoneFinder


class CalcSol:
    def UTCcl(self, positionAA, selecteddate=""):

        geolocator = Nominatim(user_agent="anyName")
        tf = TimezoneFinder()
        # location = geolocator.geocode(positionAA)
        # print(location.address)
        self.coords = geolocator.geocode(positionAA)
        print("coords", self.coords)
        if self.coords == None:
            resres = "Zadané mesto nenájdené"
            return resres
        self.timezone1 = tf.timezone_at(
            lng=self.coords.longitude, lat=self.coords.latitude
        )
        print("ajooj", self.timezone1)
        naive = datetime.now()
        tmzn = pytz.timezone(self.timezone1)
        print(tmzn, "tmzn")
        self.aware1 = naive.astimezone(tmzn)
        print(self.aware1, "upraveny cas")

        cazon = re.split(r"(\D+)|(\D-)", str(self.aware1))
        print("ojojo", selecteddate)
        if selecteddate != "":
            # selecteddate =selecteddate.split("-")

            print("seeeer", selecteddate)
            selecteddate = str(selecteddate)
            print(type(selecteddate))
            print(type(cazon))
            cazon[0] = str(selecteddate[0:4])
            cazon[3] = str(selecteddate[5:7])
            cazon[6] = str(selecteddate[8:])
        if selecteddate == "":
            print("serss")
            cazon = re.split(r"(\D+)|(\D-)", str(self.aware1))
        self.caz1 = cazon
        print(self.caz1)
        print(cazon)
        cazon = cazon[-6] + cazon[-4] + cazon[-3] + cazon[-1]
        print("cazon", cazon)
        self.caz = cazon

    def calculations(self, positionAA):
        # x = strftime("%a, %d %b %Y %H:%M:%S")
        # rok = int(strftime("%y"))
        # print(type(rok))
        # mesiac = int(strftime("%m"))
        # den = int(strftime("%d"))
        # den_v_roku = int(strftime("%j"))
        # cas_zona = int(strftime("%z"))
        # hodina = int(strftime("%H"))
        # minuta =int(strftime("%M"))
        # sekunda  = int(strftime("%S"))

        # x = strftime("%a, %d %m %Y %H:%M:%S")
        # print("X",x)
        # print(type(x))
        # print("CC",self.caz1)
        rok = int(self.caz1[0])
        mesiac = int(self.caz1[3])
        den = int(self.caz1[6])
        den_v_roku = int(strftime("%j"))
        cas_zona = int(self.caz1[21])
        print(cas_zona, "caz zona")
        hodina = int(self.caz1[9])
        minuta = int(self.caz1[12])
        sekunda = int(self.caz1[15])
        print(den)

        print("cas zona", strftime("%z"))

        if strftime("%z")[0] == "+":
            cas_zona = int(strftime("%z")[1:3])
            print("c1", cas_zona)
        else:
            cas_zona = -abs(int(strftime("%z")[1:3]))
            print("c", cas_zona)
        self.tzzzz = float(cas_zona)
        print(self.tzzzz, "tzzz")
        print(type(self.tzzzz))
        self.tzzzz = self.caz1[19] + str(cas_zona)
        print(self.tzzzz, "tzzz")
        self.tzzzz = int(self.tzzzz)
        print(self.tzzzz, "tzzz")
        print(rok, mesiac, den, self.tzzzz, den_v_roku, hodina)
        fr_rok = (2 * pi / 365) * (den_v_roku - 1 + (hodina - 12 / 24))
        print("fr_rok", fr_rok)
        # cas= (strftime("%H:%M:%S"))
        # cas=(hodina+":"+minuta+":"+sekunda+":")
        cas = f"{hodina:02d}:{minuta:02d}:{sekunda:02d}"
        print(cas[0:2], cas[3:5])
        cas_val = (int(cas[0:2]) * 60 + int(cas[3:5])) / 24 / 60
        print("2")
        print(cas_val, "Cas val")
        print(cas)
        print("cas", cas[0:2])
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
        date_time_str = (
            f"{den:02d}/{mesiac:02d}/{rok} {hodina:02d}:{minuta:02d}:{sekunda:02d}"
        )
        date_time_str_sol = f"{hodina}:{minuta}:{sekunda}"
        print(date_time_str)
        print(type(date_time_str))
        print(date_time_str_sol)
        date_time_obj = datetime.strptime(date_time_str, "%d/%m/%Y %H:%M:%S")
        print("The type of the date is now", type(date_time_obj))
        print(date_time_obj)
        date_time_sol = datetime.strptime(date_time_str_sol, "%H:%M:%S")

        print(date_time_sol)
        time_delta_base = timedelta(
            hours=int(strftime("%H")),
            minutes=int(strftime("%M")),
            seconds=int(strftime("%S")),
        )
        time_delta_seconds = time_delta_base.total_seconds()
        print("base", time_delta_base)
        time_delta_base = time_delta_base * 2
        print("base2", time_delta_base)
        print("1x", time_delta_seconds)
        time_delta_seconds = time_delta_seconds * 2
        print("2x", time_delta_seconds)

        date1 = JD = (
            367 * rok
            - 7 * (rok + (mesiac + 9) / 12) / 4
            + 275 * mesiac / 9
            + den
            + 1721014
        )
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
                raise TypeError(
                    'Invalid type for parameter "date" - expecting datetime'
                )
            elif date.year < 1801 or date.year > 2099:
                raise ValueError("Datetime must be between year 1801 and 2099")

            # Perform the calculation
            julian_datetime = (
                367 * date.year
                - int((7 * (date.year + int((date.month + 9) / 12.0))) / 4.0)
                + int((275 * date.month) / 9.0)
                + date.day
                + 1721013.5
                + (date.hour + date.minute / 60.0 + date.second / pow(60, 2)) / 24.0
                - 0.5 * copysign(1, 100 * date.year + date.month - 190002.5)
                + 0.5
            )

            return julian_datetime

        # example_datetime = datetime(2022, 3, 11, 7, 30, 0)
        example_datetime = date_time_obj
        print(get_julian_datetime(example_datetime))
        julian_den = get_julian_datetime(example_datetime)

        jul_rok = (julian_den - 2451545) / 36525
        print(jul_rok, "jul rok ")

        geomMeanLongSundeg = float(
            280.46646 + jul_rok * (36000.76983 + jul_rok * 0.0003032) % 360
        )
        print("geomMeanlongSun OK ", geomMeanLongSundeg)
        geomMeanAnomSundeg = 357.52911 + jul_rok * (35999.05029 - 0.0001537 * jul_rok)
        print("geomMeanAnomSun OK  ", geomMeanAnomSundeg)
        eccentEarthOrbit = 0.016708634 - jul_rok * (
            0.000042037 + 0.0000001267 * jul_rok
        )
        print("eccentEarthOrbit OK", eccentEarthOrbit)
        sunEqofCtr = (
            sin(radians(geomMeanAnomSundeg))
            * (1.914602 - jul_rok * (0.004817 + 0.000014 * jul_rok))
            + sin(radians(2 * geomMeanAnomSundeg)) * (0.019993 - 0.000101 * jul_rok)
            + sin(radians(3 * geomMeanAnomSundeg)) * 0.000289
        )
        print("sunEqofCtr OK", sunEqofCtr)

        sunTrueLongdeg = geomMeanLongSundeg + sunEqofCtr
        print("sunTrueLongdeg OK ", sunTrueLongdeg)
        sunTrueAnomdeg = geomMeanAnomSundeg + sunEqofCtr
        print("sunTrueAnomdeg OK ", sunTrueAnomdeg)
        test_long = location.latitude
        print(type(test_long))
        sun_rad_vector_AUs = (
            1.000001018 * (1 - eccentEarthOrbit * eccentEarthOrbit)
        ) / (1 + eccentEarthOrbit * cos(radians(sunTrueAnomdeg)))
        sun_app_long_deg = (
            sunTrueLongdeg
            - 0.00569
            - 0.00478 * sin(radians(125.04 - 1934.136 * jul_rok))
        )
        mean_obliq_ecliptic_deg = (
            23
            + (
                26
                + (
                    (
                        21.448
                        - jul_rok * (46.815 + jul_rok * (0.00059 - jul_rok * 0.001813))
                    )
                )
                / 60
            )
            / 60
        )
        obliq_corr_deg = mean_obliq_ecliptic_deg + 0.00256 * cos(
            radians(125.04 - 1934.136 * jul_rok)
        )
        sun_rt_ascen_deg = degrees(
            atan2(
                cos(radians(obliq_corr_deg)) * sin(radians(sun_app_long_deg)),
                cos(radians(sun_app_long_deg)),
            )
        )
        print(
            "!!!!!!!!",
            degrees(
                atan2(
                    cos(radians(obliq_corr_deg)) * sin(radians(sun_app_long_deg)),
                    (cos(radians(sun_app_long_deg))),
                )
            ),
        )
        print(
            cos(radians(obliq_corr_deg)) * sin(radians(sun_app_long_deg)),
            (cos(radians(sun_app_long_deg))),
        )

        print(
            degrees(
                atan2(
                    cos(radians(obliq_corr_deg)) * sin(radians(sun_app_long_deg)),
                    (cos(radians(sun_app_long_deg))),
                )
            )
        )
        sun_declin_deg = degrees(
            asin(sin(radians(obliq_corr_deg)) * sin(radians(sun_app_long_deg)))
        )
        var_y = tan(radians(obliq_corr_deg / 2)) * tan(radians(obliq_corr_deg / 2))
        eq_of_time_minutes = 4 * degrees(
            var_y * sin(2 * radians(geomMeanLongSundeg))
            - 2 * eccentEarthOrbit * sin(radians(geomMeanAnomSundeg))
            + 4
            * eccentEarthOrbit
            * var_y
            * sin(radians(geomMeanAnomSundeg))
            * cos(2 * radians(geomMeanLongSundeg))
            - 0.5 * var_y * var_y * sin(4 * radians(geomMeanLongSundeg))
            - 1.25
            * eccentEarthOrbit
            * eccentEarthOrbit
            * sin(2 * radians(geomMeanAnomSundeg))
        )
        ha_sunrise_deg = degrees(
            acos(
                cos(radians(90.833))
                / (cos(radians(location.latitude)) * cos(radians(sun_declin_deg)))
                - tan(radians(location.latitude)) * tan(radians(sun_declin_deg))
            )
        )
        print(ha_sunrise_deg, "ha_sunrise_deg")
        print(
            sun_rad_vector_AUs,
            "sun_rad_vector_AUs OK ",
            sun_app_long_deg,
            "sun_app_long_deg OK",
            mean_obliq_ecliptic_deg,
            "mean_obliq_ecliptic_deg OK ",
        )
        print(
            obliq_corr_deg,
            "obliq_corr_deg",
            sun_rt_ascen_deg,
            "sun_rt_ascen_deg ",
            sun_declin_deg,
            "sun_declin_deg  ",
            var_y,
            "var_y  ",
            eq_of_time_minutes,
            "eq_of_time_minutes  ",
        )
        solar_noon_LST = (
            720 - 4 * location.longitude - eq_of_time_minutes + self.tzzzz * 60
        ) / 1440
        print(solar_noon_LST, "solar_noon_LST")
        sunrise_time_LST = solar_noon_LST - ha_sunrise_deg * 4 / 1440
        print(sunrise_time_LST, "Sunrise")
        sunset_time_LST = solar_noon_LST + ha_sunrise_deg * 4 / 1440
        print(sunset_time_LST, "sunset_time_LST")
        sunlight_duration_minutes = 8 * ha_sunrise_deg
        print(sunlight_duration_minutes, "sunlight_duration_minutes")
        print("eq", eq_of_time_minutes)
        print(type(cas))
        true_solar_time_min = (
            cas_val * 1440 + eq_of_time_minutes + 4 * location.longitude - 60 * 1
        ) % 1440
        print(true_solar_time_min, "true_solar_time_min")
        if true_solar_time_min / 4 < 0:
            hour_angle_deg = true_solar_time_min / 4 + 180
        else:
            hour_angle_deg = true_solar_time_min / 4 - 180
        solar_zenith_angle_deg = degrees(
            acos(
                sin(radians(location.latitude)) * sin(radians(sun_declin_deg))
                + cos(radians(location.latitude))
                * cos(radians(sun_declin_deg))
                * cos(radians(hour_angle_deg))
            )
        )
        solar_elevation_angle_deg = 90 - solar_zenith_angle_deg
        if solar_elevation_angle_deg > 85:
            approx_atmospheric_refraction_deg = 0
        elif solar_elevation_angle_deg > 5:
            approx_atmospheric_refraction_deg = (
                58.1 / tan(radians(solar_elevation_angle_deg))
                - 0.07 / pow(tan(radians(solar_elevation_angle_deg)), 3)
                + 0.000086 / pow(tan(radians(solar_elevation_angle_deg)), 5)
            ) / 3600
        elif solar_elevation_angle_deg > -0.575:
            approx_atmospheric_refraction_deg = (
                1735
                + solar_elevation_angle_deg
                * (
                    -518.2
                    + solar_elevation_angle_deg
                    * (
                        103.4
                        + solar_elevation_angle_deg
                        * (-12.79 + solar_elevation_angle_deg * 0.711)
                    )
                )
            ) / 3600
        else:
            approx_atmospheric_refraction_deg = (
                -20.772 / tan(radians(solar_elevation_angle_deg)) / 3600
            )

        # IF(AE2>85;0;IF(AE2>5;58,1/TAN(RADIANS(AE2))-0,07/POWER(TAN(RADIANS(AE2));3)+0,000086/POWER(TAN(RADIANS(AE2));5);
        #  IF(AE2>-0,575;1735+AE2*(-518,2+AE2*(103,4+AE2*(-12,79+AE2*0,711)));-20,772/TAN(RADIANS(AE2)))))/3600
        solar_elevation_corrected_for_atm_refraction_deg = (
            solar_elevation_angle_deg + approx_atmospheric_refraction_deg
        )

        if hour_angle_deg > 0:
            solar_azimuth_angle_deg_cwfrom_N = (
                degrees(
                    acos(
                        (
                            (
                                sin(radians(location.latitude))
                                * cos(radians(solar_zenith_angle_deg))
                            )
                            - sin(radians(sun_declin_deg))
                        )
                        / (
                            cos(radians(location.latitude))
                            * sin(radians(solar_zenith_angle_deg))
                        )
                    )
                )
                + 180 % 360
            )
        else:
            solar_azimuth_angle_deg_cwfrom_N = (
                540
                - degrees(
                    acos(
                        (
                            (
                                sin(radians(location.latitude))
                                * cos(radians(solar_zenith_angle_deg))
                            )
                            - sin(radians(sun_declin_deg))
                        )
                        / (
                            cos(radians(location.latitude))
                            * sin(radians(solar_zenith_angle_deg))
                        )
                    )
                )
                % 360
            )

        # IF(AC2>0;MOD(DEGREES(ACOS(((SIN(RADIANS($B$3))*COS(RADIANS(AD2)))-SIN(RADIANS(T2)))/(COS(RADIANS($B$3))*SIN(RADIANS(AD2)))))+180;360);
        # MOD(540-DEGREES(ACOS(((SIN(RADIANS($B$3))*COS(RADIANS(AD2)))-SIN(RADIANS(T2)))/(COS(RADIANS($B$3))*SIN(RADIANS(AD2)))));360))

        sunrise_time_LST = str(timedelta(days=sunrise_time_LST, seconds=0))[0:9]
        print("split", sunrise_time_LST)
        print(type(sunrise_time_LST))
        sunrise_time_LST = sunrise_time_LST.split(":", maxsplit=2)
        sunrise_time_LST = ":".join(sunrise_time_LST[0:2])
        print("split", sunrise_time_LST)
        print(type(sunrise_time_LST))
        sunset_time_LST = str(timedelta(days=sunset_time_LST, seconds=0))[0:9]
        sunset_time_LST = sunset_time_LST.split(":", maxsplit=2)
        sunset_time_LST = ":".join(sunset_time_LST[0:2])
        solar_noon_LST = str(timedelta(days=solar_noon_LST, seconds=0))[0:9]
        solar_noon_LST = solar_noon_LST.split(":", maxsplit=2)
        solar_noon_LST = ":".join(solar_noon_LST[0:2])

        rerere = str("sabinooov")
        resres = [
            location.address,
            location.latitude,
            location.longitude,
            geomMeanLongSundeg,
            geomMeanAnomSundeg,
            eccentEarthOrbit,
            sunEqofCtr,
            sunTrueLongdeg,
            sunTrueAnomdeg,
            sun_app_long_deg,
            mean_obliq_ecliptic_deg,
            obliq_corr_deg,
            sun_rt_ascen_deg,
            sun_declin_deg,
            eq_of_time_minutes,
            ha_sunrise_deg,
            solar_noon_LST,
            sunrise_time_LST,
            sunset_time_LST,
            sunlight_duration_minutes,
            date_time_str,
        ]
        resres = [str(x) for x in resres]
        print(len(resres))
        return resres

        # str(location)
        # "tu som ",
        #  type(str(location)),


d = CalcSol()
d.UTCcl("sabinov")
# d.calculations("sabinov")

# my_locat= CalcSol("sabinov")
# my_locat.calculations("sabinov")
