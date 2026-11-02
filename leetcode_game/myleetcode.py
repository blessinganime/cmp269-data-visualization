# creating a list containing three prbolems dictionary. Basically my problem bank which is stored into memory from start of the file
problems_bank = [
    {
        "challenge": "1", 
        "name": "Two Sum", 
        "difficulty": "Easy", 
        "exp_reward": 10,
        "description": "Given an array of integers, return indices of the two numbers such that they add up to a specific target."
        },

    {
         "challenge": "2",
         "name": "Add Two Numbers",
         "difficulty": "Medium",
         "exp_reward": 20,
         "description": "You are given two non-empty linked lists representing two non-negative integers. Add the two numbers and return it as a linked list."
         },

    {
         "challenge": "3",
         "name": "Median of Two Sorted Arrays",
         "difficulty": "hard",
         "exp_reward": 50,
         "description": "Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays",
         },
                  
]

# Now I create a loop to loop through the options of challenges in the prompt bank. Allowing user to click on any three

while True:
    print("----LEETCODE PROBLEMS-----")
    print("1. view Available Quests")
    print("2. Exit")

    choice = input("Chose a quest: ") #this is like java scanner waiting for user to make an option 

    if choice == "1":
        print("---Availaible Quests------")

        
        # This scans our list and prints out the details of each dictionary
        for prob in problems_bank:
            print(f"[{prob['challenge']}] {prob['name']} - {prob['difficulty']} ({prob['exp_reward']} EXP)")

        quest_choice = input("Enter a challenge: ")

        if quest_choice == "1":
            print(f"Quest Name: {problems_bank[0]['name']}")
            print(f"Description: {problems_bank[0]['description']}")
            coding_language = input("Declare your weapon! What digital language did you forge this solution with?")
            solution_details = input("Record your battle strategy! In a short summary, explain how you completed this trial:")
            print("\n[TRIAL CLEAR!] You successfully fulfilled your first contract and earned 10 EXP! \n")


        elif quest_choice == "2":
            print(f"Quest Name: {problems_bank[1]['name']}")
            print(f"Description: {problems_bank[1]['description']}")
            coding_language = input("Declare your weapon! What digital language did you forge this solution with?")
            solution_details = input("Record your battle strategy! In a short summary, explain how you completed this trial:")
            print("\n[✨ QUEST COMPLETED!] Brilliant maneuvers! +20 EXP has been added to your Battle Scroll! \n")

        elif quest_choice == "3":
            print(f"Quest Name: {problems_bank[2]['name']}")
            print(f"Description: {problems_bank[2]['description']}")
            coding_language = input("Declare your weapon! What digital language did you forge this solution with?")
            solution_details = input("Record your battle strategy! In a short summary, explain how you completed this trial:")
            print("\n[ BOSS CONQUERED!] UNBELIEVABLE VICTORY! You claim the 50 EXP Legendary Bounty! \n")

        else:
            print("Quest not found! Return to the main menu and try again")


        quest_end = input("Do you wish to end you adventure for the day? (yes/no): ")

        if quest_end == "yes":
            print("Well done adeventurer! You progress is safe. Logging ogg...")
            break
            


           
            
        
            
    




