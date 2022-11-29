# Script to calculate some basic investing/trading formulas.

# 1
def calculating_percentage_gain_or_loss():
    """Calculating the percentage gain/loss on an investment. """
    while True:
        try:
            price_sold = float(input('\nEnter the price at which you sold your investment: '))
            price_purchased = float(input('Enter the purchase price of your investment: '))
        except ValueError:
            print('One of the values you entered was not valid. Please try again.')
            continue
        else:
            if price_sold > price_purchased:
                print('You sold your investment at a {:.2f}% gain.'.format((((price_sold - price_purchased) / price_purchased) * 100)))
            else:
                print('You sold your investment at a {:.2f}% loss.'.format((((price_sold - price_purchased) / price_purchased) * 100)))
            break

# 3
def calculating_market_cap():
    """Calculating the market cap of a cryptocurrency."""
    while True:
        try:
            circulating_supply = float(input("\nEnter the circulating supply of the cryptocurrency: "))
            price = float(input("Enter the price of the cryptocurrency: "))
        except ValueError:
            print("One of the values you entered was not valid. Please try again.")
            continue
        else:
            print("The market cap of this cryptocurrency is ${:,.2f}.".format(circulating_supply * price))
            break

# 3
def calculating_risk_per_trade():
    """Calculating the amount of risk needed per trade."""
    while True:
        try:
            allowed_risk = ['0.5%', '1%', '2%', '3%']
            total_equity = float(input("\nEnter your total equity: "))
        except ValueError:
            print("The value you entered was not accepted. Please try again.")
            continue
        else:
            for number, percentage in enumerate(allowed_risk, start=1):
                print(f"({number}) {percentage}")
            while True:
                enter_risk = int(input("\nPlease enter your risk amount (options 1 - 4): "))
                print()
                if enter_risk not in range(1, 4 + 1):
                    print("The option you selected is not valid. Please try again.")
                    continue
                elif enter_risk == 1:
                    print('-' * 50)
                    print("Your risk for this trade is ${:,.2f}".format(total_equity * (float(allowed_risk[0].strip('%')) / 100)))
                    print('-' * 50)
                    break
                elif enter_risk == 2:
                    print('-' * 50)
                    print("Your risk for this trade is ${:,.2f}".format(total_equity * (float(allowed_risk[1].strip('%')) / 100)))
                    print('-' * 50)
                    break
                elif enter_risk == 3:
                    print('-' * 50)
                    print("Your risk for this trade is ${:,.2f}".format(total_equity * (float(allowed_risk[2].strip('%')) / 100)))
                    print('-' * 50)
                    break
                elif enter_risk == 4:
                    print('-' * 50)
                    print("Your risk for this trade is ${:,.2f}".format(total_equity * (float(allowed_risk[3].strip('%')) / 100)))
                    print('-' * 50)
                    break
        break

# 4
def calculating_position_size():
    """Calculating position size per trade."""
    while True:
        try:
            disclaimer = "Your plan states that your risk amount should always be between 0.5% - 3%."
            border = f"{len(disclaimer) * '-'}"
            print(f"\n{border}")
            print(f"{disclaimer}")
            print(f"{border}")
            risk_percentage = float(input("\nEnter the percentage you would like to risk on this trade: "))
            print(f"You will be risking {risk_percentage}% on this trade.")
            equity = float(input("Enter your current equity: "))
            # Dividing the risk percentage by 100 gives you a decimal.
            risk = equity * (risk_percentage / 100)
            print(f"Your risk for this trade is ${risk:.2f}.")
            entry_price = float(input("\nEnter your entry price: "))
            stop_loss_price = float(input("Enter your stop-loss price: "))
            distance_to_stop_loss = ((entry_price - stop_loss_price) / entry_price)
            position_size = risk / distance_to_stop_loss
        except ValueError:
            print("One of the values you entered was not valid. Please try again.")
            continue
        else:
            print(f"Your position size is ${position_size}.")
            # Double checking the math. Position size * distance to stop-loss (decimal)
            # should equal risk amount.
            if position_size * distance_to_stop_loss == risk:
                print(f"Position size is correct. Position Size * Distance to stop-loss: ${position_size * distance_to_stop_loss} == Risk: ${risk}.")
            else:
                print("Double check the math.")
        break

# 5
def calculating_distance_to_target():
    """Calculating the distance to profit objective (as a percentage)."""
    while True:
        try:
            target_price = float(input("Please enter your target price: "))
            entry_price = float(input("Please enter your entry price: "))
            print()
        except ValueError:
            print("One of the values you entered was not valid. Please try again.")
        else:
            distance_to_target = ((target_price - entry_price) / entry_price)
            print("-" * 50)
            print("The distance to your target is {:.2%}".format(abs(distance_to_target)))
            print("-" * 50)
            break


# 6
def calculating_distance_to_stop_loss():
    """Calculating the distance to stop-loss (as a percentage and decimal)."""
    while True:
        try:
            entry_price = float(input("Please enter your entry price: "))
            stop_loss_price = float(input("Please enter your stop-loss price: "))
            print()
        except ValueError:
            print("One of the values you entered was not valid. Please try again.")
        else:
            # Calculating distance to stop-loss as a decimal and percentage.
            distance_to_stop_loss = ((entry_price - stop_loss_price) / entry_price)
            print("-" * 50)
            print("The distance to your stop-loss is {:.2f} or {:.2%}".format(abs(distance_to_stop_loss), abs(distance_to_stop_loss)))
            print("-" * 50)
            break

