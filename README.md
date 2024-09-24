# Alteryx-File-Conversion

   ___   __ _______________  ___  __  _________  _  ___   _________  ____________  _  ______
  / _ | / //_  __/ __/ _ \ \/ / |/_/ / ___/ __ \/ |/ / | / / __/ _ \/ __/  _/ __ \/ |/ / __/
 / __ |/ /__/ / / _// , _/\  />  <  / /__/ /_/ /    /| |/ / _// , _/\ \_/ // /_/ /    /\ \  
/_/ |_/____/_/ /___/_/|_| /_/_/|_|  \___/\____/_/|_/ |___/___/_/|_/___/___/\____/_/|_/___/  

   ___         ______                 ___             __
  / _ )__ __  / __/ /____ _  _____   / _ \___ ___ ___/ /
 / _  / // / _\ \/ __/ -_) |/ / -_) / , _/ -_) -_) _  / 
/____/\_, / /___/\__/\__/|___/\__/ /_/|_|\__/\__/\_,_/  
     /___/                                            
   __ __    __              _     __     ____      ___                         ____        
  / // /__ / /_ _  ___ ____(_)___/ /    / __/___  / _ \___ ___ _____  ___     /  _/__  ____
 / _  / -_) /  ' \/ -_) __/ / __/ _ \   > _/_ _/ / ___/ _ `/ // / _ \/ -_)   _/ // _ \/ __/
/_//_/\__/_/_/_/_/\__/_/ /_/\__/_//_/  |_____/  /_/   \_,_/\_, /_//_/\__( ) /___/_//_/\__/ 
                                                          /___/         |/                 

I could not find a tool to convert the the .yxzp, .yxmd and .yxmc files for Alteryx, so I wrote this Python script that converts them to JSON

Directions: add Alteryx files into the folder that contains the Python script and run the following command. Remember to change "path/to/directory" with the actual path of where your files are located. Must be in the same folder as the Python script.

python batch_convert_alteryx_files_to_json.py "path/to/directory" "path/to/output/directory"

.
.
.
