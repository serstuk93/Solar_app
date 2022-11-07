from mimetypes import init
from PIL import Image, ImageOps

# from io import BytesIO
# from PIL import ImageDraw


class MapLocator:
    def __init__(
        self,
        latt=0,
        lng=0,
    ):
        """ "
        generating map image.
        first argument is lattitude, second longtitude
        """
        self.lng = lng
        self.latt = latt

    def image_merger(self):  # merge 2 images with scale
        self.pin_img = Image.open("p5.png", mode="r", formats=None).convert('RGBA')
        size = self.pin_img.size
        #print(size)
        self.pin_img = ImageOps.fit(
            self.pin_img, (25, 25), method=0, bleed=0.0, centering=(0.0, 0.0)
        ).convert('RGBA')
        size = (1000, 500)
        self.temp_img = Image.new("RGBA", size, (0, 0, 0, 0))
       # temp_img.show() 
        self.temp_img.paste(self.pin_img, self.pixel_coords())

    
        self.image = Image.open("temp.jpg", mode="r", formats=None)
        self.image = ImageOps.fit(self.image, size, bleed=0.0, centering=(0.5, 0.5)).convert('RGBA')



    def pixel_coords(
        self,
    ):  # calculate pixel coordinates for selected location to draw pin

        # long lat
        # max long 0 , 365  | or -365 ,0
        # max lat <85, -85>
        # long = val modulo 360 / 360 * 1000 pixels minus size of pin img
        # lat = val modulo 85 / 170 * 500 pixels minus size of pin img
        # sb 49,21  lat long
        # london 51,0
        # tokio 35,140
        # NY 42 ,-71
        # cape town -34,18

        y, x = 49 * -1 + 84, 0
        y, x = float(self.latt) * -1 + 84, float(self.lng)
        long = int((x % 360 / 360 * 1000 + 500) - 12.5) % 1000
        lat = int(((((y % 170) / 170) * 500) - 12.5) % 500)
        locat = (long, lat)
        #print(locat)
        return locat

    def img_map_generator(self):  # merge 2 images and return location

        self.image_merger()
        self.imgl = "t1.png"
        m_img = Image.alpha_composite(self.image, self.temp_img)
        #m_img.show()
        m_img = m_img.save(self.imgl)
        return "t1.png"


if __name__ == "__main__":
    d = MapLocator(35, 139.5)
    d.img_map_generator()
