#Alison Taylor
#04-08-2017
#Quest tool part 2-Allow users to create new quest data and stores the data in
#an xml file. Allows users to look at a list of existing quest files in the same
#directory as their script,select one, and edits its data

from lxml import etree
import os
import sys
    
def main():
    continueCreatingQuests=True
    questIncrementer = 1
    conversationIncrementer = 1
    stepIncrementer = 1
    questID =""
    questName = ""
    questLevel = 1
    experienceReward = 1
    cashReward = 1
    questDifficulty = ""
    questIsTimed = False
    questTime = 1
    questRewards =list()
    questDescription = ""
    questStepsList=list()
    modifyQuest=False
    scriptDir = sys.path[0]
    fileToModify = ""
    while(continueCreatingQuests == True):
        modifyQuest=willModifyQuest()
        if (modifyQuest == True):
            # show files
            fileToModify=getFileList(scriptDir)

            #modify  file
            questID=getQuestID(fileToModify)
            questName = modifyQuestName(fileToModify)
            questLevel = modifyQuestLevel(fileToModify)
            experienceReward = modifyExperienceReward(fileToModify)
            cashReward = modifyCashReward(fileToModify)
            questDifficulty = modifyQuestDifficulty(fileToModify)
            questIsTimed= modifyQuestIsTimed(fileToModify)
            if questIsTimed == True :
                questTime = modifyQuestTime(fileToModify)
            questRewards = modifyQuestRewards(fileToModify)
            questDescription = modifyQuestDescription(fileToModify)
            questStepsList = modifyQuestStepsList(fileToModify)
        else:
            #get quest data
            questID="QU_"+str(questIncrementer)
            questName = setQuestName()
            questLevel = setQuestLevel()
            experienceReward = setExperienceReward()
            cashReward = setCashReward ()
            questDifficulty= setQuestDifficulty()
            questIsTimed = setQuestIsTimed()
            if questIsTimed == True :
                questTime = setQuestTime()
            questRewards = setQuestRewards()
            questDescription = setQuestDescription()
            questStepsList = setQuestSteps()
            questIncrementer +=1
        writeQuestFile(questID,questName,questLevel,experienceReward,cashReward,questDifficulty, questIsTimed, questTime, questRewards,questDescription,questStepsList)
        continueCreatingQuests = setContinueAddingQuests()

#gets the quests ID
def getQuestID(fileToModify):
    with open (fileToModify, encoding = "utf8") as f:
        tree=etree.parse(f)
        root=tree.getroot()
        return root.tag

#allows for modifying the quest name
def modifyQuestName(fileToModify):
    questName = ""
    with open (fileToModify, encoding = "utf8") as f:
        tree=etree.parse(f)
        root=tree.getroot()
        questName = root.xpath("//quest_name/text()")
    print("The current quest name is "+str(questName[0]))
    print("If you want to change it input a new name, otherwise press 1 : ")
    inputtedData = input()
    if inputtedData == "1":
        return questName[0]
    else:
        return inputtedData

#allows for modifying the quest level
def modifyQuestLevel(fileToModify):
    level = None
    with open (fileToModify, encoding = "utf8") as f:
        tree=etree.parse(f)
        root=tree.getroot()
        level = root.xpath("//quest_level/text()")

    checkInput = None
    while checkInput is None :
        print("The current quest level is " +level[0])
        print("If you would like to change it input a new level ,otherwise press n : ")
        inputtedData = input()
        if inputtedData == "n":
          return level[0]
        else:
            try: checkInput=int(inputtedData)
            except ValueError:
              print("Your input is invalid.")
    return checkInput

#allows for modifying the quest experience reward
def modifyExperienceReward(fileToModify):
    experienceReward = None
    with open (fileToModify, encoding = "utf8") as f:
        tree=etree.parse(f)
        root=tree.getroot()
        experienceReward = root.xpath("//experience_reward/text()")

    checkInput = None
    while checkInput is None :
        print("The current experience reward is " +experienceReward[0])
        print("If you would like to change it input a new experience reward number ,otherwise press n : ")
        inputtedData = input()
        if inputtedData == "n":
          return experienceReward[0]
        else:
            try: checkInput=int(inputtedData)
            except ValueError:
              print("Your input is invalid.")
    return checkInput

