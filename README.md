# fetchTest

Backend Engineering Intern Programming Test for Fetch Rewards

This code defines a function spendPoints that takes a list of command line arguments and reads transactions from a CSV file to calculate the total points earned by each payer and then spend those points according to the oldest transactions. The function returns a dictionary with the updated total points for each payer after the points are spent.

## Dependencies

This code imports the following modules:

1. csv for reading and writing CSV files
2. sys for accessing command line arguments
3. datetime for manipulating dates and times
4. typing for type hints

## Usage

To use this code, you need to have Python 3 installed on your system. You can run the script by typing 'python3 pointSpender.py points filename.csv' in the terminal. The 'points' field should be an integer value for the total points to be spent, and 'filename.csv' should be the name of the CSV file containing the transaction data in the same directory as the python file.

The spendPoints function takes a list of command line arguments as input and returns a dictionary with the updated total points for each payer after the points are spent. If any input values are invalid, the function will print an error message and return None.

## Functionality

The spendPoints function reads the transaction data from the CSV file and sorts it by the transaction date in ascending order. It then calculates the total points earned by each payer and spends the points in the oldest transactions first. The function updates the total points for each payer after the points are spent and returns a dictionary with the updated points.

If there are not enough points to spend, the function will spend as many points as possible and return the updated total points. If the CSV file or the points value is invalid, the function will print an error message and return None.

## Example Usage

Suppose you have a CSV file named transactions.csv with the following transaction data:

payer,points,timestamp
DANNON,1000,2021-02-02T14:00:00Z
UNILEVER,200,2021-01-01T15:00:00Z
DANNON,-200,2021-02-02T14:05:00Z
MILLER COORS,10000,2021-03-02T14:00:00Z
DANNON,300,2021-02-03T14:00:00Z

You can run the script to spend 500 points as follows:

python3 pointSpender.py 500 transactions.csv
The script will output the updated total points for each payer after the points are spent. In this case, the output will be:
{'MILLER COORS': 10000, 'DANNON': 800, 'UNILEVER': 0}

This indicates that DANNON has 800 points remaining, UNILEVER has 0 points remaining, and MILLER COORS has 10000 points remaining after spending 500 points.
