import json

print('Loading function')

INTENT_GET_INVENTORY = "getInventory"
INTENT_GET_SALES_ORDERS = "getSalesOrder"

ENTITY_PRODUCT = "product"
ENTITY_LOCATION = "location"
ENTITY_CUSTOMER = "customer"
ENTITY_SUPPLIER = "supplier"

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    # Simulator response:
    requestData = extract_request_data(event)
    res = get_body_response(requestData)
    response = {'result': res}
    return response

def extract_request_data(event):
    if 'body' in event and 'headers' in event:
        return json.loads(event['body'])
    else:
        return event
        
def get_body_response(body):
    print("Received body: " + json.dumps(body, indent=2))
    res = "I cannot understand your question. Please try again."
    intent = ""
    if 'intent' in body:
        intent = body['intent']
        if intent == INTENT_GET_INVENTORY:
            res = get_inventory_response(body)
    print('Intent is: '+intent)
    #print("Response = "+res)
    return res

def get_inventory_response(body):
    res = "I canot find any inventory data."
    if hasEntityValue(body, ENTITY_PRODUCT) and (not hasEntityValue(body, ENTITY_LOCATION)):
        product = body[ENTITY_PRODUCT]
        if product.lower() == 'xyz':
            res = "I cannot find any inventoy for ["+product+"]."
        else:
            res = "I found the following inventory data for product ["+product+"]: \n\r"
            res = res + " - at DC001: 123 units\n"
            res = res + " - at DC103: 234 units\n"
    elif (not hasEntityValue(body, ENTITY_PRODUCT)) and hasEntityValue(body, ENTITY_LOCATION):
        location = body[ENTITY_LOCATION]
        res = "I found the following inventory at location ["+location+"] \n\r"
        res = res + " - iPhone: 216 units \n"
        res = res + " - Xbox:   124 units \n"
        res = res + " - iPad:   17 units \n"
    elif hasEntityValue(body, ENTITY_PRODUCT) and hasEntityValue(body, ENTITY_LOCATION):
        location = body[ENTITY_LOCATION]
        product = body[ENTITY_PRODUCT]
        res = "I found 216 unit of ["+product+"] at ["+location+"]\n"
    return res
  
def hasEntityValue(body, entityName):
    ret = False
    if entityName in body:
        product = body[entityName]
        ret =  not isNoneOrEmpty(product)
    return ret
    
def isNoneOrEmpty(val):
    ret = False
    try:
        if val is None:
            ret = True
        elif val == "":
            ret = True
    # except NameError:
    except:
        ret = True
    else: 
        pass
    return ret