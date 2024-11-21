#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:    W0499622 
#Student Name:  Jack Leonard

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # realised after making this that a 2d array would wok really well

    guidesNum = int(input("Please enter the number of guides selling cookies: ")) #makes user enter number of guides, used in for loop later
    guidesNames = [] #empty list used for guide names
    guidesBoxes = [] #empty list used for guide boxes
    totalBoxes = 0 #starting number of boxes
    guidesBadges = [] # empty list used to reference badges to specific guides later
    



    for i in range(guidesNum):
        guidesNames.append(input("Enter name of guide {0}: ".format(i+1))) # adds guide names to list
        guidesBoxes.append(int(input("Enter the number of boxes sold by {0}: ".format(guidesNames[i])))) #adds guides number of boxes to a seperate list
        totalBoxes += guidesBoxes[i] #used to get the total amount of boxes for later calculation
    
    averageBoxes = totalBoxes / guidesNum # calculates the average number of boxes
    print("The average number of boxes sold is {0} \n".format(averageBoxes)) #prints the average number of boxes sold

    currentHighest = 0 #used to keep track of who currently has the highest amt of boxes sold
    bestGuide = 0 #used to keep track of the index of the guide with the most sold 
    for i in range(guidesNum):
        if guidesBoxes[i] > currentHighest:
            currentHighest = guidesBoxes[i] #keeps track of current highest amt sold
            bestGuide = i # keeps track of current best girl guide
        if guidesBoxes[i] == 0: # no award for not selling any :(
            guidesBadges.append("")
        elif guidesBoxes[i] > averageBoxes:
            guidesBadges.append("Super Seller Badge") #award for selling more than average
        elif guidesBoxes[i] < averageBoxes:
            guidesBadges.append("Left over cookies") #award for selling less than average

    guidesBadges[bestGuide] = "Trip to Girl Guide Jamboree in Aruba!" #gives the highest award to best guide

    print("Guide:    Prizes won:\n-----------------------------------------") #formatting print statement so the organization of information makes sense
    for i in range(guidesNum): #for printing through each guide and their awards
        print("{0}     -{1}".format(guidesNames[i],guidesBadges[i]))



    # YOUR CODE ENDS HERE

main()