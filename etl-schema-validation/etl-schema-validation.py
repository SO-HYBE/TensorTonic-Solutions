def validate_records(records: list, schema: list) -> list:
    """
    Returns a list of result dictionaries.
    """
    # Write code here
    output = []
    for i, record in enumerate(records):
        is_valid = True
        errors = []
        result = {}
        for col in schema:
            if col["column"] not in record:
                is_valid = False
                errors.append(f"{col["column"]}: missing")
                continue
                
            if record[col["column"]] is None and col["nullable"] == False:
                is_valid = False
                errors.append(f"{col["column"]}: null")
                continue
            elif record[col["column"]] is None and col["nullable"] == True:
                continue
                
            if col["type"] == "float":
                if type(record[col["column"]]).__name__ not in ("int", "float"):      
                    is_valid = False
                    errors.append(f"{col["column"]}: expected {col["type"]}, got {type(record[col["column"]]).__name__}")
                    continue
            else:
                if type(record[col["column"]]).__name__ != col["type"]:        
                    is_valid = False
                    errors.append(f"{col["column"]}: expected {col["type"]}, got {type(record[col["column"]]).__name__}")
                    continue
            if "max" in col and "min" in col:
                if record[col["column"]] < col["min"] or record[col["column"]] > col["max"]:
                    errors.append(f"{col["column"]}: out of range")
                    continue
            elif "max" in col and "min" not in col:
                if record[col["column"]] > col["max"]:
                    errors.append(f"{col["column"]}: out of range")
                    continue
            elif "min" in col and "max" not in col:
                if record[col["column"]] < col["min"]:
                    errors.append(f"{col["column"]}: out of range")
                    continue   
                    
        is_valid = len(errors) == 0
        result["record_index"] = i
        result["is_valid"] = is_valid
        result["errors"] = errors
        output.append(result)
    return output