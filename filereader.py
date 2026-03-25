#Names
import json
def read_string_lists_from_file(filename):
    with open(filename, "r") as f:
        result = []
        for line in f:
            line = line.strip()
            if line:
                try:
                    data = json.loads(line)
                    result.append(data)
                except json.JSONDecodeError:
                    # handle or skip bad lines
                    pass
        return result


# Example usage
#lists = read_string_lists_from_file("data.txt")
#print(lists)

def write_string_lists_to_file(data, filename):
#    import json
    with open(filename, "w") as f:
        for pair in data:
            json.dump(pair, f)
            f.write("\n")


#POly Ordinates
def parse_two_number_lists_line(line):
    line = line.strip()
    if not (line.startswith("[[") and line.endswith("]]")):
        return []

    inner = line[2:-2]  # remove outer [[ and ]]
    
    if "], [" not in inner:
        return []

    first_part, second_part = inner.split("], [")

    try:
        list1 = [float(x.strip()) for x in first_part.split(",") if x.strip()]
        list2 = [float(x.strip()) for x in second_part.split(",") if x.strip()]
        return [list1, list2]
    except ValueError:
        return []


def read_two_number_lists_per_line(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            parsed = parse_two_number_lists_line(line)
            if parsed:
                result.append(parsed)
    return result


def write_two_number_lists_per_line(data, filename):
    with open(filename, 'w') as file:
        for pair in data:
            # Each pair must be a list of two sublists
            if (isinstance(pair, list) and len(pair) == 2 and
                all(isinstance(sublist, list) for sublist in pair)):

                # Format each sublist as [num1, num2, ...]
                formatted_pair = "[{}], [{}]".format(
                    ", ".join(str(float(num)) for num in pair[0]),
                    ", ".join(str(float(num)) for num in pair[1])
                )
                file.write(f"[{formatted_pair}]\n")

#Distances

def read_floats_from_file(filename):
    with open(filename, 'r') as file:
        line = file.readline().strip()
        if not line:
            return []
        # Accepts both comma and space separation
        parts = [part.strip() for part in line.replace(',', ' ').split()]
        try:
            return [float(num) for num in parts if num]
        except ValueError:
            return []  # return empty if any item fails

def write_floats_to_file(floats, filename):
    with open(filename, 'w') as file:
        line = " ".join(f"{num}" for num in floats)
        file.write(line + "\n")

def store_location_to_file(location, filename):
    """
    Appends a location string to a text file.
    
    Parameters:
    - location (str): The location to store.
    - filename (str): The name of the text file.
    """
    if isinstance(location, str):
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(location.strip() + '\n')
    else:
        print("Invalid input: location must be a string.")


def retrieve_locations_from_file(filename):
    """
    Reads all locations from a text file.
    
    Parameters:
    - filename (str): The name of the text file.
    
    Returns:
    - list: A list of location strings.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("File not found. Returning an empty list.")
        return []


def store_locationlist_to_file(location_list, filename):
    """
    Appends a list (e.g., [x, y, z]) to a text file as a JSON string.
    
    Parameters:
    - location_list (list): The list to store.
    - filename (str): The name of the text file.
    """
    if isinstance(location_list, list):
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(json.dumps(location_list) + '\n')
    else:
        print("Invalid input: location must be a list.")


def retrieve_locationslist_from_file(filename):
    """
    Reads all list entries from a text file, where each line is a JSON list.
    
    Parameters:
    - filename (str): The name of the text file.
    
    Returns:
    - list of lists: All retrieved location lists.
    """
    locations = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    locations.append(json.loads(line.strip()))
                except json.JSONDecodeError:
                    print("Skipping invalid line:", line)
    except FileNotFoundError:
        print("File not found. Returning an empty list.")
    return locations
