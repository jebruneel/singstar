import openpyxl
import requests
import re
import urllib

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
         searchSongFromUSDB(artist, title)


def searchSongFromUSDB(artist, title):
    baseURL = "http://usdb.animux.de/index.php?link=byartist&select="
    searchstring = baseURL + artist[0]
    findsonglinkinwebpage(searchstring, title)


def findFirstYoutubeVidInURL(usdburl):
    # baseurl = "http://usdb.animux.de/index.php"
    # songURL = baseurl + usdburl

    # response = requests.get(songURL)   
    # if response.status_code == 200:
    #     # Get the response text
    #     response_text = response.text

    #     lines = response_text.splitlines()
        
    #     for i, line in enumerate(lines):
    #         print(line)
    print('ge moet hier nog zorgen dat je de eerste video download van op de songurl website -> maar de eerste video is vaak youtube.com/v/xxxxxxx , how to fix?')




def findsonglinkinwebpage(url, string_to_find):
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
        found = True
    
        # define the variable where the result will be stored
        result = ""
        
        # find the index of the "href='" substring in the line
        index = line.find("href='")
        if index != -1: # if the substring was found
          # add everything after the substring and before the next "'" character to the result
          result += line[index + 6 : line.find("'", index + 6)]
        
        # print the result

        findFirstYoutubeVidInURL(result)
    

    # If the string was not found in any of the lines
    if not found:
      print(f"Could not find '{string_to_find}' in the webpage at {url}")
    
  else:
    print(f"Could not access the webpage at {url}")


importExcelFile('sing.xlsx')