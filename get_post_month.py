from read_data import fromJson


def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        int: the number of posts for the given month
    """
    m=0
    data=data["messages"]
    for i in data:
        if i["type"]=="message":
            x = i["date"]
            x=x[5:7]
            if int(x)==int(month):
                m+=1

    return m
path="data/result.json"
data=fromJson(path)
s=get_post_month(data, 10)
print(s)