#allows for modifying the quest cash reward
def modifyCashReward(fileToModify):
    cashReward = None
    with open (fileToModify, encoding = "utf8") as f:
        tree=etree.parse(f)
        root=tree.getroot()
        cashReward = root.xpath("//cash_reward/text()")

    checkInput = None
    while checkInput is None :
        print("The current cash reward is " +cashReward[0])
        print("If you would like to change it input a new cash reward number ,otherwise press n : ")
        inputtedData = input()
        if inputtedData == "n":
          return cashReward[0]
        else:
            try: checkInput=int(inputtedData)
            except ValueError:
              print("Your input is invalid.")
    return checkInput


#allows for modifying the quest's difficult
def modifyQuestDifficulty(fileToModify):
    difficulty = None
    with open (fileToModify, encoding = "utf8") as f:
        tree=etree.parse(f)
        root=tree.getroot()
        difficulty = root.xpath("//quest_difficulty/text()")

    checkInput = None
    while checkInput is None :
        print("The current quest difficult is " +difficulty[0])
        print("If you would like to change it input a new difficulty level or press 1 : ")
        print("Options are Easy, Standard, Hard, Group, Raid :")
        inputtedData = input()
        if inputtedData == "1":
          return difficulty[0]
        else:
            if inputtedData=="Easy" or inputtedData=="Standard" or inputtedData=="Hard" or inputtedData == "Group" or inputtedData =="Raid" :
                checkInput = inputtedData
            else :
                print("Your input is invalid.")
    return checkInput

#allows for modifying whether or not the quest is timed
def modifyQuestIsTimed(fileToModify):
    isTimed = None
    with open (fileToModify, encoding = "utf8") as f:
        tree=etree.parse(f)
        root = tree.getroot()
        isTimed = root.xpath("//is_quest_timed/text()")
    checkInput = None
    while checkInput is None:
        print("The boolean value for whether or not this quest is timed is currently "+isTimed[0])
        print("If you would like to change it please input True to make it timed and False to make it otherwise.")
        print("If you don't want to change it press 1 :")
        isTimedCheck=input()
        if isTimedCheck == "1" :
            if isTimed[0]=="True":
                return True
            else:
                return False
        elif isTimedCheck == "True":
            checkInput = True
        elif isTimedCheck == "False" :
            checkInput = False
        else:
            print("Your input is invalid.")
            
    return checkInput

#allows for modifying the timer for this quest
def modifyQuestTime(fileToModify):
    timer = None
    with open (fileToModify, encoding = "utf8") as f:
        tree=etree.parse(f)
        root = tree.getroot()
        timer = root.xpath("//quest_time/text()")
    if len(timer) == 0:
        return setQuestTime()
    else:
        checkInput = None
        while checkInput is None :
            print("The current timer for this quest is "+timer[0])
            print("If you would like to change it please input a time amount, otherwise press n: ")
            inputTimer=input()
            if inputTimer == "n" :
              return timer[0]
            else:
              try: checkInput = int(inputTimer)
              except ValueError:
                print("Your input is invalid.")
                pass
              
              
    return checkInput

#allows for modifying the items given as quest rewards
def modifyQuestRewards(fileToModify):
    rewardsList = None
    with open (fileToModify, encoding = "utf8") as f:
        tree=etree.parse(f)
        root=tree.getroot()
        rewardsList = root.xpath("//quest_rewards")[0].getchildren()
    numOfItems=None
    items=list()
    while numOfItems == None :
        print("The current number of items given as rewards is "+str(len(rewardsList)))
        print("If you would like to change the number of items given as rewards please input a number, else input n : ")
        checkInput=input()
        if checkInput == "n":
              numOfItems=len(rewardsList)
        else:
              try: numOfItems = int(checkInput)
              except ValueError:
                print("Your input is invalid")
                pass
    i = 1
    while i!=numOfItems :
        items.append("IT_"+str(i))
        i+=1
    return items
                                                                     
        
    

#allows for modifying the quest description
def modifyQuestDescription(fileToModify):
    questDes = ""
    with open (fileToModify, encoding = "utf8") as f:
        tree=etree.parse(f)
        root=tree.getroot()
        questDes = root.xpath("//quest_description/text()")
    print("The current quest description is "+str(questDes[0]))
    print("If you want to change it input a new description, otherwise press 1 : ")
    inputtedData = input()
    if inputtedData == "1":
        return questDes[0]
    else:
        return inputtedData