# 7
def calculating_risk_reward_ratio():
    """Calculating risk/reward ratio."""
    while True:
        try:
            target_price = float(input("\nEnter your target price: "))
            entry_price = float(input("Enter your entry price: "))
            stop_loss_price = float(input("Enter your stop-loss price: "))
        except ValueError:
            print("One of the values you entered was not valid. Please try again.")
            continue
        else:
            print(f"Your R ratio is {round((target_price - entry_price) / (entry_price - stop_loss_price), 2)}R.")
        break

# 8
def calculating_winrate():
    """Calculating winrate after a certain amount of trades (as a percentage)."""
    while True:
        try:
            winning_trades = int(input("\nEnter your amount of winning trades :"))
            total_trades = int(input("Enter the amount of trades you have taken: "))
        except ValueError:
            print('One of the values you entered was not valid. Please try again.')
            continue
        else:
            print('You have a {:.2f}% winrate.'.format((((winning_trades / total_trades) * 100))))
        break


# 9
def calculating_winrate_profitability():
    """Calculating the winrate needed to be profitable using a trader's R average."""
    while True:
        try:
            R = float(input("\nEnter your R: "))
        except ValueError:
            print('One of the values you entered was not valid. Please try again.')
            continue
        else:
            print('You will need a minimum winrate of {:.2f}% to be profitable.'.format(1 / (1 + R) * 100))
        break

# 10
def calculating_altusd_price():
    """Calculating the USD price of an altcoin."""
    while True:
        try:
            btc_usd_price = float(input("\nEnter the current price of Bitcoin: "))
            alt_btc_price = float(input("Enter the price of the altcoin in sats: "))
            print()
        except ValueError:
            print("One of the values you entered was not valid. Please try again.")
        else:
            alt_usd_price = btc_usd_price * alt_btc_price
            print("The price of this altcoin is ${:,.2f}".format(alt_usd_price))
        break

# 11
def calculating_apy():
    """Calculating apy."""
    accepted_answers = ['daily', 'monthly', 'quarterly', 'semi-annually', 'yearly']
    while True:
        try:
        # r is the period rate
            r = float(input('\nEnter the period rate: '))
        except ValueError:
            print("The value you entered was not valid. Please try again.")
        else:
        # n is the number of compounding periods per year (monthly, quarterly, semi-annually, etc)
            print("Below are the different compounding periods to choose from.")
            # Adding nuumbers to each selection in the accepted_answers list.
            for index, value in enumerate(accepted_answers, start=1):
                print(f"[{index}] {value.title()}")
            selection = int(input("Please select one (Hint: Enter 1, 2, 3, 4, or 5): "))
            if selection not in range(1, len(accepted_answers) + 1):
                print('Your selection was invalid. Please try again.')
            # Daily APY
            elif selection == 1:
                print(f"The annual percentage yield is {round(((1 + ((r / 100) / 365)) ** 365 - 1) * 100, 2)}%")
            # Monthly APY
            elif selection == 2:
                print(f"The annual percentage yield is {round(((1 + ((r / 100) / 12)) ** 12 - 1) * 100, 2)}%")
            # Quarterly APY
            elif selection == 3:
                print(f"The annual percentage yield is {round(((1 + ((r / 100) / 4)) ** 4 - 1) * 100, 2)}%")
            # Semi-Annual APY
            elif selection == 4:
                print(f"The annual percentage yield is {round(((1 + ((r / 100) / 6)) ** 6 - 1) * 100, 2)}%")
            # Yearly APY
            elif selection == 5:
                print(f"The annual percentage yield is {round(((1 + ((r / 100) / 1)) ** 1 - 1) * 100, 2)}%")
            break

# 12
def calculating_drawdown_recovery():
    "Calculating drawdown recovery."
    while True:
        try:
            enter_drawdown = input("Enter your drawdown % (as a number): ")
            calculation = ((1 / (1 - (int(enter_drawdown) / 100))) - 1) * 100
        except ValueError:
                print("One of the values you entered was not valid. Please try again.")
        else:
            print(f"You have lost {enter_drawdown}% of your capital.")
            print(f"In order for you to break even, you will need a {round(calculation, 1)}% gain.")
        break

if __name__ == '__main__':
    while True:
        try:
            print('(1) Calculate percentage gain/loss. \
                \n(2) Calculate market cap. \
                \n(3) Calculate risk per trade. \
                \n(4) Calculate position size. \
                \n(5) Calculate distance to target as a percentage. \
                \n(6) Calculate distance to stop-loss as a decimal and a percentage. \
                \n(7) Calculate risk/reward ratio. \
                \n(8) Calculate win rate as a percentage. \
                \n(9) Calculate minimum win rate needed to be profitable as a percentage. \
                \n(10) Calculate the price of an altcoin in dollars. \
                \n(11) Calculate APY. \
                \n(12) Calculate drawdown recovery. \n')
            user_input = int(input('Enter: '))
        except ValueError:
            print('The value you entered was not valid, please try again.\n')
            continue
        else:
            if user_input == 1:
                calculating_percentage_gain_or_loss()
            elif user_input == 2:
                calculating_market_cap()
            elif user_input == 3:
                calculating_risk_per_trade()
            elif user_input == 4:
                calculating_position_size()
            elif user_input == 5:
                calculating_distance_to_target()
            elif user_input == 6:
                calculating_distance_to_stop_loss()
            elif user_input == 7:
                calculating_risk_reward_ratio()
            elif user_input == 8:
                calculating_winrate()
            elif user_input == 9:
                calculating_winrate_profitability()
            elif user_input == 10:
                calculating_altusd_price()
            elif user_input == 11:
                calculating_apy()
            elif user_input == 12:
                calculating_drawdown_recovery()
            break


input()