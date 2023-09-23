def main(): # run with 'python LP4-3.py in shell'
  eggs = int(input("Enter number of eggs purchased: "))
  dozen = int(eggs/12)
  extra = eggs%12
  if dozen<4:
    cost = (dozen*.50)+extra*0.0416
  elif dozen>=4 and dozen<6:
    cost = (dozen*.45)+extra*0.0375
  elif dozen>=6 and dozen<11:
    cost = (dozen*.40)+extra*0.0333
  elif dozen>11:
    cost = (dozen*.35)+extra*0.0291
  '${:,.2f}'.format(cost)
  print(f"The bill is equal to: ${cost}")
  print(dozen)
  print(extra)
  pass


if __name__ == "__main__":
  main()
  