# ----- TMDB -----#
import requests


API_KEY = "55a764184948db155b0284897955ac2f"
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NWE3NjQxODQ5NDhkYjE1NWIwMjg0ODk3OTU1YWMyZiIsInN1YiI6IjYyMjhlNDlkMTEzMGJkMDA0NWRmMDRiZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZR2zpBw6Vg-0b6wu2PSXiZ0Uosig1rsMNWzyDDU8zw0"
new_movie_title = "Matrix"

# response = requests.get("https://api.themoviedb.org/3/search/movie",
#                         params={"api_key": API_KEY, "query": new_movie_title})

# response.raise_for_status()
# data = response.json()
# movie_list = data["results"]

# for movie in movie_list:
#     print(movie["original_title"])

movie_id = 624860
api_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
response = requests.get(api_url)
data = response.json()
print(data)
