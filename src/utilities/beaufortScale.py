def wind_beaufort_scale(value):
    """Convert wind speed value to Beaufort Scale (0-12)

    The Beaufort wind force scale is an empirical measure that
    relates wind speed to observed conditions at sea or on land.

    Parameters:
    value: wind speed value to convert in m/s

    Returns:
    a string containing the Beaufort Description

    """

    scale = {
        '0': 'Calm',
        '1': 'Light air',
        '2': 'Light breeze',
        '3': ' Gentle breeze',
        '4': 'Moderate breeze',
        '5': 'Fresh breeze',
        '6': 'Strong breeze',
        '7': 'High wind, moderate gale, near gale',
        '8': 'Gale, fresh gale',
        '9': 'Strong gale',
        '10': 'Storm, whole gale',
        '11': 'Violent storm',
        '12': 'Hurricane'
    }
    if value < 0.0:
        return 'Negative speed are not valid'
    elif value < 0.5:
        return scale['0']
    elif value <= 1.5:
        return scale['1']
    elif value <= 3.4:
        return scale['2']
    elif value <= 5.4:
        return scale['3']
    elif value <= 7.9:
        return scale['4']
    elif value <= 10.7:
        return scale['5']
    elif value <= 13.8:
        return scale['6']
    elif value <= 17.1:
        return scale['7']
    elif value <= 20.7:
        return scale['8']
    elif value <= 24.4:
        return scale['9']
    elif value <= 28.4:
        return scale['10']
    elif value <= 32.6:
        return scale['11']
    else:
        return scale['12']
