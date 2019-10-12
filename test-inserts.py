import pymongo
from faker import Faker
import time

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

fake = Faker()

count = 0
total_records_to_write = 5000
total_run_time = 0
begin_time = time.time()
number_records = 0
records_per_second = 0

while count <= total_records_to_write :
    customer = {
        "first" : fake.first_name(),
        "last" : fake.last_name(),
        "job" : fake.job(),
        "address" : fake.address()
    }
    mycol.insert_one(customer)
    total_run_time = time.time() - begin_time
    records_per_second = count / (total_run_time)
    count = count+1

print(f'records_per_second {records_per_second} total_run_time {total_run_time}')

