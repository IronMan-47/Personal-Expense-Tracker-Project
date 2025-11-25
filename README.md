Personal Expense Tracker System 💰

1. Project
Personal Expense Tracker

2. Overview of the Project
The Personal Expense Tracker is a console program.
I use the Personal Expense Tracker as a student. I use the Personal Expense Tracker as a professional to manage money tasks.
I use the Personal Expense Tracker every day. The Personal Expense Tracker lets me see my spending.
I often have trouble, with the expenses, like food, travel or stationery. The mobile apps I tried are too complex or intrusive. That is why I made the project. The project gives the tool that runs on the desktop. The tool lets me log the expenses quickly. The tool saves the data automatically to a CSV file. The tool runs on the desktop. Writes the data without steps. The tool shows me the spending habits by breaking the spending habits down by the category. I can see the spending habits by the category whenever I need.

3. Features
📝 Quick Expense Logging: Add details like Product Name, Category, Price, and Date in seconds.
I notice that Auto‑Save saves the data to expenses.csv after each entry. Auto‑Save does not need a save.
🔍 Search & View: The Search & View tool helps me see a history of transactions. The Search & View tool also helps me find items, by the ID.
✏️. Delete: mistakes such, as typos, in the price. Remove the entries easily.
📊 Analytics: I can see a summary of the Total Spent. I can see a breakdown of the spending, by Category. For example I can see how much I spent on FOOD and how much I spent on TRAVEL.
🛡️ Crash Handling: I added error handling. The error handling stops the program from crashing when you type text of numbers.

4. Technologies & Tools Used
Language: Python 3.10
Modules:
    csv (Standard library for file handling)
    Modules2 (Custom backend module included in the repo)
    Development Environment: Developed using PyCharm/VS Code, but runs in any standard terminal/command prompt.

5. Steps to run the project
Prerequisites
When I set up the machine I always check that Python 3.x is installed on my computer. You also need to make sure that Python 3.10 is installed on your system. Do not skip this step.
Check by running python --version or python3 --version in your terminal.

Verify Files:
I make sure the main.py file is, in the folder. I also make sure the Modules2.py file is, in the folder. The main.py file and the Modules2.py file must stay together in one folder.
Running the Application
Run the following command in your terminal:
python main.py
(When I run the script, on some systems I have to use python3 main.py. I type python3 main.py to start the script.)

7. Instructions for Testing
First I make sure the application is running. Then I follow these steps to test the core functionality of the application:
First Run:
When the menu appears I click Option 1 (Add New Expense option)
Enter a sample expense (e.g., Name: Coffee, Category: Food, Price: 50, Date: 12-12-2024).
I open the project folder. I look for a file called expenses.csv. I expect the file expenses.csv to already be there automatically.

View Data:
Select Option 2 (View all Expenses).
I am checking. I need the Coffee entry displayed.

Vailding Other Options:
Then We can check the other option similarly by giving the required input asked by the program and the Getting the output from the program

Analysis:
Continuing with the Eg I was giving 
Add a second expense with the same category (e.g., Sandwich, Food, 100).
Select Option 7 (Show Category total).
Check the total for FOOD. The total, for FOOD should be 150.
