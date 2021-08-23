import time
import random

#offers = ["21%", "91%", "87%", "3%", "90%", "10%", "96%", "16%", "54%", "74%", "62%", "98%", "100%", "200%", "14%", "154%", "134%", "199%", "0%"]

companies = ["VUE Shop system", "amazon", "myntra", "google ads", "flipkart", "xbox", "ps5"]

offers_choose = random.randrange(1, 100)

companies_choose = random.choice(companies)


print("drop a coupon win a prize!")
drop = input("type drop to win prize: ")
if drop == "drop":
    print("dropping coupon")
    time.sleep(3)
    print("decoding prize,")
    time.sleep(2)
    print("Woo hoo! You got " + str(offers_choose) + str("%") +" in " + str(companies_choose) + " come again and win new prizes!")



    