#allows for modifying the quest steps
def modifyQuestStepsList(fileToModify):
    stepsList = None
    exploreLocationIncrementer = 0
    conversationNpcIncrementer = 0
    continueAddingSteps = False
    steps=list()
    with open (fileToModify, encoding = "utf8") as f:
        tree=etree.parse(f)
        root=tree.getroot()
        stepsList = root.xpath("//quest_steps")[0].getchildren()
    i=0
    print(stepsList)
    #modify existing steps
    while i!=len(stepsList) :
        #set initial values of step from xml file
        newStep = questStep()
        newStep.stepID = "QS_"+str(i+1)
        print(stepsList[i].getchildren()[0].text)
        newStep.questStepDescription=stepsList[i].getchildren()[0].text
        newStep.stepCompletesQuest=stepsList[i].getchildren()[1].text
        newStep.stepType=stepsList[i].getchildren()[2].text
        if newStep.stepType == "Kill" :
            newStep.killCount=stepsList[i].getchildren()[2][0].text
        elif newStep.stepType == "Explore" :
            exploreLocationIncrementer +=1
            newStep.setExplorationLocation("LOC_"+str(exploreLocationIncrementer))
        elif newStep.stepType == "Conversation" :
            conversationNpcIncrementer += 1
            newStep.setConversationNpc("CO_"+str(conversationNpcIncrementer))
        newStep.nextStep = stepsList[i].getchildren()[3].text
        steps.append(newStep)
        i+=1
        #modify step values if wanted
    n=0
    while n!=i:
        steps[n].questStepDescription=steps[n].modifyQuestStepDescription()
        steps[n].stepCompletesQuest=steps[n].modifyDoesStepCompleteQuest()
        steps[n].stepType=steps[n].modifyStepType()
        if steps[n].stepType == "Kill" :
            steps[n].killCount=steps[n].modifyKillCount()
        elif steps[n].stepType == "Explore" :
            exploreLocationIncrementer +=1
            newStep.setExplorationLocation("LOC_"+str(exploreLocationIncrementer))
        elif steps[n].stepType == "Conversation" :
            conversationNpcIncrementer += 1
            newStep.setConversationNpc("CO_"+str(conversationNpcIncrementer))
        steps[n].modifyNextStep(steps)
        n+=1

    continueAddingSteps = continueAddingStepsChoice()
    questStepIncrementer=len(steps)
    #add more steps to the quest if user chooses to
    while continueAddingSteps==True:
        newStep = questStep()
        questStepIncrementer +=1
        newStep.stepID = "QS_"+str(questStepIncrementer)
        newStep.questStepDescription = newStep.setQuestStepDescription()
        newStep.setDoesStepCompleteQuest()
        newStep.stepType = newStep.setStepType()
        if newStep.stepType == "Kill" :
            newStep.setKillCount()
        elif newStep.stepType == "Explore" :
            exploreLocationIncrementer += 1
            newStep.exploreLocation="LOC_"+str(exploreLocationIncrementer)
        elif newStep.stepType == "Conversation" :
            conversationNpcIncrementer += 1
            newStep.conversationNpc = "CO_"+str(conversationNpcIncrementer)
        newStep.nextStep = newStep.setNextStep(steps)
        steps.append(newStep)
        continueAddingSteps = continueAddingStepsChoice()
       
    return steps
              
        
#sets the name for this quest
def setQuestName():
    name = ""
    print("Please input the name for your quest: ")
    name = input()
    return name

#sets the level for this quest
def setQuestLevel():
    level = None
    while level is None :
        print("Please input the level for your quest: ")
        try: level = int(input())
        except ValueError:
            print("Your input is invalid.")
            pass
    return level

#sets the experience amount rewarded for completing this quest
def setExperienceReward():
    expReward = None
    while expReward is None :
        print("Please input the experience amount rewarded by your quest: ")
        try: expReward = int(input())
        except ValueError:
            print("Your input is invalid.")
            pass
    return expReward

#sets the experience amount rewarded for completing this quest
def setCashReward():
    cashReward = None
    while cashReward is None :
        print("Please input the cash amount rewarded by your quest: ")
        try: cashReward = int(input())
        except ValueError:
            print("Your input is invalid.")
            pass
    return cashReward

#sets the quest difficulty for this quest
def setQuestDifficulty():
    questDiff = None
    checkDiff = ""
    while questDiff is None :
        print("Please input the difficulty level for your quest")
        print("Options are Easy, Standard, Hard, Group, Raid : ")
        checkDiff = input()
        if checkDiff=="Easy" or checkDiff=="Standard" or checkDiff=="Hard" or checkDiff == "Group" or checkDiff =="Raid" :
            questDiff=checkDiff
        else :
            print("Your input is invalid.")

    return questDiff

