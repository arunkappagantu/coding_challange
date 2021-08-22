# LFS_coding_challange

# Assumptions:

- Stock price is always in whole dollar amount (no cents)

# Implementation:

- Created a docker image and have pushed it to Docker Hub, can be pulled using the below command
  docker pull arunkappagantu/arun_public_repo
- Read and load the daily stock price (into list) from text (.txt) file baked in the image
**    Note: Have also provided a solution (commented code) to load file dynamically from S3 using Boto3 (needs file in a S3 Bucker and AWS creds to access it)** 
- Used nested for loop to and comparing maximum difference between and purchase and subsequent price raise sale is caluculated

# Tests/Validations:

- Have put checks in the code to ensure that the function exists in any of the following scenarios
    - If the file consists of non-integer value or special character or blank entry
    - The file should contain atleast 2 records (comma (,) seperated) to ensure comparision
    - Ensure that the sale only can occour after purchase (ie the index of sale is always greater than purchase)
    - Ensure that the sale price is always greater than the purchase price
