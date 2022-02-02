import art
from game_data import data
import random



def check_guess(a_followers, b_followers, guess):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def account_data(account):
  account_name = account['name']
  account_country = account['country']
  account_desc = account['description']
  return f"{account_name}, a {account_desc}, from {account_country}"
 
print(art.logo)
score = 0
should_continue =  True
account_b = random.choice(data)


while should_continue:

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    

    print(f"Compare A: {account_data(account_a)}")
    print(art.vs)
    print(f"Against B: {account_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B'").lower()
    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']
    is_correct = check_guess(a_followers, b_followers, guess)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        should_continue = False
        print(f"Sorry, you're wrong. Final score: {score}")


