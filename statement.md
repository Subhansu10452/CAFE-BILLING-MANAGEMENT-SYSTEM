=========================================================================================================================================
                                              **CAFE BILLING MANAGEMENT SYSTEM**
=========================================================================================================================================

# PROBLEM STATEMENT
⚪Small cafes need a simpler to take orders from customers, create bills, finding the bill, and track the available stock.
⚪Handling these above tasks manually can lead to incorrect totals, deliver the wrong items which is not ordered and may be wrong in tracking the available stock.
⚪So, this program which is a simple python program can help these cafes to avoid the avobe mentioned mistakes.

# SCOPE OF THE PROJECT
⚪This project is a single user,simple python program intended to use by cafe staffs on their computers.
⚪ This project can display menu, add new items in the menu, update the stock, create bills, find the old bill if required by using the bill number.
⚪This project save the menu info in the json file and bill records in a text file.But this project doesn't have the program to accpet online payments from customer,graphical interface.

# TARGET USERS
⚪Cafe's owner who need a simple way to maintain menu items and track the stocks.
⚪Cafe's cashier who take orders from customer and prepare the bill.

# HIGH-LEVEL FEATURES
- **View menu** -> Display the menu, item numbers,price,name and quantities.
- **Add item** -> Enter the new item with its price, name and starting stock.
- **Update stock** -> Set the new quantities for an existing item.
- **Create bill** -> select the menu items and its quantities and the selected item and quantites must be in menu and available stock.
- **Calculate grand total** -> First calculate order line, subtotal, taxes and then grand total.
- **Save bills** -> Save each bills including bill number, date, time, items and totals.
- **Search bills** -> Find the saved bill number by using its bill number.