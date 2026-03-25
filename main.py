## Function for user settings
def add_setting(setting_dict, setting_tuple):
    
    ## Convert the key and value to lowercase
    key, value = setting_tuple
    key = str(key).lower()
    value = str(value).lower() 
    
    ## Check if the key settings exists
    if key in setting_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    ## Check if the key doesn't exists
    if key not in setting_dict:
        setting_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
    
    return key,value


## Function for updating user settings
def update_setting(update_setting_dict, update_setting_tuple):

    ## Convert the key and value to lowercase
    key, value = update_setting_tuple
    update_setting_key = str(key).lower()
    update_setting_value = str(value).lower()
    
    ## Check if the key already exists, and update its value
    if update_setting_key in update_setting_dict:
        update_setting_dict[update_setting_key] = update_setting_value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    ## Check if the key doesn't exists
    if update_setting_key not in update_setting_dict:
        return f"Setting '{update_setting_key}' does not exist! Cannot update a non-existing setting."
    
    return update_setting_key, update_setting_value

## Function for deleteting user settings
def delete_setting(delete_setting_dict, delete_setting_tuple):
    
    ## Convert the key and value to lowercase
    key = delete_setting_tuple
    delete_setting_key = str(key).lower()
    
    ## Check if the key already exists, and delete it 
    if delete_setting_key in delete_setting_dict: 
        del delete_setting_dict[delete_setting_key]
        return f"Setting {delete_setting_key} deleted successfully!"
    else:
        ## Check if the key doesn't exists
        return "Setting not found!"
    
    return delete_setting_key

## Function for viewing user settings
def view_settings(view_settings_dict):
    
    ## Return No settings available. if the given dictionary of settings is empty.
    if not view_settings_dict:
        return "No settings available."

    ## If the dictionary contains any settings, return a string displaying the settings. 
    if view_settings_dict:
        current_settings = "Current User Settings:\n"
        for key, value in view_settings_dict.items():
            current_settings += f"{key}: {value}\n".capitalize()
        return current_settings


## Test dictionary
## Update testing logic with multiple scenarios
test_settings = {
    "theme": "dark",
    "volume": "high",
    "notifications": "enabled"
}


print(add_setting(test_settings, ("THEME", "dark")))
print(update_setting(test_settings, ("volume", "high")))
print(delete_setting(test_settings, "volume"))
print(view_settings(test_settings))