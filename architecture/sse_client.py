import requests

def event_stream():
    url = "http://localhost:5000/stream"
    response = requests.get(url, stream=True)
    client = response.iter_lines()

    # Iterate over the response
    for line in client:
        if line:  # filter out keep-alive new lines
            print("Received: {0}".format(line.decode()))

if __name__ == "__main__":
    event_stream()
