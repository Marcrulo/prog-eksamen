
'''
Data = {'x': [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
        'y': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7],
       }

with open("game_is_on.json", 'r') as f:
        datastore = json.load(f)

    if datastore["game_is_on"] is False:
        check_is_over = {}
        check_is_over['game_is_on'] = True
        await client.change_presence(game=discord.Game(name="Tavle-leg"))

        # Write data to JSON file
        data = {}
        data['players'] = [ctx.message.author.id]
        data['chosen_things'] = []
        data['theme'] = theme
        data['turn'] = 0

        for item in players:
            num_only_id = re.findall(r'\d+', item)
            data['players'].append(num_only_id[0])
            #data['players'].append({'nick': num_only_id}) # Add nickname

        with open('game_is_on.json', 'w') as outfile:
            json.dump(check_is_over, outfile)

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
'''
import json, csv

path = "C:/Users/marcu/Dropbox/3_skole/SRC/data/PoliticalPref"
files = ["comment_likes", "media_post_likes","tags","political_post_likes"]

columns = []

for file in files:
	with open(path+"/"+file+".json", 'r') as f:
		datastore = json.load(f)

		with open('crowded.csv', 'w', newline='') as myFile:
			writer = csv.writer(myFile)
			#print(datastore['1005592425'].keys())
			for key in datastore['1005592425'].keys() :
				#print(key)
				columns.append(datastore['1005592425'].keys())
			# txt #myFile.write(str(columns))
			# csv #writer.writerow(columns)

