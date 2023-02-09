from read_data import fromJson

def get_number_of_posts(data:dict)->int:
    """
    Return the number of posts for a given dictionary

    Args:
        data (dict): a dictionary of posts

    Returns: 
        int: the number of posts for the given dictionary
    """
    count=0
    data=data["messages"]
    for i in data:
        if i["type"]=="message":
            count+=1    
    return count

path="data/result.json"
data = fromJson(path)
print(get_number_of_posts(data))