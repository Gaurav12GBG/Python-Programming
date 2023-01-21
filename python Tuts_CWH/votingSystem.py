nominee_1 = input("Please enter your name : ")
nominee_2 = input("Please enter your name : ")

nom_1 = 0
nom_2 = 0

votes_id = [1, 2, 3, 4]

num_of_votes = len(votes_id)

while True:
    age = int(input("Enter your true age because your age is verified with voterlist :"))
    if age < 18:
        print("Sorry, You are not allowed for vote because of less age than 18 !! Please try after 18")
    else:
        voter_id = int(input("Please enter your voting Id : "))
        if votes_id == []:
            print("Voting session is over now!!")

            if nom_1 > nom_2:
                percent = (nom_1/num_of_votes)*100
                print(nominee_1,"is a winner! with", percent, "% of vote")
                break
            else:
                percent = (nom_2/num_of_votes)*100
                print(nominee_2,"is a winner! with", percent, "% of vote")
                break
    
        else:
            if voter_id in votes_id:
                print(f"1 for {nominee_1} \n2 for {nominee_2}")
                vote = int(input("Please give your vote either 1 or 2 :"))
                votes_id.remove(voter_id)
            
                if vote == 1:
                    nom_1 += 1
                    print(f"Thanks for voting , Your vote for {nominee_1} casted successfully !!")
                else:
                    nom_2 += 2
                    print(f"Thanks for voting , Your vote for {nominee_2} casted successfully !!")
            else:
                print("You are not a voter or you are already voted !!")

