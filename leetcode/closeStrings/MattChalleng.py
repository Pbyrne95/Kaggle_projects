msg = f"""
    ETEVHTWGSAHGWYVPNKQOEGWYVPNKPDEPHWAOVWPFWNHANEVW
    XAVOAEAJEUXTAOWBTEVHTWGSAHGWYVPNQAOQVGTYHAVAXETO
    ANFQEOIQPLANTEVHFYNSQVEBEOWSKNCKLOPEVTYJAUFWYNCO
    TWZESQEPERQSQOPEVYCEVHEGDEHEVHEYOPNQEEHWYFTKTEVH
    TWGSAHGWYVPNKQOWVAPDEPWVTKFWNHANOTEVHTWGSAHGWYVP
    NQAOPDANAENAWVTKPIWHWYFTKTEVHTWGSAHGWYVPNQAOQVPD
    AIWNTHWVAWBPDAUQOYLFASQOPEVIDEPQOPDAWPDANWVA
    """

def features_dict(msg):
    index = 0
    iter_dict = dict()
    for char in msg:
        if char not in iter_dict:
            iter_dict[char] =1
        else:
            iter_dict[char] +=1
    
    return iter_dict

print(len(msg))
print(features_dict(msg))