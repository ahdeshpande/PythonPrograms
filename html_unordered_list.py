def string_list_to_html_ul(string_list):
    """
    Function that converts a string list to an HTML unordered list
    """

    # Create a html unordered list from the user input list.
    # Add the start tag of ul
    html_string = "<ul>\n"

    # Iterate through input list
    for user_input in string_list:
        html_string += "\t<li>" + user_input + "</li>\n"

    # Append the closing tag of ul
    html_string += "</ul>\n"

    return html_string


print("Welcome to string to HTML unordered list conversion!")

# This is a list to store the user inputs.
user_input_list = []

# Set an initial condition depending on if you want to accept input from user.
accept_input = True

print("Enter the string: [enter blank string when done]")
# Set up the while loop to accept.
while accept_input:
    str_input = input("> ")

    if str_input == "":
        accept_input = False
    else:
        # Check for special characters '<' '>'

        # If '<', change to &lt;
        str_input = str_input.replace('<', '&lt;')
        # If '>', change to &gt;
        str_input = str_input.replace('>', '&gt;')

        # If not converted like above, they can mess up the interpreter.

        # Once converted, append the string to the list.
        # Strip the whitespace at the beginning or at the end of the string.
        user_input_list.append(str_input.strip())

# Print the output
print("\nOutput:")
print(string_list_to_html_ul(user_input_list))
