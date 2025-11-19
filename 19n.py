# The Shopping Cart: where all your tasks will be stored
tasks = [] 

# The Receptionist: keeps asking what you want to do
while True:
    print("\n--- MENU ---")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Remove a Task  <-- NEW FEATURE")
    print("4. Exit Program")

    choice = input("Enter your choice (1-4): ")

    # ... (Code for 1 and 2 remains the same) ...
    if choice == '1':
        # 1. ADD TASK
        new_task = input("What is the new task? ")
        tasks.append(new_task) 
        print(f"✅ Task '{new_task}' added!")

    elif choice == '2':
        # 2. VIEW TASKS
        if not tasks:
            print("ℹ️ Your list is empty! Add a task first.")
            continue

        print("\n--- YOUR TO-DO LIST ---")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
        print("-----------------------")
    
    elif choice == '3':
        # 3. REMOVE TASK
        if not tasks:
            print("ℹ️ Cannot remove. The list is currently empty.")
            continue

        # First, show the list so the user knows what numbers to use
        print("\n--- Current Tasks ---")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
        print("---------------------")

        # Get the number from the user
        task_num_to_remove = input("Enter the NUMBER of the task to remove: ")
        
        # --- NEW REMOVAL LOGIC ---
        try:
            # Convert user's number (1, 2, 3...) to Python's index (0, 1, 2...)
            index_to_remove = int(task_num_to_remove) - 1

            # Check if the number is valid (e.g., the user didn't type 99)
            if 0 <= index_to_remove < len(tasks):
                
                # Action: Use .pop() to remove the item at that position
                removed_task = tasks.pop(index_to_remove)
                print(f"🗑️ Task '{removed_task}' removed!")
            else:
                print("❌ Invalid number. Please enter a number shown on the list.")
        
        # Catch the error if the user types letters instead of numbers
        except ValueError:
            print("❌ Invalid input. Please enter a valid task number.")


    elif choice == '4':
        # 4. EXIT
        print("👋 Goodbye! Tasks are not saved.")
        break

    else:
        print("⚠️ Invalid choice. Please try again.")