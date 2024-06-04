#
import pandas as pd
import matplotlib.pyplot as plt


netflix_df = pd.read_csv("netflix_data.csv")


sorted_by_mostfrequent_duration = netflix_df.sort_values("duration",ascending=False)
movies_in_1990 = sorted_by_mostfrequent_duration.loc[(sorted_by_mostfrequent_duration["release_year"] >= 1990) & (sorted_by_mostfrequent_duration["release_year"] < 2000) & (sorted_by_mostfrequent_duration["type"] == "Movie")]
duration = movies_in_1990["duration"].agg("median")

short_movie_count = movies_in_1990.loc[(movies_in_1990["duration"] < 90) & (movies_in_1990["genre"] == "Action")].shape[0]

short_movie_count_2 = 0
# Iterate over the labels and rows of the DataFrame and check if the duration is less than 90, if it is, add 1 to the counter, if it isn't, the counter should remain the same
for label, row in movies_in_1990.iterrows() :
    if row["duration"] < 90 and row["genre"] == "Action" :
        short_movie_count_2 = short_movie_count_2 + 1
    else:
        short_movie_count_2 = short_movie_count_2

# Visualize the duration column of your filtered data to see the distribution of movie durations
# See which bar is the highest and save the duration value, this doesn't need to be exact!
plt.hist(movies_in_1990["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()



