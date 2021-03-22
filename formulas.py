def map_splitter(upper_left, upper_right, lower_right):
    x_odd = []
    x_even = []

    current_point_x = upper_left[0]

    # upper_right = 1.0

    while current_point_x <= upper_right[0]:
        x_odd.append(current_point_x)
        current_point_x += (1.0/111.0 * 2.0)


    current_point_x = upper_left[0] + (1.0/111.0)

    while current_point_x <= upper_right[0]:
        x_even.append(current_point_x)
        current_point_x += (1.0/111.0 * 2.0)

    y_odd = []
    y_even = []

    current_point_y = upper_left[1]

    while current_point_y >= lower_right[1]:
        y_odd.append(current_point_y)
        current_point_y -= (1.0/111.0 * 2.0)

    current_point_y = upper_left[1] - (1.0/111.0)

    while current_point_y >= lower_right[1]:
        y_even.append(current_point_y)
        current_point_y -= (1.0/111.0 * 2.0)

    even_points = [[str(i), str(j)] for i in x_even for j in y_even]
    odd_points = [[str(f), str(k)] for f in x_odd for k in y_odd]
    output = even_points + odd_points

    return output

def bing_maps_query(center_point_long, center_point_lat, radius, entity_input, BING_MAPS_KEY, base_url):
    import requests

    sq_km = str(radius)
    entity_type = str(entity_input)
    bing_maps_key = BING_MAPS_KEY
    query_components = "EntityID,DisplayName,Phone,Latitude,Longitude"

    query = "spatialFilter=nearby(" + center_point_lat + "," + center_point_long + "," + sq_km + ")&$filter=EntityTypeID%20eq%20'" + entity_type +  "'&key=" + bing_maps_key + "&$format=json"

    URL = base_url + query

    r = requests.get(URL)
    # results = pd.DataFrame(r.json().get("d").get("results")) # Just save the raw JSONs
    results = r.json()

    return results