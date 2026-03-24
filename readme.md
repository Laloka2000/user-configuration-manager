# User Configurator Manager

A lightweight Python utility designed to manage application settings using a dictionary-based storage. This project ensures consistency by forcing all keys and values to lowercase and provides informative feedback for every operation.

## Features

- **Case-Insensitive Handling**: Automatically converts all settings to lowercase to avoid duplication (e.g., `Color` and `color` are treated as the same key).
- **Validation**: Prevents overwriting existing settings unless explicitly updated.
- **Formatted Feedback**: Returns user-friendly success and error messages for every action.

## Functionalities

The manager consists of four core functions:

1.  **`add_setting(settings_dict, setting_tuple)`**
    - Adds a new key-value pair if the key does not exist.
    - Returns: Confirmation message or an error if the key is already present.
2.  **`update_setting(update_setting_dict, update_setting_tuple)`**
    - Updates the value of an existing key.
    - Returns: Confirmation message or an error if the key is missing.
3.  **`delete_setting(delete_setting_dict, delete_setting_tuple)`**
    - Removes a setting from the dictionary.
    - Returns: Success message or a "not found" notice.
4.  **`view_settings(view_settings_dict, view_settings_tuple)`**
    - Displays all current settings in a readable format.

---

## Installation & Usage

Simply include the functions in your Python script. No external dependencies are required.

### Example Code

```python
# Initial testing dictionary
user_config = {
    "theme": "dark",
    "language": "en"
}

# Adding a new setting
result = add_setting(user_config, ("FontSize", "LARGE"))
print(result) 
# Output: Setting 'fontsize' added with value 'large' successfully!

# Attempting to add an existing key
result = add_setting(user_config, ("THEME", "light"))
print(result) 
# Output: Setting 'theme' already exists! Cannot add a new setting with this name.