import pandas as pd
from colorama import Fore

df = pd.read_csv("unclean_data.csv")

df = df.rename(columns= {'movie_title': 'Movie_Title', 'num_critic_for_reviews': 'Critic_Number', 'duration': 'Time',
                         'DIRECTOR_facebook_likes': 'Director_Likes', 'actor_3_facebook_likes': 'Actor3_Likes',
                         'ACTOR_1_facebook_likes': 'Actor1_Likes', 'gross': 'Sell', 'num_voted_users': 'Voted_Users',
                         'Cast_Total_facebook_likes': 'Cast_Likes', 'num_user_for_reviews': 'Reviews_Users',
                         'budget': 'Budget', 'title_year': 'Released_Year',
                         'ACTOR_2_facebook_likes': 'Actor2_Likes', 'imdb_score': 'Imdb_Score'})

df = df.drop(['title_year.1', 'facenumber_in_poster'], axis= 1)
df = df.fillna(0)

df['Movie_Title'] = df['Movie_Title'].str.split(pat= '?').str[0]

df = df.astype({'Actor1_Likes': 'float', 'Actor3_Likes': 'float'})
df['Actors_Likes'] = (df['Actor1_Likes'] + df['Actor2_Likes'] + df['Actor3_Likes']) / 3
df = df.drop(['Actor1_Likes', 'Actor2_Likes', 'Actor3_Likes'], axis= 1)

df['Avg_Users'] = (df['Voted_Users'] + df['Reviews_Users']) / 2
df = df.drop(['Voted_Users', 'Reviews_Users'], axis= 1)

df.loc[[1, 3, 6, ], 'Time'] = 168, 165, 100
df.loc[4, 'Director_Likes'] = 475

df = df.astype({'Time': 'int', 'Cast_Likes': 'int', 'Actors_Likes': 'int',
                'Avg_Users': 'int'})

print(df, Fore.YELLOW + "\nTop Sell : ", df['Sell'].max(),
      Fore.GREEN + '\nLess Budget : ', df['Budget'].min(),
      Fore.BLUE + '\nLatest Released : ', df['Released_Year'].max(),
      Fore.RED + '\nTop IMDb Score : ', df['Imdb_Score'].max())