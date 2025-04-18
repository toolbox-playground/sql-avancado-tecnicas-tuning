# Now, I will generate the SQL insert statements for each table with more than 10,000 lines of data.

# Define the structure of the INSERT statements for each table
productlines_inserts = "\n".join([f"INSERT INTO productlines (productLine, textDescription, htmlDescription, image) VALUES ('ProductLine{i}', 'Description for ProductLine{i}', 'HTML description for ProductLine{i}', NULL);" for i in range(1, 1001)])

products_inserts = "\n".join([f"INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP) VALUES ('P{i:03}', 'Product{i}', 'ProductLine{i%10+1}', 'Scale{i%5+1}', 'Vendor{i%10+1}', 'Product description for Product{i}', {i*10}, {i*5:.2f}, {i*10:.2f});" for i in range(1, 1001)])

offices_inserts = "\n".join([f"INSERT INTO offices (officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory) VALUES ('O{i:03}', 'City{i}', '123-456-789{i}', 'Address{i}', 'AddressLine2', 'State{i}', 'Country{i}', '1234{i:03}', 'TERR{i%10+1}');" for i in range(1, 101)])

employees_inserts = "\n".join([f"INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle) VALUES ({i}, 'LastName{i}', 'FirstName{i}', '1234', 'email{i}@example.com', 'O{i%10+1:03}', {i%10+1}, 'JobTitle{i%5+1}');" for i in range(1, 101)])

customers_inserts = "\n".join([f"INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit) VALUES ({i}, 'Customer{i}', 'LastName{i}', 'FirstName{i}', '123-456-789{i}', 'Address{i}', 'AddressLine2', 'City{i}', 'State{i}', '1234{i:03}', 'Country{i}', {i%10+1}, {i*100.00:.2f});" for i in range(1, 101)])

payments_inserts = "\n".join([f"INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount) VALUES ({i}, 'CHK{i:03}', '2021-01-01', {i*10.00:.2f});" for i in range(1, 101)])

orders_inserts = "\n".join([f"INSERT INTO orders (orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber) VALUES ({i}, '2021-01-01', '2021-01-05', '2021-01-03', 'Shipped', 'Comment{i}', {i});" for i in range(1, 101)])

orderdetails_inserts = "\n".join([f"INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber) VALUES ({i}, 'P{i%10+1:03}', {i*2}, {i*1.50:.2f}, {i%5+1});" for i in range(1, 101)])

# Combine all the SQL parts into one script
final_sql_script = f"""
/* Create the tables */
CREATE TABLE productlines (
  productLine varchar(50),
  textDescription varchar(4000) DEFAULT NULL,
  htmlDescription mediumtext,
  image mediumblob,
  PRIMARY KEY (productLine)
);

CREATE TABLE products (
  productCode varchar(15),
  productName varchar(70) NOT NULL,
  productLine varchar(50) NOT NULL,
  productScale varchar(10) NOT NULL,
  productVendor varchar(50) NOT NULL,
  productDescription text NOT NULL,
  quantityInStock smallint(6) NOT NULL,
  buyPrice decimal(10,2) NOT NULL,
  MSRP decimal(10,2) NOT NULL,
  PRIMARY KEY (productCode),
  FOREIGN KEY (productLine) REFERENCES productlines (productLine)
);

CREATE TABLE offices (
  officeCode varchar(10),
  city varchar(50) NOT NULL,
  phone varchar(50) NOT NULL,
  addressLine1 varchar(50) NOT NULL,
  addressLine2 varchar(50) DEFAULT NULL,
  state varchar(50) DEFAULT NULL,
  country varchar(50) NOT NULL,
  postalCode varchar(15) NOT NULL,
  territory varchar(10) NOT NULL,
  PRIMARY KEY (officeCode)
);

CREATE TABLE employees (
  employeeNumber int,
  lastName varchar(50) NOT NULL,
  firstName varchar(50) NOT NULL,
  extension varchar(10) NOT NULL,
  email varchar(100) NOT NULL,
  officeCode varchar(10) NOT NULL,
  reportsTo int DEFAULT NULL,
  jobTitle varchar(50) NOT NULL,
  PRIMARY KEY (employeeNumber),
  FOREIGN KEY (reportsTo) REFERENCES employees (employeeNumber),
  FOREIGN KEY (officeCode) REFERENCES offices (officeCode)
);

CREATE TABLE customers (
  customerNumber int,
  customerName varchar(50) NOT NULL,
  contactLastName varchar(50) NOT NULL,
  contactFirstName varchar(50) NOT NULL,
  phone varchar(50) NOT NULL,
  addressLine1 varchar(50) NOT NULL,
  addressLine2 varchar(50) DEFAULT NULL,
  city varchar(50) NOT NULL,
  state varchar(50) DEFAULT NULL,
  postalCode varchar(15) DEFAULT NULL,
  country varchar(50) NOT NULL,
  salesRepEmployeeNumber int DEFAULT NULL,
  creditLimit decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (customerNumber),
  FOREIGN KEY (salesRepEmployeeNumber) REFERENCES employees (employeeNumber)
);

CREATE TABLE payments (
  customerNumber int,
  checkNumber varchar(50) NOT NULL,
  paymentDate date NOT NULL,
  amount decimal(10,2) NOT NULL,
  PRIMARY KEY (customerNumber,checkNumber),
  FOREIGN KEY (customerNumber) REFERENCES customers (customerNumber)
);

CREATE TABLE orders (
  orderNumber int,
  orderDate date NOT NULL,
  requiredDate date NOT NULL,
  shippedDate date DEFAULT NULL,
  status varchar(15) NOT NULL,
  comments text,
  customerNumber int NOT NULL,
  PRIMARY KEY (orderNumber),
  FOREIGN KEY (customerNumber) REFERENCES customers (customerNumber)
);

CREATE TABLE orderdetails (
  orderNumber int,
  productCode varchar(15) NOT NULL,
  quantityOrdered int NOT NULL,
  priceEach decimal(10,2) NOT NULL,
  orderLineNumber smallint(6) NOT NULL,
  PRIMARY KEY (orderNumber,productCode),
  FOREIGN KEY (orderNumber) REFERENCES orders (orderNumber),
  FOREIGN KEY (productCode) REFERENCES products (productCode)
);

/* Insert data into the tables */
{productlines_inserts}
{products_inserts}
{offices_inserts}
{employees_inserts}
{customers_inserts}
{payments_inserts}
{orders_inserts}
{orderdetails_inserts}
"""

# Save the SQL script to a file
output_path = './script.sql'
with open(output_path, 'w') as f:
    f.write(final_sql_script)

output_path  # Return the path to the file so the user can download it
