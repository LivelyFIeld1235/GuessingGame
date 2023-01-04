import random;

def generateNUM():
    generateNUM = random.randint(0,100);
    return generateNUM;

def guessNum():
    isValid = False;
    while(isValid == False):
        try:
            guess = int(input("Enter a Guess of a number between 0-100"));
            isValid = True;
        except ValueError:
            print("please enter a valid num")
    return guess

def storeandCheck(cache, guess,NUM):

    if(len(cache) == 0):
        cache.append(abs(NUM-guess));
        return "try again";
    else:
        if(len(cache) == 1):
            cache.append(abs(NUM-guess))
            if(cache[1] < cache[0]):
                return "closer, try again";
            else:
                return "further, try again";
        else:
            cache[0] = cache[1];
            cache[1] = (abs(NUM-guess))
            if(cache[1] < cache[0]):
                return "closer, try again";
            else:
                return "further, try again";

if __name__ == "__main__":
    cache = [];
    NUM = generateNUM();
    tries = 10;
    print(f"you have {tries} tries")
    guess = guessNum();
    while(guess != NUM and tries != 0):
        string = storeandCheck(cache, guess, NUM)
        print(string);
        guess = guessNum();
        tries -= 1;
        print(f"you have {tries} tries")
    if(tries == 0):
        print("you lose")
    else:
        print("you win")