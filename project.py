import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Users\Ajay\OneDrive\Desktop\python full course\project\netflix_titles.csv"
)

# print(df.head())


    # cleaning data 
    
    
    df = df.dropna(subset=['type','release_year','rating','country','duration'])

type_count = df['type'].value_counts()   # counts movies and TV shows

plt.figure(figsize=(6,4))
plt.bar(type_count.index, type_count.values, color=['skyblue','orange'])
plt.title("Number of TV Shows and Movies on Netflix")
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('bar_chart_comparison_between_movies_tvshow.png')
plt.show()


# pie chart 
rating_count = df['rating'].value_counts()   

plt.figure(figsize=(8,6))
plt.pie(rating_count, labels= rating_count.index,autopct='%1.1f%%',)
plt.title("percentahe of content rating ")
plt.tight_layout()
plt.savefig('rating_pie.png')
plt.show()


# check
# duration_count = df['duration'].value_counts()
# plt.figure(figsize=(6,4))
# plt.hist(type_count.index, type_count.values, color=['skyblue','orange'])
# plt.title("Distrubution of movie ")
# plt.xlabel('Duration (minutes)')
# plt.ylabel('Numbers of movie')
# plt.tight_layout()
# plt.savefig('histogram_duration.png')
# plt.show()

movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace(' min','').astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'], bins=30, color='purple', edgecolor='black')
plt.title('Distribution of Movie Duration')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
plt.show()


release_counts = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(10,6))
plt.scatter(release_counts.index, release_counts.values, color='red')
plt.title('Release year vs number of shows')
plt.xlabel('Release year')
plt.ylabel('Number of shows')
plt.tight_layout()
plt.savefig('release_year_noshow.png')
plt.show()


country_count = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index , country_count.values , color = 'teal')
plt.title('Top 10 country by numbers of shows')
plt.xlabel('Numbers of shows ')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top_10_country.png')
plt.show()

content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# First subplot: Movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[0].set_title('Movies Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

# Second subplot: TV Shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange')
ax[1].set_title('TV Shows Released Per Year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of TV Shows')

fig.suptitle('Comparison of Movies and TV Shows Released Over Years')

plt.tight_layout()
plt.savefig('movies_tv_shows_comparison.png')
plt.show()
