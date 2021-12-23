import constants

player_list =[]
panthers=[]
bandits =[]
warriors=[]

#cleans player data from the player list in the constants file
def clean_data():
  
  for item in constants.PLAYERS:    
    height = int(item['height'][0:2])
    if item['experience'] == "NO":
      experience = False
    else: 
      experience = True
    guardians = list(item['guardians'].split(" and "))
    
    dictionary ={
      'name': item['name'],
      'guardians': guardians,
      'experience': experience,
      'height': height
    }
    player_list.append(dictionary)
    
#Evenly distributes the players
def balance_teams():
  players_per_team =int(len(constants.PLAYERS) / len(constants.TEAMS))
  experienced_count = 0
  inexperienced_count = 0
  experienced_list = []
  inexperienced_list = []
  
  # Create a loop that counts the number of experienced and inexperienced players on the team
  for player in constants.PLAYERS:
    if player['experience'] == 'YES':
      experienced_count += 1
    elif player['experience'] == 'NO':
      inexperienced_count += 1
  inexperienced_per_team = int(inexperienced_count / len(constants.TEAMS))
  experienced_per_team = int(inexperienced_count / len(constants.TEAMS))
  
  #Exceeds Expectations: balances the number of inexperienced and experienced players on each team
  for player in player_list:
    if player['experience'] == True:
      experienced_list.append(player)
    elif player['experience'] == False:
      inexperienced_list.append(player)
      
  for x in range(0, experienced_per_team):    
    panthers.append(experienced_list.pop())
    bandits.append(experienced_list.pop())
    warriors.append(experienced_list.pop())
  for x in range(0, inexperienced_per_team):    
    panthers.append(inexperienced_list.pop())
    bandits.append(inexperienced_list.pop())
    warriors.append(inexperienced_list.pop())
  
#Takes in a team's name as input and displays the stats for a particuar team
def display_stats(team_name):
  experienced_count = 0
  inexperienced_count = 0
  total_height = 0
  names_list =[]
  guardians_list = []
  
  print("Total players: {}".format(len(team_name)))
  #Exceeds Expectations: Sorts the players by height
  team_name = sorted(team_name, key = lambda i: i['height'])

  
  for player in team_name:
    total_height += player['height']
    if player['experience'] == True:
      experienced_count += 1
    elif player['experience'] == False:
      inexperienced_count += 1
    names_list.append(player['name'])
    guardians_list.extend(player['guardians'])
            
  print("Total experienced: {}".format(experienced_count))
  print("Total inexperienced: {}".format(inexperienced_count))
  print("Average height: {}".format(total_height/len(team_name)))
  
  print("\nPlayers on Team: ")
  print(",".join(names_list))
  
  print("\nGuardians: ")
  print(",".join(guardians_list))
  
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  
  #Exceeds Expectations: Saved the Team's Analysis as a dictionary and returns it when the method has executed
  team_stats = {'total_experienced' : experienced_count, 'total_inexperienced' : inexperienced_count, 'height': total_height/len(team_name)}
  return team_stats
  
# Main function in the program that prompts the user and displays the teams' stats
# Exceeds Expectations: The user is returned to the main menu until they select "Quit"
def basketball_stats():
  while True: 
    print("\nBASKETBALL TEAM STATS TOOL")
    print("\n\n---- MENU----")
    print("\n\nHere are your choices: \n A) Display Team Stats\n B) Quit")
    first_response = input("\n\nEnter an option: ")
    if first_response.lower() == "b": 
      print("\nI hope you play again soon!")
      break
    if first_response.lower() == "a":
      print("\n\nA) Panthers \nB) Bandits \nC) Warriors")
      second_response = input("\nEnter an option: ")
      if second_response.lower() == "a":
        print("Team: Panthers Stats")
        print("--------------------")
        panthers_stats = display_stats(panthers)
        continue
      elif second_response.lower() == "b":
        print("Team: Bandits Stats")
        print("--------------------")
        bandits_stats =display_stats(bandits)
        continue
      elif second_response.lower() == "c":
        print("Team: Warriors Stats")
        print("--------------------")
        warriors_stats =display_stats(warriors)
        continue
      else: 
        print("\nPlease enter a valid response(a/b/c)")
        continue       
    else:
      print("\nPlease enter a valid response(a/b)")
      continue
    
if __name__ == "__main__":
  clean_data()
  balance_teams()
  basketball_stats()
