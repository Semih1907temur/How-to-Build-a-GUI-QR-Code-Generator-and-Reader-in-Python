import qrcode  # QR kod kütüphanesini ekler.

# Kullanıcıdan QR kod için metin alır.
data = input("Enter the text to generate QR code: ")

# QR kodu oluşturur ve yapılandırır.
qr = qrcode.QRCode(
    version=1,  # Boyut ve karmaşıklık için versiyon belirler.
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi.
    box_size=10,  # QR kod kutucuklarının boyutu.
    border=4,  # Çerçeve kalınlığı.
)
qr.add_data(data)  # QR koduna metni ekler.
qr.make(fit=True)  # Boyutlandırmayı otomatik yapar.

# QR kodu bir görüntü olarak oluşturur.
img = qr.make_image(fill_color="black", back_color="white")

# QR kodu dosya olarak kaydeder.
img.save("simple_qr_code.png")
print("QR Code saved as simple_qr_code.png")
