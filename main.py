menu = {
    "Dal Makhni": 120,
    "Aloo paratha": 40,
    "Jeera aloo": 80,
    "Lassi": 25,
    "Fahad": 0.2,
}

print("Aapka Swagat hai")
print("")
print("Dal Makhni: 120\nAloo paratha: 40\nJeera aloo: 80\nLassi: 25\nRasgulla: 15")

Order1 = input("kya khana chahenge? : ")

print("Your bill is: ", menu[Order1])
Order2 = input("Aur Kuch lenge? : ")
if Order1 != "Dal Makhni" and Order2 == "No":
    print("Your total bill is ", menu[Order1])

elif Order1 == "Dal Makhni" and Order2 == "No":
    print("Sorry sir, You Cant order just a Dal Makhni")
    print("Thank You")

else:
    total_bill = menu[Order1] + menu[Order2]
    Coupon = input("Do you have a coupon Code, if yes then enter it? :")
    if Coupon == "Fahad":
        disc_value = total_bill * menu[Coupon]
        print("Your bill after 20% Discount: ", total_bill - disc_value)
    else:
        print("Your total bill is: ", menu[Order1] + menu[Order2])

print("Thank you for ordering")
