#!/usr/bin/env python
# coding: utf-8

# In[2]:


from module5_mod import NumberStorage

if __name__ == "__main__":
    try:
        N = int(input("Enter a positive integer N: "))
        if N <= 0:
            print("N must be a positive integer.")
            exit(1)

        number_storage = NumberStorage()

        for i in range(N):
            num = int(input(f"Enter number {i + 1}: "))
            number_storage.insert_number(num)

        X = int(input("Enter an integer X to search for: "))

        result = number_storage.find_number(X)

        if result == -1:
            print("X was not found among the numbers entered.")
        else:
            print(f"X was found at index {result}")

    except ValueError:
        print("Invalid input. Please enter valid integers.")


# In[ ]:




