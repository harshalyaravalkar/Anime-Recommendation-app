# Anime Recommendation Console App

## Overview
This repository contains a simple console application for recommending anime based on user preferences. The application interacts with the "Anime Database" API to fetch relevant data and presents recommendations to the user.

## Features
- **Watch Type Selection:** Choose between watching a movie, or TV series, or get a random recommendation.
- **Episode Preferences:** Specify preferences for the number of episodes for TV series.
- **Genre Selection:** Select the preferred mood or genre for anime recommendations.
- **Results Count:** Choose the number of anime results you want to see.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/anime-recommendation.git
2. Navigate to the project directory:

   ```bash
   cd anime-recommendation
3. Run the main script:

   ```bash
   python anime-rec.py

## Dependancies  
- [Requests](https://docs.python-requests.org/en/latest/)
- [Pandas](https://pandas.pydata.org/)
- [Random](https://docs.python.org/3/library/random.html)

## Configuration

Ensure that you have a valid API key for the "Anime Database" API. You can obtain the key by signing up on the [RapidAPI website](https://rapidapi.com/hub).

Replace the placeholder 'X-RapidAPI-Key' in the 'headers' dictionary in 'anime-rec.py' with your actual API key.

```python
headers = {
    "X-RapidAPI-Key": "your-api-key-here",
    "X-RapidAPI-Host": "anime-db.p.rapidapi.com"
}
