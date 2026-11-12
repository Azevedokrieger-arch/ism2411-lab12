import csv

# Exercise 2: Read and print raw rows
with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# Exercise 3: Skip the header
print("--- Exercise 3 ---")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

# Exercise 4: Compute totals
print("--- Exercise 4 ---")

total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")


# Exercise 5: Filter and write
print("--- Exercise 5 ---")

total_rows = 0
filtered_rows = 0

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            total_rows += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([
                    product,
                    f"{price:.2f}",
                    quantity,
                    f"{total:.2f}"
                ])
                filtered_rows += 1

print(f"Original rows: {total_rows}")
print(f"Rows written to cleaned.csv: {filtered_rows}")


# Exercise 6: csv.DictReader
print("--- Exercise 6 ---")

# csv.reader is useful for simple files when column positions are known.
# csv.DictReader is better when using column names for clarity.

dict_total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total Revenue (DictReader): ${dict_total_revenue:.2f}")

# Exercise 7: Sales summary by product
print("--- Exercise 7 ---")

product_summary = {}

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity

        if product in product_summary:
            product_summary[product] += revenue
        else:
            product_summary[product] = revenue

for product in sorted(product_summary):
    print(f"{product}: ${product_summary[product]:.2f}")

# Exercise 8: Append mode log
print("--- Exercise 8 ---")

from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log_file:
    log_file.write(
        f"{current_time} - Total Revenue: ${total_revenue:.2f}\n"
    )

print("Run log updated successfully!")

# ISM2411 Lab 12 - Reflections
#
# Reflection 1:
# Python makes it easier to automate tasks like reading, cleaning,
# and calculating data from CSV files. Excel is better for quickly
# viewing data and creating charts without writing code.

# Reflection 2:
# A business could use an append-mode log to track daily sales.
# Append mode is useful because it adds new information without
# deleting previous records, keeping a history of sales activity.


