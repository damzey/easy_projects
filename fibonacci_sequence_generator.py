from num2words import num2words

class fib_sequence:

    ''' This class is used to represent the Fibonacci sequence '''

    def __init__(self):

        '''See help(fib_sequence) for accurate signature'''

        self.fib_start_sequence = [0,1]

    def ask_the_amount_of_terms(self):

        '''This method ask the user for how many terms do they wsnt in the seqeunce '''

        self.desired_number = int(input('How many numbers do you want in your sequence: '))
        while self.desired_number <= 0:
            print('Please enter a positive integer')
        if self.desired_number == 1:
            print(self.fib_start_sequence[0])
            exit 
        elif self.desired_number == 2:
            print([self.fib_start_sequence[0], self.fib_start_sequence[1]])
            exit
        else:
            return self.desired_number
    
    def calculate_fibonacci_length(self):

        '''This method creates the sequence with the desired number of terms '''

        for i in range(2, self.desired_number):
            next_number = self.fib_start_sequence[-1] + self.fib_start_sequence[-2]
            self.fib_start_sequence.append(next_number)
        return self.fib_start_sequence, self.desired_number
    
    def check_if_number_is_in_the_Fibonacci_sequence(self):

        ''' This method checks to see if the number is in the created sequence  '''

        number = int(input(f"Please enter the number you want to check is in the Fibonacci sequence of {self.desired_number} terms: "))
        print()
        if number not in self.fib_start_sequence:
            print(f"Unlucky! {number} is not in the Fibonacci sequence")
            print(self.fib_start_sequence)
        else:  
            print(f"Congratulations! {number} is in the Fibonacci sequence")
            print()
            for i in range(len(self.fib_start_sequence)):
                if number == self.fib_start_sequence[i]:
                    self.fib_start_sequence[i] = number
                    print(f"{number} is the {num2words(i, to = 'ordinal_num')} number in the Fibonacci sequence")
            print()
            print(self.fib_start_sequence)

def Fibonnaci_generator_and_check():   
    game = fib_sequence()
    game.ask_the_amount_of_terms()
    if game.desired_number < 3:
        exit
    else:
        game.calculate_fibonacci_length()
        game.check_if_number_is_in_the_Fibonacci_sequence()

Fibonnaci_generator_and_check()


            


    
    
    
