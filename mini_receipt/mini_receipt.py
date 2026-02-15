import sys

max_str_length = 20

product1_name = input("Podaj nazwę pierwszego produktu: ")[:max_str_length]
product1_name = product1_name.lower().capitalize()
product1_price = float(input("Podaj cenę produktu: ").replace(",","."))
product1_price = round(product1_price, 2)
product1_amount = int(input("Podaj ilość: "))

product2_name = input("Podaj nazwę drugiego produktu: ")[:max_str_length]
product2_name = product2_name.lower().capitalize()
product2_price = float(input("Podaj cenę produktu: ").replace(",","."))
product2_price = round(product2_price, 2)
product2_amount = int(input("Podaj ilość: "))

product3_name = input("Podaj nazwę trzeciego produktu: ")[:max_str_length]
product3_name = product3_name.lower().capitalize()
product3_price = float(input("Podaj cenę produktu: ").replace(",","."))
product3_price = round(product3_price, 2)
product3_amount = int(input("Podaj ilość: "))

if product1_amount <= 0 or product2_amount <= 0 or product3_amount <= 0:
    print("Wprowadzono nieprawidłową ilość produktu")
    sys.exit()

product1_total_price = product1_price * product1_amount
product2_total_price = product2_price * product2_amount
product3_total_price = product3_price * product3_amount

sum_netto = product1_total_price + product2_total_price + product3_total_price
vat_sum = sum_netto * 0.23
sum_brutto = sum_netto + vat_sum

print(f"{'=' * 14} PARAGON {'=' * 14}")
print("NAZWA".ljust(20), "ILOŚĆ".rjust(5), "BRUTTO".rjust(9))
print('-' * 36)
print(f"{product1_name.ljust(20)} {str(product1_amount).rjust(4)} {product1_total_price:>10.2f}")
print(f"{product2_name.ljust(20)} {str(product2_amount).rjust(4)} {product2_total_price:>10.2f}")
print(f"{product3_name.ljust(20)} {str(product3_amount).rjust(4)} {product3_total_price:>10.2f}")
print('-' * 36)
print(f"{'SUMA NETTO:'.ljust(25)}{sum_netto:>10.2f}")
print(f"{'SUMA VAT (23%):'.ljust(25)}{vat_sum:>10.2f}")
print(f"{'SUMA BRUTTO:'.ljust(25)}{sum_brutto:>10.2f}")
print('=' * 36)