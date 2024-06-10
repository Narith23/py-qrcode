# basic_qrcode

import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save(
    "basic_qrcode.png",
    scale=10,
    border=2,
)
