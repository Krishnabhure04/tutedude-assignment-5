# Task 2: Demonstrate List Slicing

def slice_and_reverse():
    # Create a list from 1 to 10
    numbers = list(range(1, 11))

    # Extract the first five elements
    first_five = numbers[:5]

    # Reverse the extracted list
    reversed_five = first_five[::-1]

    # Display both lists
    print("First five elements:", first_five)
    print("Reversed list:", reversed_five)

if __name__ == "__main__":
    slice_and_reverse()
