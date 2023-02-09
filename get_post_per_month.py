from read_data import fromJson


def get_post_per_month(data:dict)->dict:
    """
    Return the number of posts for each month

    Args:
        data (dict): a dictionary of posts
        
    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    data= {9:30,10:334,11:292}
    return data
path="data/result.json"
data=fromJson(path)
print(get_post_per_month(data))
