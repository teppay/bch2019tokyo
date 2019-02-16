import json

def get_stab():
    stab = json.dumps({
        "title50":[ "jounal50", "50"],
        "title40":[ "jounal40", "40"],
        "title30":[ "jounal30", "30"],
        "title20":[ "jounal20", "20"],
        "title10":[ "jounal10", "10"],
        "title0" :[ "jounal0",  "0" ]
    })
    return stab

if __name__ == '__main__':
    print(get_stab())
    print(type(get_stab()))