#sets whether or not this quest is timed
def setQuestIsTimed():
    isTimed = None
    while isTimed is None:
        print("Please input True if this quest is timed and False otherwise : ")
        isTimedCheck=input()
        if isTimedCheck == "True":
            isTimed = True
        elif isTimedCheck == "False" :
            isTimed = False
        else:
            print("Your input is invalid.")
            
    return isTimed

#sets the amount of time for this quest
def setQuestTime():
    time = None
    while time is None :
        print("Please input the timer for this quest: ")
        try: time = int(input())
        except ValueError:
            print("Your input is invalid.")
            pass
    return time

#sets the list of item rewards for this quest
def setQuestRewards():
    itemIncrementer = 1
    items = list()
    numOfItems = None
    while numOfItems is None:
        print("Please input the number of items this quest rewards : ")
        try: numOfItems = int(input())
        except ValueError:
            print("Your input is invalid")
            pass
    i = 1
    while i!=numOfItems :
        items.append("IT_"+str(i))
        i+=1
    return items

#sets the description for this quest
def setQuestDescription():
    description = ""
    print("Please input the description for this quest: ")
    description = input()
    return description
            

#sets the steps for this quest
def setQuestSteps():
    continueAddingSteps= True
    steps = list()
    questStepIncrementer = 0
    exploreLocationIncrementer = 0
    conversationNpcIncrementer= 0
    while continueAddingSteps == True:
        newStep = questStep()
        questStepIncrementer +=1
        newStep.stepID = "QS_"+str(questStepIncrementer)
        newStep.questStepDescription=newStep.setQuestStepDescription()
        newStep.setDoesStepCompleteQuest()
        newStep.stepType = newStep.setStepType()
        if newStep.stepType == "Kill" :
            newStep.setKillCount()
        elif newStep.stepType == "Explore" :
            exploreLocationIncrementer += 1
            newStep.exploreLocation="LOC_"+str(exploreLocationIncrementer)
        elif newStep.stepType == "Conversation" :
            conversationNpcIncrementer += 1
            newStep.conversationNPC = "CO_"+str(conversationNpcIncrementer)
        newStep.nextStep = newStep.setNextStep(steps)
        steps.append(newStep)
        continueAddingSteps = continueAddingStepsChoice()
    return steps

#sets whether or not the user wants to continue adding steps
def continueAddingStepsChoice():
    choice = 0
    print ("Would you like to add another step to this quest? ")
    print ("Type 1 to keep adding steps or input anything else to stop making steps ")
    choice = input()
    if choice != "1":
      return False
    else:
      return True

#sets whether or not the user wants to continue creating or modifying quests
def setContinueAddingQuests():
    choice =0
    print ("Would you like to continue creating and modifying quest data? ")
    print ("Type 1 to continue or input anything else to exit ")
    choice = input()
    if choice != "1":
      return False
    else:
      return True

#sets whether or not the user wants to modify a quest
def willModifyQuest():
    choice = 0
    print ("Would you like to modify a quest or create a new quest? ")
    print ("Type 1 to modify a quest or input anything else to create a quest")
    choice = input ()
    if choice != "1" :
        return False
    else:
        return True

#gets the list of files that can be modified as well as lets the user select a file to modify
def getFileList(scriptDir):
    fileChoice = None
    files = os.listdir(scriptDir)
    questFiles= list()
    for file in files :
        if ".xml" not in file:
            #do nothing
            continue
        else:
            if "QU_" not in file:#make sure this program only tries to modify quest data xml files
                continue
            else:
                questFiles.append(file)
    i=1       
    for questFile in questFiles:
        print (str(i)+". "+questFile)
        i+=1
    while fileChoice is None:
        print("Please input the number of the corresponding quest data file you would like to modify: ")
        try:
            fileChoice=int(input())
            fileChoice<=len(questFiles)
        except ValueError:
            print("Your input is invalid")
            pass
    return questFiles[fileChoice-1]
    

