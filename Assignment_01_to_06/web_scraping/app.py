import requests
from bs4 import BeautifulSoup

# Function to get the profile image link of a GitHub user
def get_profile_image(username):
    url = f"https://github.com/{username}"

    # Make an HTTP request to get the HTML content of the page
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the image tag for the profile picture
        profile_image_tag = soup.find('img', {'alt': f"@{username}'s avatar"})

        # Check if the image tag was found
        if profile_image_tag:
            # Get the 'src' attribute which contains the image URL
            profile_image_url = profile_image_tag['src']
            return profile_image_url
        else:
            return "Profile image not found."
    else:
        return "User not found or invalid URL."

# Main function
def main():
    # Ask the user for a GitHub username
    username = input("Enter the GitHub username: ")

    # Get the profile image URL
    profile_image_url = get_profile_image(username)

    # Display the profile image URL
    print(f"Profile Image URL: {profile_image_url}")

if __name__ == "__main__":
    main()
