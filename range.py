labels = [(15,"ThreeFive"), (5,"Five"),(3,"Three")]

class Integer:
   def __init__(self, n):
       self.number = n

   def __repr__(self):
       for number, label in labels:
           if self.number%number == 0:
               return label

       # Default values for other numbers
       return str(self.number)


if __name__ == '__main__':
   numbers = [Integer(x) for x in range(1,101)]
   print(numbers)
