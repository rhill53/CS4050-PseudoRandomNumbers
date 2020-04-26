"""
This module requires the installation of google_images_download
$ pip install google_images_download
Also it requires access to the internet, and subsequently google image search
"""

# importing google_images_download module
from google_images_download import google_images_download

# creating object
response = google_images_download.googleimagesdownload()


def download_images(query):
    # keywords is the search query
    # format is the image file format
    # limit is the number of images to be downloaded
    # print urs is to print the image file url
    # size is the image size which can
    # be specified manually ("large, medium, icon")
    # aspect ratio denotes the height width ratio
    # of images to download. ("tall, square, wide, panoramic")
    arguments = {"keywords": query,
                 "limit": 1,  # number of photos? Originally 4
                 "format": "jpg",
                 "single_image": True,
                 "no_directory": True,
                 "print_urls": True,
                 "size": "medium"}
    try:
        response.download(arguments)

        # Handling File NotFound Error
    except FileNotFoundError:
        arguments = {"keywords": query,
                     "limit": 1,
                     "format": "jpg",
                     "single_image": True,
                     "no_directory": True,
                     "print_urls": True,
                     "size": "medium"}

        # Providing arguments for the searched query
        try:
            # Downloading the photos based
            # on the given arguments
            response.download(arguments)
        except:
            pass
    return response


# # Driver Code
# for query in search_queries:
#     downloadimages(query)
#     print()
