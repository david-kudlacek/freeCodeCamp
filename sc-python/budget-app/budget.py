class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.funds = float()

    def __str__(self):
        line_length = 30
        asterisk_length = int((line_length - len(self.name)) / 2)
        output = ""
        total = float()

        output = output + f"{'*' * asterisk_length}{self.name}{'*' * asterisk_length}\n"

        for i in self.ledger:
            description = i["description"]
            amount = f"{i['amount']:.2f}"
            if description == "":
                output = output + f"{amount.rjust(30)}\n"
            else:
                output = output + f"{description[:23]} {amount.rjust(29 - len(description))}\n"
            total = total + float(amount)

        output = output + f"Total: {total}"

        return output

    def deposit(self, amount, description=""):
        details = {"amount": amount, "description": description}
        self.ledger.append(details)  # Add entry to ledger

        self.funds = self.funds + amount  # Add funds

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            details = {"amount": -amount, "description": description}
            self.ledger.append(details)  # Add entry to ledger

            self.funds = self.funds - amount  # Reduce funds
            return True
        return False

    def transfer(self, amount, category):  # Transfer given amount to destination category
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")  # Add entry to ledger
            category.deposit(amount, f"Transfer from {self.name}")  # Add entry to other ledger
            return True
        return False

    def get_balance(self):
        return self.funds

    def check_funds(self, amount):  # Check if enough funds available to withdraw
        if amount > self.funds:
            return False
        return True


def create_spend_chart(categories):
    withdrawal_sums = dict()
    total_sum = float()
    percentages = list()
    names = list()
    output = "Percentage spent by category\n"

    # Calculate percentage spent in each category
    for category in categories:
        for i in category.ledger:
            if i["amount"] > 0:
                continue
            amount = i['amount']
            withdrawal_sums.setdefault(category.name, 0)
            withdrawal_sums[category.name] -= amount
            total_sum = total_sum + amount

    for category in categories:
        percentages.append(abs(withdrawal_sums[category.name] / total_sum * 100))
        names.append(category.name)

    for n in range(10, -1, -1):
        percentage = str(n * 10).rjust(3)
        percentage_bars = ["", "", ""]
        for i, p in enumerate(percentages):
            if p >= int(percentage):
                percentage_bars[i] = "o  "
            else:
                percentage_bars[i] = "   "
        output += f"{percentage}| {percentage_bars[0]}{percentage_bars[1]}{percentage_bars[2]}\n"
    output += "    " + "----------\n"

    for i in range(0, max(len(n) for n in names) + 1):
        if i != max(len(n) for n in names):
            output += "     "
            for name in names:
                if len(name) > i:
                    output += f"{name[i]}  "
                else:
                    output += "   "
            if i != max(len(n) for n in names) - 1:
                output += "\n"

    return output
