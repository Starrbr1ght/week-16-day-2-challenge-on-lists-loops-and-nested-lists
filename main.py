# # School Supply Order Tracking – Logic Challenge

# ## Objective
# Students will apply their understanding of lists, nested lists, slicing, sorting, list grouping, and logical decision-making to solve a real-world data organization problem without using code.

# ---

# ## Scenario
# You are helping the main office organize student supply requests for the week. Each request includes:

# - Student name  
# - Item requested  
# - Quantity requested  

# All requests must be stored together in one organized system.

# ---

# ## Student Tasks (No Coding – Logic Only)

# ### 1. Create Student Requests
# Create a collection that stores information for **3 different student requests**.  
# Each student request must include:
# - Student name  
# - Item requested  
# - Quantity requested  
requests = []
for _ in range(3):
  name=input("What is your name?")
  item=input("What item do you need?")
  quantity=int(input("How many of this item do you need?"))
  requests.append((name , item, quantity))
  print(requests)

supplies = [row[2] for row in requests]
supplies_sorted = sorted(supplies)
print("Quantities sorted:", supplies_sorted)
# ---

# ### 2. Identify Key Information
# From your collection:
# - Identify the **first student’s name**
# - Identify the **last student’s requested item only**
first_name = requests[0][0]
last_item= requests[-1][1]


# ---

# ### 3. Quantity Extraction
# Create a **separate list that contains only the quantities requested** by the students.
second_position_items = [sublist[1] for sublist in requests]
print(second_position_items)


# ---

# ### 4. Order Size Analysis
# Analyze the quantities:
# - If **any quantity is greater than 5**, label the order:
#   “Large order detected!”
# - Otherwise label the order:
#   “Orders within normal limits.”
# temp= requests
# if temp > 5:
#   print("large order detected")
# else:
#   print("orders within normal limits")
# # ---
quantities = [entry[2] for entry in requests]  # make sure quantity is int

if any(q > 5 for q in quantities):
    print("Large order detected!")
else:
    print("Orders within normal limits.")

# ### 5. Quantity Organization
# Re-organize the quantity list from **smallest to largest** and display the final result.

# ---

# ## Challenge Extension: Classroom Storage Grid

# You are also given a grid showing classroom supply counts:
list=[
Classroom 1: 8, 12, 5  
Classroom 2: 7, 3, 9  
Classroom 3: 10, 6, 4 ] 

# Answer the following:

# 1. What is the **middle number** in the second classroom’s list?'

# 2. Create a new list that extracts **only the last number** from each classroom.
# 3. Explain **why this information must be stored as a nested structure instead of a single list.**

