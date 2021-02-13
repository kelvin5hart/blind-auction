from replit import clear
import art

print(art.logo)
entries = {}
continueBid = "yes"

while continueBid == "yes":
  name = input("What is you name? \n")
  bid = int(input("What's your bid? \n$"))
  optionNext = input("Are there other bidders? Type 'yes' or 'no' \n").lower()
  entries[name] = bid
  clear()
  print(entries)
  if optionNext == "no":
    continueBid = "no"

score = 0
for person in entries:
  if entries[person] > score:
    score = entries[person]
    nameOfPerson = person

print(f"Highest bidder is {nameOfPerson} with a bid of ${score}")
