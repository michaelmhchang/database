# Description
A simple database application that accesses information through the database.csv. This application can currently update and add data, as well as show what is currently on the database.

# Current function descriptions
#### _Show database_ ####
* Shows database in format:  
('_item_1_', '_upc_code_1_')  
_item_1_date_1_  _item_1_price_1_  
_item_1_date_2_  _item_1_price_2_  
('_item_2_', '_upc_code_2_')  
_item_2_date_1_  _item_2_price_1_  
.  
.  
.  

#### _Add item_ ####
* New item column criteria:
	* Item name does not exist
	* Item name exists but different upc code
* If item exists in database:
	* Creates a new row under current item
		* New row includes current date logged and the new price
	
# Notes
* Compile menu.py to access database
* Originally made this to log Walmart prices
	* That's why database uses upc codes
	* Also the reason for creating a new column for an item with the same name but different upc code (for different editions or colours, etc.)

# Future upates
- Add a remove feature
- Change from a walmart database to a generic one

# Edit notes
Feel free to edit and critique the code as much as you like! I'm always looking for ways to improve and become more efficient. I created this application to learn more and improve anyway that I can!  

