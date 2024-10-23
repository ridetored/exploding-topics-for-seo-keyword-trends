import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import time

# Function to fetch trending topics from a website (e.g., Google Trends or another website)
def fetch_trending_topics(url):
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        # Scrape relevant data (this would depend on the site's structure)
        # For demo purposes, let's assume we're grabbing topics from h2 tags
        topics = []
        for h2_tag in soup.find_all('h2'):
            topic = h2_tag.get_text()
            topics.append(topic)

        return topics

    except Exception as e:
        print(f"Error fetching topics: {e}")
        return []

# Function to analyze and plot keyword search patterns over time
def track_keyword_trend(keyword, timeframe="2023-01-01:2023-12-31"):
    # Placeholder function to simulate search trend analysis
    # In a real-world scenario, you can use the Google Trends API or another data source
    # Here, we generate some dummy data to visualize

    # Generate dates and random popularity scores for demonstration
    dates = pd.date_range(start="2023-01-01", periods=365, freq='D')
    popularity = pd.Series([50 + 20 * abs(time.time() % 5) for _ in range(365)], index=dates)

    # Plot the trend
    plt.figure(figsize=(10, 6))
    plt.plot(popularity.index, popularity.values, label=keyword)
    plt.title(f"Search Trend for '{keyword}' over Time")
    plt.xlabel("Date")
    plt.ylabel("Search Popularity")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function to run the script
def main():
    # Example of fetching topics from a demo URL
    url = "https://example.com/trending-topics"  # Replace with actual URL
    trending_topics = fetch_trending_topics(url)

    if trending_topics:
        print("Trending Topics:")
        for idx, topic in enumerate(trending_topics):
            print(f"{idx+1}. {topic}")

        # Let's track the trend of the first topic (as a demo)
        first_topic = trending_topics[0]
        track_keyword_trend(first_topic)

    else:
        print("No trending topics found.")

if __name__ == "__main__":
    main()
