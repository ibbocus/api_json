# What is JSON? Javascript Object Notation

## Syntax - JSON is s syntax for exchanging data

### Where and How? Between a browser and server.

### What type of data? 

Json is also used to parse the data from existing files or web browsers
- Only text - hence JSON is text written in JSON format
- the following list shows the the types of data json files can contain
``` bash
a String
a number
an object(json object)
an array
a boolean
null
```

- Where does this syntax derive from javascript?
- Data is in Name/value pairs:
``` bash
NAME    VALUE
{"name": "james"}
``` 

``` bash

import json

car_data = {"name": "tesla", "engine":"electric"} # creating a dictionary

print(car_data) # printing the dictionary

print(type(car_data)) # checking the type of the dictionary

car_data_json_string = json.dumps(car_data)
# json.dumps changes python dict to json str dumps = dump string

print(type((car_data_json_string)))

with open("new_json_file.json", "w") as jsonfile: # enter the name of the file, make it writable using "w"
    json.dump(car_data, jsonfile)
    # dump takes two arguments, the first is the dictionary the second is the file object to dump it to

# encoding and creating and writing into json file

with open("new_json_file.json") as jsonfile:
    # reading from the file we just created
    car = json.load(jsonfile)
    print(type(car_data)) # returns a dictionary, as only dumps converts to string whereas dump puts a json object somewhere
    print(car['name'])
    print(car['engine']) #since this is in the with open block, you know that this is coming from the new file
    
# this is in essence the encoding then decoding process

```"# api_json" 
