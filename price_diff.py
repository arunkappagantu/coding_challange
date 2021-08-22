import sys

price_list = []
max_price_differnce = -1 
file = './stock_price.txt'
    
# Loading Data for text file into price list
fi = open(file, 'r') 
content = fi.readlines()

for line in content:
    line_list = line.split(',')
    for i in line_list:
        try:
            price_list.append(int(i))
        except Exception as err:
            print("Format error in file. There may be an non-integer value, special character or blank entry")
            sys.exit(1)

### Alternate solution to fetch and load data dynamically from text file in S3 is using boto3 (mentioned below)

#import boto3
#s3 = boto3.client('s3', aws_access_key_id=<Key_ID>, aws_secret_access_key=<Key>)
#s3.download_file(<Bucket>, <key>, '/tmp/stock_price.txt')

# Ensuring atleast 2 records for comparision  
    if (len(price_list)<2):
        print("Less than two records in file cannot compare")
        sys.exit(1)

# Iterate every index through all the subsequent indexes
for pur in range(len(price_list)):
    current_index = pur+1  ### Ensuing that value is only compared with subsequent values in the list
    for sal in price_list[current_index:]:
        price_differnce = sal - price_list[pur]
        
### Capturing maximum price differnce
        if price_differnce > max_price_differnce:
            purchase_index, purchase_price, sale_index, sale_price, max_price_differnce = pur, price_list[pur], current_index, sal, price_differnce
        current_index += 1
    
# Validating that function is performing as expected
    if(purchase_index>sale_index or purchase_price>sale_price):
        print("Function error in comparision. Sale should happen after purchase and sale price should always be greater than purchase price to make profit.")
        sys.exit(1)
        
print("Maximum profit of ${} would have been made purchsing the stock at ${} and selling it at ${}".format(max_price_differnce, purchase_price, sale_price))
print("Index of the purchase is {} and index of sale is {}".format(purchase_index, sale_index))