print("---Stock Transaction Program---")
purchasePrice = 40 * 2000
purchasecommision = purchasePrice * 0.03

salePrice = 42.75 * 2000
saleCommision = salePrice * 0.03

print(f"""
Joe Paid ${purchasePrice:,.2f} for the stocks with a ${purchasecommision:,.2f} commision
---
Joe made ${salePrice:,.2f} on the stocks with a ${saleCommision:,.2f} commision
---
After paying the commission, Joe made ${(salePrice + saleCommision)-(purchasePrice + purchasecommision):,.2f}
""")