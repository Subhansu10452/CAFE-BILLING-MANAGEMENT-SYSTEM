=========================================================================================================================================
                                                **CAFE BILLING MANAGEMENT SYSTEM**
=========================================================================================================================================

**WHAT IS THE PURPOSE OF THIS PROJECT**
->This project helps the cafe staff to take orders from customers and create bills.
->It can also search old bills,add new items in the menu and update stock.
->It also uses government taxes like SGST AND CGST.

## There is no requirement of additional application. This is a simple python program which runs in terminal.

**WHAT IMPORT MODULES I HAVE USED AND HOW DO THEY WORK**
->First one is json which reads and writes the menu data.
->Second one is os which checks whether the menu data file exists.
->Last one is datetime which provide the current data and time for bill numbers and dates.

*WHAT DATA USED BY THIS PROGRAM*
- DATA_MENU is cafe_data.json which stores the menu.
- BILL_FILE is bill_txt which stores the bills.

**WHAT FUNCTIONS I HAVE USED AND WHAT ARE THERE WORK**
<load_menu()>
✅ It reads cafe_data.json if it exists.
✅ Json changes the dictionary keys to text so laod_menu() converts item numbers back to integers. 
✅ If the file doesn't exist, it will use default menu.It takes no user input and returns the main menu.
<save_menu()>
✅ It writes the current menu to cafe_data.json.
✅ It takes no user input and returns no value.
✅ save_menu() call after changing the menu or stock.
<show_menu()>
✅ The work of this function is to call the menu which contains item's number,name,price and their stock quantity.
✅ It takes no input from user and doesn't change the data.
<add_item()>
✅ The work of this function is to ask the user to enter the item's name,price and starting stock..
✅ It adds the items,save in the menu and print the confirmation page.
✅ While using this function user have to keep these three following points in their minds otherwise invalid inputs make an error and make no changes.
       ⚪The name can't be blank.
       ⚪Price and Stock number must be in whole numbers.
       ⚪Price must be greater than zero.
<update_stock()>
✅ The work of this function is to update the starting quantity of existing items.The stock quantity must be in the whole number.
✅ On valid input it saves and update in the menu.                
<create_bill()>
✅ The work of this function is to create bill.It repeatdly show the menu and ask the user to enter the item number and its required quantities.(Item number must be in the menu)
✅ The required quantitiy must be in the whole number above zero and do not exceed the stock quantity.Otherwise error will be print.
✅ Enter G to finish entering items.
           🔴HOW WILL THE BILL CREATE?
              ✓For each item, line total = price*quantity. It add the line totals to get the subtotal. Now the taxes will be calculated:
                            SGST = subtotal * 2.5\100
                            CGST = subtotal * 2.5\100
              ✓Grand total = subtotal + SGST + CGST
✅ It prints the bill containinng bill number,date,time,subtotal,taxes and grand total.
✅ It subtracts the ordered quantites from item's stock number and update the menu.
✅ If G is enetered before entering any item is ordered then no bill will be created.
✅ It appends the bill to bills.txt 
<show_saved_bill()>
✅ It will ask user for bill number , search in bills.txt and print the matching bill.
✅ If the bill number is not found in bills.txt then it will return no bill was found.0

**HOW THE BUILT-IN FUNCTIONS WORK IN THIS PROGRAM?**
✅ Input("  ") display the question and return the user's response as text.
✅ strip() removes the space at the start and the end.
✅ isdigit() to check for digits.
✅ int() to convert text into numbers.
✅ print() to display the messege in the terminal.
✅ json.dump save the menu.
✅ file.write() add bill text to the bill file.

## MAIN PROGRAM FLOW
1. Define tax rates and the deafult menu.
2. Call load_menu() to display the current menu.
3. Display the main options repeatdely and read the user's choice.
4. Choice 1 creates a bill; Choice 2 searches bills; Choice 3 adds an item; Choice 4 show the menu; Choice 5 update the stock and Choice  6 prints the thank you messege and exit the loop.

## ABOUT THE FILES CREATED IN THIS PROGRAM
- cafe_data.json stores item's numbers,prices,names and current stock. If it doesn't exist, deafult menu will display.
- bills.txt stores completed bills and used to search stored bill.

**STEPS TO RECREATE THIS PROGRAM IF ANYONE WANTS**
1. Import json,os and datetime.
2. Define file names,tax rate and the default menu.
3. Write functions to load and save the menu.
4. Write function to display the menu.
5. Write functions to update stock,add an item and checking all inputs.
6. Write bill entry which accepts item numbers and quantitites with updating the stock.
7. calculate line total,subtotal,SGST,CGST and at last grand total.
8. Display and save the bill.
9. Write bill search by reading bills.txt and find the bill number user has entered.
10. Add a loop which call the main menu each time after selecting any choice.


