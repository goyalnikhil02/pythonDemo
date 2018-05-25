
import sys
import json
#import yaml



firstArg=sys.argv[1]
secondArg=sys.argv[2]
thirdArg=sys.argv[0]
#print ("Number of arguments", len(sys.argv), 'arguments.')
for arg in sys.argv :
    print(arg)

    
print(firstArg+secondArg)
"""
Example usage:
$ python 29_json_to_yaml.py 29_json_test.json
"""
'''
# load json data
json_data = json.loads(open(sys.argv[1]).read())
# convert unicode to string
converted_json_data = json.dumps(json_data)
# output yaml
#print(yaml.dump(yaml.load(converted_json_data), default_flow_style=False))

print("*******************8")

'''