#writes the xml data file
def writeQuestFile(questID,questName,questLevel,experienceReward,cashReward,questDifficulty, questIsTimed, questTime, questRewards,questDescription,questStepsList) :
    root = etree.Element(questID)
    questNameChild=etree.Element('quest_name')
    questNameChild.text=questName
    root.append(questNameChild)
    questLevelChild=etree.Element('quest_level')
    questLevelChild.text=str(questLevel)
    root.append(questLevelChild)
    experienceRewardChild=etree.Element('experience_reward')
    experienceRewardChild.text=str(experienceReward)
    root.append(experienceRewardChild)
    cashRewardChild=etree.Element('cash_reward')
    cashRewardChild.text=str(cashReward)
    root.append(cashRewardChild)
    questDifficultyChild = etree.Element('quest_difficulty')
    questDifficultyChild.text=questDifficulty
    root.append(questDifficultyChild)
    questIsTimedChild = etree.Element('is_quest_timed')
    questIsTimedChild.text = str(questIsTimed)
    root.append(questIsTimedChild)
    if questIsTimed == True :#put time in the xml file only if the quest is time
        questTimeChild=etree.Element('quest_time')
        questTimeChild.text=str(questTime)
        root.append(questTimeChild)
    questRewardsChild = etree.Element('quest_rewards')
    i = 0
    while i!=len(questRewards) :
        questRewardsElement=etree.Element(questRewards[i])
        questRewardsChild.append(questRewardsElement)
        i+=1
    root.append(questRewardsChild)
    questDescriptionChild = etree.Element('quest_description')
    questDescriptionChild.text=questDescription
    root.append(questDescriptionChild)
    questStepsChild = etree.Element('quest_steps')
    j=0
    while j!=len(questStepsList) :
        stepElement =etree.Element(questStepsList[j].stepID)
        stepDesElement = etree.Element("step_description")
        stepDesElement.text=questStepsList[j].questStepDescription
        stepElement.append(stepDesElement)
        stepCompletesElement = etree.Element('step_completes_quest_bool')
        stepCompletesElement.text=str(questStepsList[j].stepCompletesQuest)
        stepElement.append(stepCompletesElement)
        stepTypeElement = etree.Element('step_type')
        stepTypeElement.text=questStepsList[j].stepType
        stepElement.append(stepTypeElement)
        if questStepsList[j].stepType == 'Kill' :
            killCountElement = etree.Element('kill_count')
            killCountElement.text= str(questStepsList[j].killCount)
            stepTypeElement.append(killCountElement)
        elif questStepsList[j].stepType == 'Explore' :
            exploreLocElement = etree.Element('explore_location')
            exploreLocElement.text= questStepsList[j].exploreLocation
            stepTypeElement.append(exploreLocElement)
        elif questStepsList[j].stepType == 'Conversation' :
            conversationNpcElement = etree.Element('conversation_NPC')
            conversationNpcElement.text= questStepsList[j].conversationNPC
            stepTypeElement.append(conversationNpcElement)
        stepsNextStepElement = etree.Element("next_step_ID")
        stepsNextStepElement.text=questStepsList[j].nextStepID
        stepElement.append(stepsNextStepElement)
        questStepsChild.append(stepElement)
        j+=1
    root.append(questStepsChild)

    tree = etree.ElementTree(root)
    tree.write(questID+"Data.xml")

        
       
