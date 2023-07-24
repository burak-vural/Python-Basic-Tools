import os
from PIL import Image

# PNG uzantılı fotoğrafların bulunduğu klasörü belirtin.
directory = "/path/to/png/images"

# Tüm PNG uzantılı fotoğrafları listeleyin.
images = os.listdir(directory)

# Tüm PNG uzantılı fotoğrafları WEBP uzantısına dönüştürün.
for image in images:
    if image.endswith(".png"):
        im = Image.open(f"{directory}/{image}")
        im.save(f"{directory}/{image[:-4]}.webp", format="webp")

# Dönüştürme işleminin tamamlandığını bildirin.
print("Dönüştürme işlemi tamamlandı.")
