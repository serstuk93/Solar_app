from geopy.geocoders import Nominatim
from time import strftime
from datetime import datetime, timedelta
from math import pi, cos, sin, acos, tan, radians, degrees, asin, copysign, atan2

# from dateutil import tz
import re
import pytz
from timezonefinder import TimezoneFinder


class CalcSol:
    def UTCcl(
        self, positionAA, selecteddate=""
    ):  # positionAA is name of town, select date is date from kivymd calendar
        geolocator = Nominatim(user_agent="anyName")
        tf = TimezoneFinder()
        self.coords = geolocator.geocode(positionAA)
        if self.coords == None:
            resres = "Adress not found"
            return resres
        self.timezone1 = tf.timezone_at(
            lng=self.coords.longitude, lat=self.coords.latitude
        )
        naive = datetime.now()
        tmzn = pytz.timezone(self.timezone1)
        self.aware1 = naive.astimezone(tmzn)

        cazon = re.split(r"(\D+)|(\D-)", str(self.aware1))
        if selecteddate != "":
            selecteddate = str(selecteddate)
            cazon[0] = str(selecteddate[0:4])
            cazon[3] = str(selecteddate[5:7])
            cazon[6] = str(selecteddate[8:])
        if selecteddate == "":
            cazon = re.split(r"(\D+)|(\D-)", str(self.aware1))
        self.caz1 = cazon
        # print("caz1", self.caz1)
        self.caz = cazon[-6] + cazon[-4] + cazon[-3] + cazon[-1]

    def calculations(self, positionAA):
        rok = int(self.caz1[0])
        mesiac = int(self.caz1[3])
        den = int(self.caz1[6])
        den_v_roku = int(strftime("%j"))
        # cas_zona = int(self.caz1[21])
        cas_zona = int(self.caz[:3])
        hodina = int(self.caz1[9])
        minuta = int(self.caz1[12])
        sekunda = int(self.caz1[15])
        # print("STRF",strftime("%z"))
        self.tzzzz =  cas_zona
        fr_rok = (2 * pi / 365) * (den_v_roku - 1 + (hodina - 12 / 24))
        cas = f"{hodina:02d}:{minuta:02d}:{sekunda:02d}"
        cas_val = (int(cas[0:2]) * 60 + int(cas[3:5])) / 24 / 60
        geolocator = Nominatim(user_agent="Sol_budik")
        location = geolocator.geocode(
            positionAA, language="en"
        )  # language set to ENGLISH
        if location == None:
            print("incorrect location")
            return None
        else:
            print(location)
        date_time_str = (
            f"{den:02d}/{mesiac:02d}/{rok} {hodina:02d}:{minuta:02d}:{sekunda:02d}"
        )
        date_time_str_sol = f"{hodina}:{minuta}:{sekunda}"
        date_time_obj = datetime.strptime(date_time_str, "%d/%m/%Y %H:%M:%S")
        date_time_sol = datetime.strptime(date_time_str_sol, "%H:%M:%S")
        time_delta_base = timedelta(
            hours=int(strftime("%H")),
            minutes=int(strftime("%M")),
            seconds=int(strftime("%S")),
        )
        time_delta_seconds = time_delta_base.total_seconds()
        time_delta_base = time_delta_base * 2
        time_delta_seconds = time_delta_seconds * 2

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
        julian_den = get_julian_datetime(example_datetime)

        jul_rok = (julian_den - 2451545) / 36525
        geomMeanLongSundeg = float(
            280.46646 + jul_rok * (36000.76983 + jul_rok * 0.0003032) % 360
        )
        geomMeanAnomSundeg = 357.52911 + jul_rok * (35999.05029 - 0.0001537 * jul_rok)
        eccentEarthOrbit = 0.016708634 - jul_rok * (
            0.000042037 + 0.0000001267 * jul_rok
        )
        sunEqofCtr = (
            sin(radians(geomMeanAnomSundeg))
            * (1.914602 - jul_rok * (0.004817 + 0.000014 * jul_rok))
            + sin(radians(2 * geomMeanAnomSundeg)) * (0.019993 - 0.000101 * jul_rok)
            + sin(radians(3 * geomMeanAnomSundeg)) * 0.000289
        )

        sunTrueLongdeg = geomMeanLongSundeg + sunEqofCtr
        sunTrueAnomdeg = geomMeanAnomSundeg + sunEqofCtr
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
        solar_noon_LST = (
            720 - 4 * location.longitude - eq_of_time_minutes + self.tzzzz * 60
        ) / 1440
        sunrise_time_LST = solar_noon_LST - ha_sunrise_deg * 4 / 1440
        sunset_time_LST = solar_noon_LST + ha_sunrise_deg * 4 / 1440
        sunlight_duration_minutes = 8 * ha_sunrise_deg
        true_solar_time_min = (
            cas_val * 1440 + eq_of_time_minutes + 4 * location.longitude - 60 * 1
        ) % 1440
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
        sunrise_time_LST = sunrise_time_LST.split(":", maxsplit=2)
        sunrise_time_LST = ":".join(sunrise_time_LST[0:2])
        sunset_time_LST = str(timedelta(days=sunset_time_LST, seconds=0))[0:9]
        sunset_time_LST = sunset_time_LST.split(":", maxsplit=2)
        sunset_time_LST = ":".join(sunset_time_LST[0:2])
        solar_noon_LST = str(timedelta(days=solar_noon_LST, seconds=0))[0:9]
        solar_noon_LST = solar_noon_LST.split(":", maxsplit=2)
        solar_noon_LST = ":".join(solar_noon_LST[0:2])

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
       # print(resres)
        return resres


if __name__ == "__main__":
    d = CalcSol()
  #  d.UTCcl("tokio")
   # d.calculations("tokio")
   # d.UTCcl("sabinov")
   # d.calculations("sabinov")
  #  d.UTCcl("new york")
  #  d.calculations("new york")

