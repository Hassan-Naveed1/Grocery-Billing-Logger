import logging
import sys

#Creating a logger
logger = logging.getLogger(__name__)

#Setting a starting lvl
logger.setLevel(logging.INFO)

#Creating a Handler
logger_handler = logging.StreamHandler(sys.stdout)

#Creating a formatter
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

#Assigning the formatter to the handler
logger_handler.setFormatter(formatter)

#Assigning the handler to the logger
logger.addHandler(logger_handler)

print("The items are: ")
items = {
    "Rice": 2.50,     # Price per kg
    "Sugar": 1.80,    # Price per kg
    "Milk": 1.20,     # Price per litre
    "Bread": 1.50    # Price per loaf
}

for item_name, item_price in items.items():
    logger.info(f"{item_name} : {item_price}")

try:
    choice = input("Please choose one of the above to buy: ")
    if choice not in items:
        raise ValueError(f"The item {choice} exist ")
    
    if choice in items.keys():
        logger.info(f"User has choosen {choice}")
        quantity_choice = input("Please enter the quantity of your choice: ")

        if not quantity_choice.isdigit():
            raise ValueError("Quantity must be a valid Integer")
        
        quantity = int(quantity_choice)

        if quantity <= 0:
            raise ValueError(f"The quantity should be a positive number")

        logger.info(f"The user has selected {quantity} {choice}")


        
        final_price = quantity * items[choice]
        logger.info(f"The final price will be: {final_price}")

except ValueError as e:
    logger.error(f"Invalid Input: {e}")

