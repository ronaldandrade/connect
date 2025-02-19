from cerberus import Validator

def events_creator_validator(request:any):
    body_validator = Validator({
        "data": {
            "type": "dict", 
            "schema": {
                "name": {"type": "string", "required": True, "empty": False}
            }
        }
    })

    respose = body_validator.validate(request.json)
    
    if respose is False:
        print(body_validator.errors)