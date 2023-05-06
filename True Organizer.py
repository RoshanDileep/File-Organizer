
# # import OS module
# import os
 
# # Get the list of all files and directories
source_folder = r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer\Organize Files" + '\\'
music_folder = r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Music" + '\\'
pictures_folder = r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Pictures" + '\\'
videos_folder = r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Videos" + '\\'

# dir_list = os.listdir(path)
 
# print("Files and directories in '", path, "' :")
 
# # prints all files
# print(dir_list)



# import OS
import os
import shutil
# os.mkdir(r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Pictures", mode = 0o777,  dir_fd = None)
# os.mkdir(r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Videos", mode = 0o777,  dir_fd = None)
# os.mkdir(r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Music", mode = 0o777,  dir_fd = None)
 
# os.walk(path, topdown=True, onerror=None, followlinks=False)
        # shutil.move(files, r"C:\Users\rosha\OneDrive\Documents\GitHub\File-Organizer")
for path, dir, files in os.walk(source_folder):
    if files:
        for file in files:
            if file.endswith((".mp3",  ".wav", ".aac", )):
                if not os.path.isfile(music_folder + file):
                    os.rename(path + '\\' + file, music_folder + file)
            if file.endswith((".mp4", ".mov", ".wmv", ".avi", ".avchd", ".flv", ".f4v", ".swf", ".mkv", ".webm")):
                if not os.path.isfile(videos_folder + file):
                    os.rename(path + '\\' + file, videos_folder + file)
            if file.endswith((".jpeg", ".jpg", ".png", ".gif", ".tiff", ".bmp", ".raw")):
                if not os.path.isfile(pictures_folder + file):
                    os.rename(path + '\\' + file, pictures_folder + file)
            