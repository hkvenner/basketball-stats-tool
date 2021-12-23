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
    
#Evenly distributes the players in the list of players among three different teams
def balance_teams():
  players_per_team =int(len(constants.PLAYERS) / len(constants.TEAMS))
  for x in range(0, players_per_team):    
    panthers.append(player_list.pop())
  for x in range(0, players_per_team):
    bandits.append(player_list.pop())
  for x in range(0, players_per_team):
    warriors.append(player_list.pop())
 
#Takes in a team's name as input and displays the stats for a particuar team
def display_stats(team_name):
  experienced_count = 0
  inexperienced_count = 0
  total_height = 0
  names_list =[]
  guardians_list = []
  
  print("Total players: {}".format(len(team_name)))
  
  for player in team_name:
    #print(player)
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
  
# Main function in the program that prompts the user and displays the teams' stats
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
        display_stats(panthers)
      elif second_response.lower() == "b":
        print("Team: Bandits Stats")
        print("--------------------")
        display_stats(bandits)
      elif second_response.lower() == "c":
        print("Team: Warriors Stats")
        print("--------------------")
        display_stats(warriors)
      else: 
        print("\nPlease enter a valid response(a/b/c)")
        continue
      third_response = input("\nDo you want to return to the beginning of the program? (Enter yes/no): ")
      while third_response.lower() != 'yes' and third_response.lower() != 'no':
        third_response = input("\nPlease enter a valid response. Do you want to return to the beginning of the program? (Enter yes/no): ")
        
      if third_response.lower() == "yes":
        continue
      elif third_response.lower() == "no":
        print("\nThanks for checking out the stats!")
        break      
    
if __name__ == "__main__":
  clean_data()
  balance_teams()
  basketball_stats()
