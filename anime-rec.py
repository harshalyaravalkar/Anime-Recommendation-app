import requests
import pandas as pd
import random

# Function to get the user's preference for watching anime type (Movie, TV Series, or Random)
def get_watch_type():
    print("\nYou can't decide what anime to watch right now?! Let me help you")
    mort = input("\nDo you wanna watch Movie or Series?! \n => 1. Movie\n => 2. Series \n => 3. Random \n Your Response => ")

    if mort == "1":
        return "Movie", None  # Return Movie type with no specific movie if selected
    elif mort == "2":
        return "TV", None    # Return TV Series type with no specific series if selected
    elif mort == "3":
        return "NA", random.randint(1, 30)  # Return Random type with a random movie/series if selected
    else:
        print("Invalid response. Please choose 1, 2, or 3.")
        return get_watch_type()

# Function to get the user's preference for the number of episodes for TV Series
def get_watch_episodes(watch_type):
    if watch_type == "TV":
        return input("\nDo you want it to be like:\n 1. Short and Sweet \n 2. Watch 100s of Eps as The Plot thickens \n Your Response =>  ")
    else:
        return "3"  # Default value for Movie or Random type

# Function to get the user's mood or genre preference
def get_watch_genre():
    gen = input("\nWhat mood are you in today?! \n 1. Happy/Nice  \n 2. Sad/Down  \n 3. Super bored \n Your Response => ")
    
    if gen == "1":
        return "Sports,Drama,Slice of Life,Action,Fantasy"
    elif gen == "2":
        return "Romance,Comedy,Supernatural,Horror,Adventure"
    elif gen == "3":
        return "Suspense,Sci-Fi,Mystery"
    else:
        print("Invalid response. Please choose 1, 2, or 3.")
        return get_watch_genre()

# Function to get the user's preference for the number of anime results
def get_results_count(watch_type):
    if watch_type in ["Movie", "TV"]:
        n0 = input("\nNumber of results you want => ")
        return int(n0)
    else:
        return 10  # Default number of results for Random type to choose one random anime from

# Function to build the query string for the API call based on user preferences
def build_query_string(watch_type, genre, results_count):
    if watch_type in ["Movie", "TV"]:
        print("done")
        return {"page": "1", "size": results_count*2, "genres": genre, "types": watch_type}
    elif watch_type == "NA":
        return {"page": "1", "size": "30", "genres": genre}

# Function to fetch anime data from the API
def fetch_anime_data(url, headers, querystring):
    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data["data"])
    else:
        print("Error:", response.status_code)
        return None

# Main function to control the flow of the program
def main():
    url = "https://anime-db.p.rapidapi.com/anime"

    # Get user preferences
    watch_type, o = get_watch_type()
    watch_episodes = get_watch_episodes(watch_type)
    watch_genre = get_watch_genre()
    results_count = get_results_count(watch_type)
    query_string = build_query_string(watch_type, watch_genre, results_count)

    headers = {
        "X-RapidAPI-Key": "7bff1edab3msh0ffc6b5eaa67dcep16df9bjsn4a2242000637",
        "X-RapidAPI-Host": "anime-db.p.rapidapi.com"
    }

    # Fetch anime data based on user preferences
    anime_data = fetch_anime_data(url, headers, query_string)

    # Display results based on user preferences
    if anime_data is not None:
        if watch_episodes == "1":
            print(anime_data[["title", "ranking", "genres", "episodes", "status"]][(anime_data["episodes"] < 50) & (anime_data["episodes"] > 0)].iloc[:int(results_count), :],
                  end="\n")
        elif watch_episodes == "2":
            print(anime_data[["title", "ranking", "genres", "episodes", "status"]][anime_data["episodes"] > 50].iloc[:int(results_count), :],
                  end="\n")
        elif watch_episodes == "3" and watch_type == "NA":
            if o is not None:
                print(anime_data[["title", "ranking", "genres", "episodes", "status"]].iloc[[o]], end="\n\n")
        else:
            print(anime_data[["title", "ranking", "genres", "episodes", "status"]].iloc[:int(results_count), :], end="\n\n")



if __name__ == "__main__":
    main()