class questStep :
    stepID=""
    nextStepID=""
    questStepDescription = ""
    stepCompletesQuest = False
    stepType=""
    killCount = 1
    exploreLocation = ""
    conversationNPC = ""

    #create a questStep
    def __init__(self):
        stepID=""
        questStepDescription = ""
        stepCompletesQuest = False
        stepType=""
        killCount = 1
        exploreLocation = ""
        conversationNPC = ""
        
    #sets the description for this quest step
    def setQuestStepDescription(self):
        description = ""
        print("Please input the description for this quest step: ")
        description = input()
        return description

    #sets whether or not this step completes the quest
    def setDoesStepCompleteQuest(self):
        doesStepCompleteQuest = None
        while doesStepCompleteQuest is None:
            print("Please input True if this step completes the quest and False otherwise : ")
            doesStepCompleteQuestCheck=input()
            if doesStepCompleteQuestCheck == "True":
                doesStepCompleteQuest = True
            elif doesStepCompleteQuestCheck == "False" :
                doesStepCompleteQuest = False
            else:
                print("Your input is invalid.")
           
        return doesStepCompleteQuest

    #sets the type of step this is
    def setStepType(self):
        stepKind = None
        checkStepKind = ""
        while stepKind is None :
            print("Please input the type of step this is")
            print("Options are Kill, Explore, Conversation : ")
            checkStepKind = input()
            if checkStepKind=="Kill" or checkStepKind=="Explore" or checkStepKind=="Conversation" :
                stepKind=checkStepKind
            else :
                print("Your input is invalid.")

        return stepKind

    #sets the number of kills required for this step
    def setKillCount(self):
        killAmount = None
        while killAmount == None :
            print("Please input the number of enemies to kill for this quest: ")
            try: killAmount = int(input())
            except ValueError:
                print("Your input is invalid.")
                pass
        return killAmount

    #sets the ID for the next step
    def setNextStep(self,steps):
        stepChoice = None
        print("Below are the current steps available to set as the next step: ")
        i=1
        for step in steps:
              print(str(i)+". "+step.stepID)
              i+=1
        while stepChoice is None:
            print("Please input the number corresponding to the step you would like to make the next step. If there are no current steps input 0: ")
            try:
                stepChoice=int(input())
                stepChoice<=len(steps)
            except ValueError:
                print("Your input is invalid")
                pass
        self.nextStepID="QS_"+str(stepChoice)
       
    #sets the conversation npcs id
    def setConversationNpc(self, npc):
        self.conversationNPC=npc

    def setExplorationLocation(self,loc):
        self.explorationLocation=loc

    #allows the user to modify the description for this quest step
    def modifyQuestStepDescription(self):
        description = ""
        print("The current quest step description is "+self.questStepDescription)
        print("Please input a new description if you would like to change it, otherwise input 1: ")
        description = input()
        if description =="1":
              return self.questStepDescription
        else:
            return description

    #modifes whether or not this step completes the quest
    def modifyDoesStepCompleteQuest(self):
        doesStepCompleteQuest = None
        while doesStepCompleteQuest is None:
            print("The current bool for whether or not this step completes the quest is "+str(self.stepCompletesQuest))
            print("Please input True if you would like to make this step complete the quest and False otherwise ")
            print("You can also input 1 to keep the current setting :")
            doesStepCompleteQuestCheck=input()
            if(doesStepCompleteQuestCheck == "1"):
                  return self.stepCompletesQuest
            elif doesStepCompleteQuestCheck == "True":
                doesStepCompleteQuest = True
            elif doesStepCompleteQuestCheck == "False" :
                doesStepCompleteQuest = False
            else:
                print("Your input is invalid.")
           
        return doesStepCompleteQuest

    #modifes the type of step this is
    def modifyStepType(self):
        stepKind = None
        checkStepKind = ""
        while stepKind is None :
            print("The current step type is "+self.stepType)
            print("Please input the type of step you would like to change this to")
            print("Options are Kill, Explore, Conversation ")
            print("You may also input 1 to keep the current step type : ")
            checkStepKind = input()
            if checkStepKind=="Kill" or checkStepKind=="Explore" or checkStepKind=="Conversation" :
                stepKind=checkStepKind
            elif checkStepKind == "1":
                stepKind = self.stepType
            else :
                print("Your input is invalid.")

        return stepKind

    #modifes the number of kills required for this step
    def modifyKillCount(self):
        killAmount = None
        while killAmount == None :
            print("The current kill amount is: "+self.killCount)
            print("Please input a new number of enemies to kill for this quest step if you would like to change it or input n to keep the current num: ")
            numberCheck=input()
            if numberCheck == "n":
                  return self.killCount
            else:
                try: killAmount = int(numberCheck)
                except ValueError:
                    print("Your input is invalid.")
                    pass
        return killAmount

    #modifies the ID for the next step
    def modifyNextStep(self,steps):
        stepChoice = None
        print("The current next step's ID is : "+self.nextStepID)
        print("Below are the current steps available to set as the next step: ")
        i=1
        for step in steps:
              print(str(i)+". "+step.stepID)
              i+=1
        while stepChoice is None:
            print("Please input the number corresponding to the step you would like to make the next step ")
            print("If you would like to keep the current setting please press n : ")
            stepChoiceCheck= input()
            if stepChoiceCheck == "n":
               stepChoice=self.nextStepID
            else:
                try:
                    stepChoice=int(stepChoiceCheck)
                    stepChoice<=len(steps)
                except ValueError:
                    print("Your input is invalid")
                    pass
        self.nextStepID="QS_"+str(stepChoice)
        
        
if __name__ == "__main__":
    main()    

       

