import qrcode

# Kullanıcıdan bir URL adresi isteyin.
url = input("Bir URL adresi girin: ")

# URL'yi QR koduna dönüştürün.
qr_code = qrcode.make(url)

# QR kodunu bir dosyaya kaydedin.
qr_code.save("qr_code.png")

# Kullanıcıya QR kodunun kaydedildiğini bildirin.
print("QR kodu başarıyla kaydedildi.")
