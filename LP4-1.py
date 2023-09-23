def main(): # run with 'python LP4-1.py in shell'
  copies = int(input("Enter number of copies: "))
  if copies<100:
    price = .30
    cost = copies*price
  elif copies>=100 and copies<500:
    price = .28
    cost = copies*price
  elif copies>=500 and copies<750:
    price = .27
    cost = copies*price
  elif copies>=500 and copies<750:
        price = .27
        cost = copies*price
  elif copies>=750 and copies<1000:
          price = .26
          cost = copies*price
  elif copies>1000:
            price = .25
            cost = copies*price
  print(f"Price per copy is: ${copies}")
  print(f"Total cost is: ${cost}")
  pass


if __name__ == "__main__":
  main()
  