# Load temperatures from file into a list of floats
def load_to_list(filepath: str) -> list[float]:
    temps = []
    with open(filepath, "r") as file:
        for line in file:
            # Convert each line to a float and add it to the list
            temps.append(float(line.strip()))
    return temps


# Print basic stats: total count, average, min, and max
def descriptive_statistics(source_data: list[float]) -> None:
    count = len(source_data)
    average = round(sum(source_data) / count, 2)
    smallest = min(source_data)
    largest = max(source_data)

    print(f"There are {count} values in the data source.")
    print(f"The average value is {average}")
    print(f"The highest value is {largest} and the smallest value is {smallest}.")


# Read file and format text based on markup rules
def apply_markup(filepath: str) -> None:
    with open(filepath, "r") as file:
        for line in file:
            words = line.strip().split()
            result = ""

            for word in words:
                # Make word uppercase if it starts with dot
                if word.startswith("."):
                    result += word[1:].upper() + " "
                # Expand word with spaces if it starts with underscore
                elif word.startswith("_"):
                    result += " ".join(list(word[1:])) + " "
                else:
                    result += word + " "
                    
            print(result.strip())
            
if __name__ == "__main__":
    # Test temperature functions
    temps = load_to_list("data/temperatures.txt")
    descriptive_statistics(temps)

    # Test markup function
    apply_markup("data/markup.txt")

"""
Reflection
I reviewed the posted solutions from Week 05 and compared them with my code. There were a few things I noticed that helped me understand how I can keep improving.

Comments  
I did include comments in my original code. They were short and explained my logic without overdoing it. The posted code had more comments, but I think mine still showed that I understood what each part was doing.

Output and Testing  
I tested my code and saw that two of my functions did not pass all the the tests. 

Logic  
I didn’t use anything too advanced. My code was beginner-level and stayed simple.

Overall I didn’t have too many issues, but I see small areas I can clean up. I am still working on writing better and cleaner while testing everything properly. 

"""

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

