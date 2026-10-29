
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []
        self.tax_rate = 5

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        subtotal = sum(product.get_total() for product in self.products)
        tax = subtotal * self.tax_rate / 100
        grand_total = subtotal + tax
        return subtotal, tax, grand_total

    def display_bill(self):
        print("\n" + "=" * 62)
        print("                 CUSTOMER BILL")
        print("=" * 62)
        print(f"{'Product':<18}{'Price':>12}{'Quantity':>12}{'Total':>15}")
        print("-" * 62)

        for product in self.products:
            print(
                f"{product.name:<18}"
                f"{product.price:>12.2f}"
                f"{product.quantity:>12}"
                f"{product.get_total():>15.2f}"
            )

        print("-" * 62)
        subtotal, tax, grand_total = self.calculate_total()
        print(f"{'Subtotal:':>42} Rs. {subtotal:.2f}")
        print(f"{'Tax (5%):':>42} Rs. {tax:.2f}")
        print(f"{'Grand Total:':>42} Rs. {grand_total:.2f}")
        print("=" * 62)


bill = Bill()

print("--- BILLING SYSTEM ---")
print("Enter product details. Type 'done' to finish.")

while True:
    name = input("\nEnter product name: ").strip()

    if name.lower() == "done":
        break

    if not name:
        print("Product name cannot be empty.")
        continue

    try:
        price = float(input("Enter product price: Rs. "))
        quantity = int(input("Enter quantity: "))

        if price <= 0 or quantity <= 0:
            print("Price and quantity must be positive.")
            continue

        product = Product(name, price, quantity)
        bill.add_product(product)
        print("Product added successfully!")

    except ValueError:
        print("Please enter a valid price and quantity.")

if bill.products:
    bill.display_bill()
else:
    print("No products added. Bill not generated.")
