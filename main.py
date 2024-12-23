import os
from plantuml import PlantUML

# Define the PlantUML server if you want to use online rendering.
# If you have plantuml.jar locally, you can pass the path to PlantUML
# E.g., PlantUML(url='/path/to/plantuml.jar')
plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')

# PlantUML diagram source code
uml_code = """
@startuml
entity "Customer" {
  * CustomerID : int
  --
  Name : string
  Email : string
}

entity "Order" {
  * OrderID : int
  --
  OrderDate : date
  Amount : float
}

entity "Product" {
  * ProductID : int
  --
  Name : string
  Price : float
}

entity "Supplier" {
  * SupplierID : int
  --
  Name : string
  ContactInfo : string
}

entity "CreditCard" {
  * CardID : int
  --
  CardNumber : string
  ExpiryDate : date
}

entity "ProductSupplier" {
  * ProductID : int
  * SupplierID : int
}

entity "CustomerCreditCard" {
  * CustomerID : int
  * CardID : int
}

Customer ||--o{ Order
Order ||--o{ Product
Product }o--|| ProductSupplier
Supplier ||--o{ ProductSupplier
Customer }o--|| CustomerCreditCard
CreditCard ||--o{ CustomerCreditCard
@enduml
"""

# Save the PlantUML code to a temporary file
with open("diagram.txt", "w") as file:
    file.write(uml_code)

# Generate the diagram image
plantuml.processes_file("diagram.txt")

# Remove the .txt file if you don't need it anymore
os.remove("diagram.txt")

print("Diagram generated successfully!")