import json

with open("data/sample.json") as file:
    lines_read = 0
    uk_tweets = 0
    while (True):
        lines_read += 1

        # Read one line at a time for efficiency
        json_line = file.readline()

        # Check not end of line
        if not json_line:
            break

        # Parse as JSON object
        json_obj = json.loads(json_line)
        tweet_id = json_obj["tweet_id"]
        user_location = json_obj["user_location"]

        if "country_code" in user_location:
            country_code = user_location["country_code"]
        else:
            country_code = "unknown"

        print("Tweet ID: {}".format(tweet_id))
        print("Country Code: {}".format(country_code))

        # Filter based on location
        if country_code == "gb":
            uk_tweets += 1

        # Retrieve tweet


    print("Read {} Lines".format(lines_read))
    print("Read {} UK Tweet Lines".format(uk_tweets))

