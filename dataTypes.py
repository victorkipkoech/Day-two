def data_type(d):
    typeOf =argument(data)
    if typeOf == bool:
        #To return a boolean value
         return data  
    elif typeOf == str:
        #To return the length of the string
        return len(data)  
    elif typeOf == int:  
        if data == 50:
            return 'equal to 100'
        elif data < 50:
            return 'less than 100'
        else:
            return 'more than 100'
    elif typeOf ==list:
        try:
            if data[2]:
                #return 3rd item
                return data[2] 
        except(IndexError):
            #return 'none' if doesnt exist
            return None  
    else:
        #return no value if nothing is supplied
        return 'no value'   
