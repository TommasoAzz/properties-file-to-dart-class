from string import Template
import sys
import os
import constant

# Gets the file name passed as argument to the script. Raises an exception if the argument is not given.
def get_file_name() -> str:
    if len(sys.argv) < 2:
        raise EnvironmentError("File name not inserted.")
    return sys.argv[1]

# Checks if the file passed as argument exists.
def check_file_existence(file_name: str) -> bool:
    return os.path.isfile(file_name)

# Returns information from the row (which should have the format of string_with_no_spaces=string_eventually_with_spaces)
def extract_information_from_row(row: str):
    if len(row.split("=")) != 2:
        print(f"Row with content:\n{row}\nis not in the specified format.")
        return constant.WRONG_INPUT,constant.WRONG_INPUT
    items = row.split("=")
    return items[0].replace(" ", "").strip(), items[1].strip()

# Given a file name (with single extension), a list of keys (ordered like in the file in which they came from), a list of values (ordered like in the file in which they came from),
# creates the content string to write to write to the output file later.
# Returns the class name (first argument) and the class content.
def create_class_content(file_name: str, keys: list, values: list):
    class_name = file_name[0:file_name.index(".")]
    class_name = class_name.replace("_","")
    class_name = class_name.replace("-","")

    # Class header
    template = Template("class $cn {\n")
    file_content = template.substitute(cn=class_name)

    # Class content
    for i in range(0, len(keys)):
        file_content += return_spaces(2)
        template = Template("static const String $key = \"$value\";\n")
        file_content += template.substitute(key=keys[i], value=values[i])
    
    # Class footer
    file_content += "}"

    return class_name, file_content


# Returns a string consisting in number spaces.
def return_spaces(number: int):
    spaces = ""

    for i in range(0, number):
        spaces += " "
    
    return spaces

# Writes the content into a file named file_name with extension .dart.
def write_content_to_file(file_name: str, content: str):
    template = Template("$fn.dart")
    new_file = open(template.substitute(fn=file_name), "w")
    new_file.write(content)
    new_file.close()

# Main function definition
def main():
    try:
        name = get_file_name()
        print(name)
        if not check_file_existence(name):
            raise FileNotFoundError(f"The file with name {name} was not found.")
        
        with open(name, 'r') as input_file:
            rows = input_file.readlines()
            class_constants_keys = []
            class_constants_values = []
            for row in rows:
                const_key, const_value = extract_information_from_row(row)
                class_constants_keys.append(const_key)
                class_constants_values.append(const_value)
            class_constants_keys = list(filter((constant.WRONG_INPUT).__ne__, class_constants_keys))
            class_constants_values = list(filter((constant.WRONG_INPUT).__ne__, class_constants_values))
            class_name, class_content = create_class_content(name, class_constants_keys, class_constants_values)
            
            write_content_to_file(class_name, class_content)
    except EnvironmentError:
        print("The file name was not inserted. The script cannot continue.")
    except FileNotFoundError:
        print("The file was not found.")

main()