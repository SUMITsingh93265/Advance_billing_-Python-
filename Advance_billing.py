# Input product
import time

product_list = []
product_quantity = []
counter = 1
# Product Input
print("******************************************************************")
print("********************** Billing system **********************")
print("******************************************************************")
print()
print("******************************************************************")
print("********************** Product section **********************")
print("******************************************************************")
print()
while True:
    product = input(f"Enter your {counter} product : ")
    product_list.append(product)
    quantity = int(input("Enter the quantity of the product : "))
    product_quantity.append(quantity)
    counter = counter + 1
    add_product = input("Do you want to add more item [Yes or No] : ")
    if add_product.capitalize() == "No":
        break

# Price input
print()
print("******************************************************************")
print("********************** Price section **********************")
print("******************************************************************")
print()
price_list = []
for i in range(len(product_quantity)):
    price = float(input(f"Enter price of the {product_list[i]} : "))
    quan = price * product_quantity[i]
    price_list.append(quan)

# Product list
print()
print("******************************************************************")
print("********************** Product list **********************")
print("******************************************************************")
print()
product_counter = 1
for i in range(len(product_list)):
    print(
        f"{product_counter}. {product_list[i]}. Qt {product_quantity[i]} = ₹ {price_list[i]}\-"
    )
    product_counter = product_counter + 1

# Pricing section
total_price = 0
for i in range(len(price_list)):
    total_price = total_price + price_list[i]

# GST section
print()
print("******************************************************************")
print("********************** Pricing section **********************")
print("******************************************************************")
print()
print("*Note = If you select option 'No' then it will not add to your bill.")
gst = input("Do you want to add GST in your bill [Yes or No] : ")
if gst.capitalize() == "Yes":
    gst_percent = input("Enter GST % = ")
    print()
    gst_amount = total_price * (float(gst_percent) / 100)
    total_price_with_gst = total_price + gst_amount
    print(f"GST percent = {gst_percent}%")
    print(f"Bill amount = ₹ {total_price}\-")
    print(f"GST amount = ₹ {gst_amount}\-")
    print("******************************************************************")
    print(f"Total price with GST = ₹ {total_price_with_gst}\-")
    print("******************************************************************")
elif gst.capitalize() == "No":
    print("GST amount is ₹ 0\-")
    print(f"Bill amount = ₹ {total_price}\-")
    print("******************************************************************")
    print(f"Total price without GST = ₹ {total_price}\-")
    print("******************************************************************")
else:
    print("Something went wrong.")

# Offer section
print()
print("******************************************************************")
print("********************** Offer section **********************")
print("******************************************************************")
print()
offer_list = [5, 10, 15]
offer = float(
    input(
        "Press 1 for 5% off, Press 2 for 10% off, Press 3 for 15% off or Press 0 for 'No discount' or even you can enter the discount : "
    ))
print()
if offer == 0:
    print("No discount on your bill.")
    print(f"Total bill to pay ₹ {total_price}\-")
elif offer == 1:
    print(f"Yehh! you receive {offer_list[0]}% flat off on your purcahse.")
    offer_bill = total_price_with_gst * (float(offer_list[0]) / 100)
    offer_bill_amount = total_price_with_gst - offer_bill
    print(
        f"Discount price is ₹ {offer_bill}\-. Pay only ₹ {offer_bill_amount}\-."
    )
elif offer == 2:
    print(f"Yehh! you receive {offer_list[1]}% flat off on your purcahse.")
    offer_bill = total_price_with_gst * (float(offer_list[1]) / 100)
    offer_bill_amount = total_price_with_gst - offer_bill
    print(
        f"Discount price is ₹ {offer_bill}\-. Pay only ₹ {offer_bill_amount}\-."
    )
elif offer == 3:
    print(f"Yehh! you receive {offer_list[2]}% flat off on your purcahse.")
    offer_bill = total_price_with_gst * (float(offer_list[2]) / 100)
    offer_bill_amount = total_price_with_gst - offer_bill
    print(
        f"Discount price is ₹ {offer_bill}\-. Pay only ₹ {offer_bill_amount}\-."
    )
elif offer > 15 and offer <= 100:
    offer_list.append(offer)
    print(f"Yehh! you receive {offer_list[-1]}% flat off on your purcahse.")
    offer_bill = total_price_with_gst * (float(offer_list[-1]) / 100)
    offer_bill_amount = total_price_with_gst - offer_bill
    print(
        f"Discount price is ₹ {offer_bill}\-. Pay only ₹ {offer_bill_amount}\-."
    )

# Date and time of shopping
print()
print("******************************************************************")
print(
    "********************** Date and time of shopping **********************")
print("******************************************************************")
print("Date and time of shoppig.")
date = time.strftime("%c")
Time = time.strftime("%H:%M:%S")
print(f"Date :- {date}")
print(f"Time :- {Time}")
print()
print("******************************************************************")
print("********************** Thanks for using **********************")
print("******************************************************************")