import re
import requests
import sys

pattern = r'<img .* src="([\w\d\s:/.-]+?)">'
regex = re.compile(pattern)


def Get_Images(URL):
    """
    A function that returns all image URLs found within a given website
    """

    print("\nAttempting to download images from the given URL.\n")
    r = requests.get(URL)

    if r.status_code != 200:
        print("Error retrieving the desired website. Aborting! Try again later.\n\n")
        print(r.status_code)
        sys.exit(1)
    elif r.status_code == 200:
        html = r.content

        All_Images = re.findall(regex, html)

        # You can either print the URLs found or return it as a list:
        print("\nPrinting all images found in the webpage:\n")
        for image in All_Images:
            print("Got Here")
            print(image)
        print("\n\n")

    return None


def main():
    args = sys.argv[1:]
    #
    # if not args:
    #     print("Usage: Get_Amazon_Images.py <Amazon_URL_to_download_from>")
    #     sys.exit(1)
    #
    # Amazon_URL = args[0]

    URL = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=imagikids"
    # extracted_data.append(Get_Images(URL))
    Get_Images(URL)
    print("here")

    return None


if __name__ == '__main__':
    main()
