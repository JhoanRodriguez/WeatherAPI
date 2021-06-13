def degToCompass(deg):
    """Func for the covertion of degrees into a directional compass

    Args:
        deg ([float]): degree to be convert to a directional compass

    Returns:
        [string]: directional compass
    """
    val = int((deg/22.5)+.5)
    arr = ["North", "North-northeast", "Northeast", "East-northeast", "East",
           "East-southeast", "Southeast", "South-southeast",
           "South", "South-southwest", "Southwest", "West-southwest", "West",
           "West-northwest", "Northwest", "North-northwest"]
    return arr[(val % 16)]
