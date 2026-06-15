import qrcode

# Taking UPI ID as input
upi_id = input("Enter your UPI ID = ")

# Payment URLs
phonepe_url = f"upi://pay?pa={upi_id}&pn=RecipientName&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=RecipientName&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=RecipientName&mc=1234"

# Create QR codes
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save QR codes
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

#Display te QR Codes (you may need to install PIL/Pillow Library)
phonepe_qr.show()
paytm_qr.show
google_pay_qr.show
