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
        self.pin_img = Image.open("pin.png", mode="r", formats=None)
        size = self.pin_img.size
        # print(size)
        self.pin_img = ImageOps.fit(
            self.pin_img, (25, 25), method=0, bleed=0.0, centering=(0.0, 0.0)
        )
        size = (1000, 500)
        self.image = Image.open("temp.jpg", mode="r", formats=None)
        self.image = ImageOps.fit(self.image, size, bleed=0.0, centering=(0.5, 0.5))

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
        long = (int(x % 360 / 360 * 1000 + 500) - 12) % 1000
        lat = (int(((y % 170) / 170) * 500) - 12) % 500
        locat = (long, lat)
        # print(locat)
        return locat

    def img_map_generator(self):  # merge 2 images and return location

        self.image_merger()
        self.imgl = "t1.jpg"
        self.image.paste(self.pin_img, self.pixel_coords())
        self.image = self.image.save(self.imgl)

        """   # create memory location of image without physical storing it 
        import io
        # BytesIO is a fake file stored in memory
        imgByteArr = io.BytesIO()
        # image.save expects a file as a argument, passing a bytes io ins
        self.image.save(imgByteArr, format='PNG')
        # Turn the BytesIO object back into a bytes object
        imgByteArr = imgByteArr.getvalue()
        ss = Image.open(io.BytesIO(imgByteArr))
        print("SS",ss)
        # ss.show()
        """

        return "t1.jpg"

        """ # create new image for testing 
        image = Image.new("RGB", (300, 50))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), "This text is drawn on image")
        byte_io = BytesIO()
        image.save(byte_io, 'PNG')
        image.show()
        """


if __name__ == "__main__":
    print("A")
    d = MapLocator(35, 140)
    d.img_map_generator()
