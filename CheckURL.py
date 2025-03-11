import requests


def image_exists( image_url, timeout = 5 ):
  """
  Checks if an image exists at the given URL.

  Args:
      image_url (str): The URL of the image.

  Returns:
      bool: True if the image exists, False otherwise.
  """
  try:
    response = requests.head( image_url, allow_redirects = True, timeout = timeout )  # using HEAD to only get headers, not full content.
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

    # Check if the content-type is an image. There are many image types, this checks for a few common ones.
    content_type = response.headers.get( "content-type" )
    if content_type and content_type.startswith( "image/" ):
      return True
    return False

  except requests.exceptions.RequestException:
    return False


if __name__ == "__main__":
  # Example URL: https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png
  url_prefix = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp"
  url_suffix = ".jpg"
  url_list = []
  start_range = 00
  end_range = 18
  width = 1  # padding for the number in the URL

  print( f"Building URLs from {start_range} to {end_range}" )
  for i in range( start_range, end_range ):
    url_list.append( url_prefix + str( f"{i:0{width}}" ) + url_suffix )

  print( f"Checking on {end_range - start_range} URLs..." )
  for url in url_list:
    try:
      if image_exists( url, 10 ):
        print( f"Valid: {url}" )
      else:
        print( "No response" )
    except KeyboardInterrupt:
      print( "Exiting..." )
