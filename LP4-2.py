def main(): # run with 'python LP4-2.py in shell'
  weight = int(input("Enter package weight in kilos: "))
  length = int(input("Enter package length in centimeters: "))
  width = int(input("Enter package width in centimeters: "))
  height = int(input("Enter package height in centimeters: "))
  area = length*width*height
  if weight>27 and area>100000:
    print("Too heavy and too large.")
  elif weight>27:
    print("Too heavy.")
  elif area>100000:
    print("Too large.")
  pass


if __name__ == "__main__":
  main()
  