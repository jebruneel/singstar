import openpyxl
import requests


def importExcelFile(file):
  # Open the Excel file
  wb = openpyxl.load_workbook(file)
  
  # Select the active sheet
  sheet = wb.active
  count = 1
  # Iterate over all cells in the sheet
  for row in sheet.iter_rows():

     artist = row[0].value  # First column
     title = row[1].value  # Second column
     # Do something with the cell values
     if artist != None : 
         searchYoutubeSongFromUSDB(artist, title)


def searchYoutubeSongFromUSDB(artist, title):
    baseURL = "http://usdb.animux.de/index.php?link=byartist&select="

    searchstring = baseURL + artist[0]

    print('searching song ' + title + ' by ' + artist + ' in website ' + searchstring )
    find_string_in_webpage(searchstring, title)

def findFirstYoutubeVidInURL(usdburl):
    baseurl = "http://usdb.animux.de/index.php"
    songURL = baseurl + usdburl

    #find first youtube video posted on that song page




def find_string_in_webpage(url, string_to_find):
  # Make a GET request to the given URL
  response = requests.get(url)

  # If the request is successful
  if response.status_code == 200:
    # Get the response text
    response_text = response.text

    # Split the response text into lines
    lines = response_text.splitlines()

    # Flag to keep track of whether the string was found or not
    found = False

    # Iterate over the lines
    for i, line in enumerate(lines):
      line = line.lower()
      string_to_find = string_to_find.lower()
      # Check if the string is in the line
      if string_to_find in line:
        # If it is, print the line number and the line
        print(f"Found '{string_to_find}' on line {i+1}: {line}")
        found = True
    
        # define the variable where the result will be stored
        result = ""
        
        # find the index of the "href='" substring in the line
        index = line.find("href='")
        if index != -1: # if the substring was found
          # add everything after the substring and before the next "'" character to the result
          result += line[index + 6 : line.find("'", index + 6)]
        
        # print the result

        print(result)
        findFirstYoutubeVidInURL(result)
    

    # If the string was not found in any of the lines
    if not found:
      print(f"Could not find '{string_to_find}' in the webpage at {url}")
    
  else:
    print(f"Could not access the webpage at {url}")


importExcelFile('sing.xlsx')