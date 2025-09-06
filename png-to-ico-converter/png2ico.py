#pip install pillow

import os
from PIL import Image

# Masaüstü yolu (kullanıcıya özel)
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
base_dir = os.path.join(desktop, "png-to-ico-converter")
png_dir = os.path.join(base_dir, "png")
ico_dir = os.path.join(base_dir, "ico")

# Klasörler yoksa oluştur
os.makedirs(png_dir, exist_ok=True)
os.makedirs(ico_dir, exist_ok=True)

# .png dosyalarını işle
for file_name in os.listdir(png_dir):
    if file_name.lower().endswith(".png"):
        png_path = os.path.join(png_dir, file_name)
        ico_name = os.path.splitext(file_name)[0] + ".ico"
        ico_path = os.path.join(ico_dir, ico_name)

        try:
            img = Image.open(png_path)
            img.save(ico_path, format='ICO', sizes=[(16, 16), (32, 32), (64, 64), (128, 128), (256, 256)])
            print(f"{ico_name} oluşturuldu.")
        except Exception as e:
            print(f"{file_name} dönüştürülürken hata oluştu: {e}")
