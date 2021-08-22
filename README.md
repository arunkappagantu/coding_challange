# LFS_coding_challange

# Considerations:

- Stock price is always in whole dollar amount (no cents)
- The index start at 0 ie. the first entry in the text file is index 0

# Implementation:

- Created a docker image and have pushed it to Docker Hub, can be pulled using the below command
  docker pull arunkappagantu/arun_public_repo
- Read and load the daily stock price (into list) from text (.txt) file baked in the image

**    Note: Have also provided a solution (commented code) to load file dynamically from S3 using Boto3 ** 

- Used nested for loop to and comparing maximum difference between and purchase and subsequent price raise sale is caluculated
    - In the example used although the min price of day was $1 (index 52), if the stock was purchased at this time the maximum profit that could have been made    is $89 by selling the stock at $90 (index 73). Instead the most profitable transction of the day would be purchsing the stock at $3 (index 7)  and selling it at $98 (index 49)

# Tests/Validations:

- Have put checks in the code to ensure that the function exists in any of the following scenarios
    - If the file consists of non-integer value or special character or blank entry
    - The file should contain atleast 2 records (comma (,) seperated) to ensure comparision
    - Ensure that the sale only can occour after purchase (ie the index of sale is always greater than purchase)
    - Ensure that the sale price is always greater than the purchase price
