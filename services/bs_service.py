from datetime import datetime

def detect_bs_norm(manufacturing_date: str):
    mfg_date = datetime.strptime(manufacturing_date, "%Y-%m-%d")

    if mfg_date >= datetime(2020, 4, 1):
        return "BS6"
    elif mfg_date >= datetime(2017, 4, 1):
        return "BS4"
    elif mfg_date >= datetime(2010, 4, 1):
        return "BS3"
    else:
        return "BS2"