"""
Author: Ivan Leffalle
Course: CSE 110
"""
#Instruction for users
print("Welcome to this game created by Ivan Leffalle. I hope you enjoy the adventure.")
print("Instructions: Once the story starts, you will have 2 options. To choose one you must write the word that is in capital letters as an option")
print("Let's get started")
print("")
#the game starts
print("\nYou find yourself standing at the edge of a dense and mysterious forest known as the Forbidden Forest. Legends say it's filled with perilous creatures and hidden treasures. Do you dare to enter?")
forest = input("1. ENTER the forest\n2. Turn BACK\n")

if forest.lower() == "enter":
    print("\nYou enter the forest and soon come to a fork in the road.")
    path = input("1. Take the LEFT path\n2. Take the RIGHT path\n")
    if path.lower() == "left":
        print("\nAs you continue down the path, you stumble upon a clearing in the forest. In the center of the glade, you see a shimmering pool of water, surrounded by lush vegetation.")
        level_2 = input("1.Approach the POOL cautiously\n2.EXPLORE the surrounding area\n")
        if level_2.lower() == "pool":
            print("\nAs you approach the pool, a small sprite emerges from the water. It greets you warmly and offers you a magical potion.")
            level_3a = input("1.ACCEPT the potion and drink it\n2.Politely DECLINE the potion\n")
            if level_3a.lower() == "accept":
               print("\nYou accept the potion and drink it. Instantly, you feel a surge of energy coursing through your veins. The sprite smiles and tells you that you are now blessed with good fortune. You continue your journey feeling invigorated and lucky.") 
            if level_3a.lower() == "decline":
               print("\nYou politely decline the potion, thanking the sprite for its offer. The sprite nods appreciatively and disappears into the pool. As you leave the glade, you feel a sense of respect for the creatures of the forest.") 
        elif level_2.lower() == "explore":
            print("\nYou explore the surrounding area and discover a hidden stash of treasure buried beneath a tree.")
            level_3b = input("1.TAKE the treasure and continue your journey\n2.LEAVE the treasure undisturbed and continue your journey\n")
            if level_3b.lower() == "take":
                 print("\nYou take the treasure and continue your journey, feeling victorious. However, as you leave the glade, you are ambushed by bandits who were watching the treasure. They steal everything you have, leaving you penniless and defeated.")
            if level_3b.lower() == "leave":
                 print("\nYou leave the treasure undisturbed, knowing that it's not yours to take. As you continue your journey, you feel a sense of honor and integrity. The forest seems to welcome you as you proceed deeper into its mysteries.")      
    if path.lower() =="right":
        print("\nYou choose the right path and soon encounter another crossroads:")
        level_2b = input("1.Follow the narrow path UPHILL\n2.Descend into the dark CAVERN\n")
        if level_2b.lower() == "uphill":
            print("\nYou climb uphill and reach a high vantage point, offering a breathtaking view of the entire forest. However, you also spot a menacing creature lurking nearb")
            level_3b2 = input("1.CONFRONT the creature\n2.RETREAT quietly\n")
            if level_3b2.lower() == "confront":
                print("\nI'm sorry. You died")
            if level_3b2.lower() == "retreat":
                print("\nGood choice! you lived to tell the story")       
        if level_2b.lower() =="cavern":
            print("\nYou descend into the dark cavern and find yourself surrounded by glittering crystals. In the dim light, you notice a mysterious artifact lying in the corner:")
            level3b3 = input("1.Approach the ARTIFACT\n2.Continue EXPLORING the cavern\n")
            if level3b3.lower() == "artifact":
                print("\nyou choosed Approach the artifact")
            if level3b3.lower() == "exploring":
                print("\nyou want to Continue exploring the cavern ")
        else:
            print("I'm sorry that is not an option")     
    else:
        print("I'm sorry that is not an option")        
#If the user simply chooses back, the game ends        
elif forest.lower() == "back":
    print("You choosed turn back")
else:
        print("I'm sorry that is not an option")     
            







