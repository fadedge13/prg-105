import Question

def main():
    q1 = Question.questions("What was the term used for submarine, by the Germans, during WWI? ", "a. U-boat",
                           "b. Underwater fighter", "c. Subnauticle Ship", "d. None of the Above", "a")
    q2 = Question.questions("What was the first functional tank called?", "a. Big Bertha", "b. PanzerI", "c. Renault Ft",
                           "d. Big Willie", "d")
    q3 = Question.questions("When did the WWI Christmas miracle take place?", "a. 1919", "b. 1912", "c. 1914", "d. 1915",
                           "c")
    q4 = Question.questions("Winston Churchill attained what position during the opening years of WWI?",
                           "a. Lord of the Admiralty", "b. Duke of the General Staff", "c. Lord Protector of the North",
                           "d. Grandmaster of the Knights Templar", "a")
    q5 = Question.questions("What campaign failled in 1916 in modern Turkey?",
                           "a. The Ardennes campaign", "b. The Gallipoli campaign", "c. The Third Ypres campaign",
                           "d. The Brusilov Offensive", "b")
    q6 = Question.questions("What caused America to enter the war?",
                           "a. Unrestricted Submarine Warefare", "b. The Zimmerman Note",
                           "c.Economic ties to the allies", "d. All of the Above", "d")
    q7 = Question.questions("Who shot down the German Fighter Ace Manfred Von Richthofen the Red Baron?",
                           "a. French flak guns", "b. No one he lost control of his plane", "c. Lt. Wilfrod May",
                           "d. Mj. Frank Williams", "c")
    q8 = Question.questions("When did World War I officially begin?",
                           "a. June 28, 1914", "b. July 28, 1914", "c. April 6, 1917", "d. November 11, 1918", "b")
    q9 = Question.questions("What treaty ended Russia's involvment with WWI?",
                           "a. the Molotove-Ribbentrop pact", "b. the Treaty of Versailles",
                           "c. Treaty of Brest-Litovsk", "d. Treaty of Bretigny", "c")
    q10 = Question.questions("Who were the Central Powers?",
                            "a. Germany, Austria-Hungry, and the Ottoman Empire", "b. France, England, and Russia",
                            "c. Italy, France, and Japan", "d. Japan, China, and America", "a")
    set_1 = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
    player_1 = 0
    player_2 = 0

    for Quest in set_1:
        print(Quest.get_questions())
        print(Quest.get_a1())
        print(Quest.get_a2())
        print(Quest.get_a3())
        print(Quest.get_a4())
        guess = input("Guess an Answer..")
        if guess == Quest.get_answer():
            player_1 = 1
            player_2 = 1
        else:
            print("No")
        if player_1 > player_2:
            print("Player 1 wins!")
        elif player_2 > player_1:
            print("Player 2 wins!")
        elif player_1 == player_2:
            print("Player's 1 and 2 tie.")

main()
