# -*- coding: UTF-8 -*-

# Filename : sql_util.py
# author by : WeiQi

import qrcode
ipa="https://fir.im/z1n5"
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_L,
                 box_size=8,
                 border=8,
                 )
qr.add_data(ipa)
qr.make(fit=True)
img=qr.make_image()
img.save('ios_qr_code.png')