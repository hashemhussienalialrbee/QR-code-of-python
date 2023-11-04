import qrcode 
qrcodeimag=qrcode.make('https://www.linkedin.com/in/hashem-hussein-a304b424a')
qrcodeimag.save('qrimages/linkedin.jpg')
inst=qrcode.make('https://instagram.com/hashamalrabee?igshid=ZDc4ODBmNjlmNQ==')
inst.save('qrimages/instagram.jpg')

inst=qrcode.make('https://www.facebook.com/profile.php?id=100086883750820&mibextid=9R9pXO')
inst.save('qrimages/facebook.jpg')

inst=qrcode.make('https://www.snap')
inst.save('qrimages/snap.jpg')
"""
inst=qrcode.make('https://instagram.com/hashamalrabee?igshid=ZDc4ODBmNjlmNQ==')
inst.save('qrimages/snap.jpg')
"""