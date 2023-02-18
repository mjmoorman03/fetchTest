import csv
import sys
import datetime 
from typing import List, Dict

def spendPoints(args: List[str]) -> Dict[str, int] | None:
    
    # read transactions from csv file into a list of dictionaries
    try:
        with open(args[2], 'r') as f:
            reader = csv.DictReader(f)
            transactions: List[Dict[str, str]] = list(reader)
    except:
        print("Invalid file")
        return

    try:
        points: int = int(args[1])
    except:
        print("Invalid points")
        return

    # sort transactions by date, so that the oldest transactions are spent first
    transactions.sort(key=lambda x: datetime.datetime.strptime(x['timestamp'], '%Y-%m-%dT%H:%M:%SZ'))

    # sum up total points for each payer
    totalPoints: Dict[str, int] = {payer: sum(int(transaction['points']) for transaction in transactions if transaction['payer'] == payer) \
        for payer in set(transaction['payer'] for transaction in transactions)}

    # spend points
    for transaction in transactions:

        # cannot spend more than the total points for a payer, more than the transaction, or the rest to spend
        availablePoints: int = min(points, int(transaction['points']), totalPoints[transaction['payer']])
        points -= availablePoints
        totalPoints[transaction['payer']] -= availablePoints
        if points == 0:
            break

    print(totalPoints)
    return totalPoints


if __name__ == "__main__":
    spendPoints(sys.argv)