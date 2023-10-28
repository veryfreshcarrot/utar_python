from random import uniform

while True:
    try:
        prices = input("Price >> ").split()

        for price in prices:
            if price == "-":
                print(price)
            else:
                markup_rate = uniform(1.05, 1.15)
                price = int(float(price) * markup_rate)

                print(str(f"{price:,}") + ".00")

        print("\n---\n")
    except Exception as e:
        print(e)
