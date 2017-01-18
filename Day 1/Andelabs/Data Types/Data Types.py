def data_type(d):
    d_type = type(d)
    if d_type == str:
        return len(d)
    elif d_type == bool:
        return d
    elif d_type ==int:
        if d ==100:
            return "equal to 100"
        elif d <100:
            return "less than 100"

        else:
            return "more than 100"

    elif d_type == list:
        try:
            if d[2]:
                return d[2]
        except (IndexError):
                return None
    else:
        return "no value"
        
