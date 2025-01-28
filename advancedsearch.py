# 1. Name:
#      Emily McGovern
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      There are multiple files and a user is needing to find a name in a specific file
#      through searching through a specific file. This code will search through search through
#      the file by splitting it in half and deciding if the name is in the lower half or the higher
#      half of the file. Once decided, then it will loop again and again, cutting the file by half
#      until the name is found or not found in the file.
# 4. Algorithmic Efficiency
#      I believe that the algorithmic efficiency is O(log n). The reasoning why I figured the efficiency
#      is O(log n) because there is a loop that is controlled by the input. The code is also subdivided
#      which means it cuts the size of the lists by half. Each time it is cut in half that
#      half will be cut in half again. I then calculated the efficiency with the equation. 
#      I used the equation cost = (c1)(log2)(n)+ c2. I then implemented a counter in my code.
#      I used the calculation n = 11 c = 4 and n = 196 c = 8. My expression then came up 
#      to cost = 4/log2(196.11) * log2(11) + 0.9626310882. Once solved I used n = 11 and c = 4 to see 
#      if my calculations were correct. In the end my calculation come up with 4 = 4.3, rounded is 4 = 4. 
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part of this project was finding the algorithm efficiency and opening the files.
#      The algorithm efficiency was very hard to find and calculate. I went back in the textbook and
#      looked through all the different types of efficiencies. I then came across 0(log n). The description
#      matched very closely to the binary search. I then calculated to see if it matched. With opening files
#      I kept trying to open all file names and found that wasn't the best choice. I then decided that 
#      using the users input and then using that input to open the one individual file.
# 6. How long did it take for you to complete the assignment?
#      Overall it took me an hour and 25 mins. It took me about 45 mins to code and 40 mins to find the 
#      algorithm efficiency.

# Importing json to the code.
import json

# Asking user for what file they want to search through.
filename = input("What file would you like to look through? ")

# Asking user what name they are looking for in the file.
find_name = input("What is the name you are looking for? ")

# Opening the file the user asked for and seeing if the file is true.
try:
    with open(f'C:/Users/lover/OneDrive/Documents/BYUI/CSE 130/w06and08/{filename}', "r") as file:
        text_names = file.read()
        json_data = json.loads(text_names)
        names_list = json_data["array"]
except Exception as no_file:
    print(f"Error loading file: {no_file}")
    

def binary_search(names_list, find_name):
    # Setting the beginning of list as 0 and the last of the list as right.
    left = 0
    right = len(names_list) - 1

    # Using a while loop to go through the file until the name is found or not.
    while left <= right:
        
        # Splitting the list in half.
        middle = (left + right) // 2

        # If the name is in the upper part of the file, then the left will move up the file. 
        if names_list[middle] < find_name:
            left = middle + 1

        # If the name is in the lower part of the file, then the right will move down the file.
        elif names_list[middle] > find_name:
            right = middle - 1

            # If the file is found or not then it will leave the loop.
        else:
            return True
    return False
    

# If the name is found in the file then it will print found, if not print not found.
def main():
    if names_list is None:
        return
    found = binary_search(names_list, find_name)
    if found:
        print(f"I found {find_name} in file {filename}")
    else:
        print(f"I could not find the {find_name} in file {filename}")
if __name__ == "__main__":
    main()

      
