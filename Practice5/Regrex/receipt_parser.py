import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    receipt = f.read()




blocks = re.split(r"\n\d+\.\n", receipt)[1:] 

products = []
prices = []

for block in blocks:
    lines = block.strip().splitlines()

    price_line = lines[-1].replace(" ", "").replace(",", ".")
    try:
        price = float(price_line)
    except ValueError:
        continue
    prices.append(price)
    
    name_lines = [l for l in lines[:-1] if "x" not in l and "Стоимость" not in l]
    name = " ".join(name_lines).strip()
    products.append(name)



total_amount = sum(prices)



date_time_pattern = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", receipt)
date = date_time_pattern.group(1)
time = date_time_pattern.group(2)



payment_pattern = re.search(r"Банковская карта|Наличные|CASH|CARD", receipt, re.IGNORECASE)
payment_method = payment_pattern.group() if payment_pattern else ""



receipt_data = {
    "products": products,
    "prices": prices,
    "total": total_amount,
    "date": date,
    "time": time,
    "payment_method": payment_method
}

print(json.dumps(receipt_data, indent=4, ensure_ascii=False))