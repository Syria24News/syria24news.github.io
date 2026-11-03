# يولّد favicon.ico (16/32/48) وicon-192.png وapple-touch-icon.png من أيقونة سوريا 24 في بلوجر
# المصدر نفسه الذي يستعمله القالب في <link rel="icon">؛ إن تغيّر الشعار عدّل SRC ثم شغّل المهمة يدوياً
import io
import urllib.request
from PIL import Image

SRC = ("https://blogger.googleusercontent.com/img/b/R29vZ2xl/"
       "AVvXsEjYYtt7ts1c5L9LAYrVjGj8xtmas33LIHPOabKyTKjBcLHRQLH7HTG21APEcEAizgO8TZlky0GTYnu3wD_CSn2kqdS8mGHESKjua8Lkca_cMMHJQOwrPJ5zlypgmDJj4_uzkJS4BJm42lYLB4RrPv-7Gi0i2X9KvFmVqvHDr5rfBkw0kFKLgeF3oX20pkqs/"
       "w512-h512-p-k-no-nu/s24-logo-favicon.png")

req = urllib.request.Request(SRC, headers={"User-Agent": "Syria24News-favicon/1.0"})
with urllib.request.urlopen(req, timeout=30) as r:
    data = r.read()

img = Image.open(io.BytesIO(data)).convert("RGBA")
if img.width < 48:
    raise SystemExit("الصورة المنزّلة صغيرة جداً: %dx%d" % img.size)

# favicon.ico متعدد الأحجام
img.save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

# أيقونة 192 للمتصفحات الحديثة، و180 لأجهزة آبل (بلا شفافية)
img.resize((192, 192), Image.LANCZOS).save("icon-192.png", optimize=True)
apple = Image.new("RGB", (180, 180), (255, 255, 255))
small = img.resize((180, 180), Image.LANCZOS)
apple.paste(small, (0, 0), small)
apple.save("apple-touch-icon.png", optimize=True)

print("تم: favicon.ico وicon-192.png وapple-touch-icon.png من صورة %dx%d" % img.size)
