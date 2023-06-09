
# # # import OS module
# # import os
 
# # # Get the list of all files and directories
# source_folder = r"C:\Users\user\OneDrive\Documents\GitHub\File-Organizer\Organize Files" + '\\'
music_folder = r"C:\Users\user\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Music" + '\\'
pictures_folder = r"C:\Users\user\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Pictures" + '\\'
videos_folder = r"C:\Users\user\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Videos" + '\\'

# # dir_list = os.listdir(path)
 
# # print("Files and directories in '", path, "' :")
 
# # # prints all files
# # print(dir_list)



# # import OS
# import os
# import shutil
# # os.mkdir(r"C:\Users\user\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Pictures", mode = 0o777,  dir_fd = None)
# # os.mkdir(r"C:\Users\user\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Videos", mode = 0o777,  dir_fd = None)
# # os.mkdir(r"C:\Users\user\OneDrive\Documents\GitHub\File-Organizer\Organize Files\Music", mode = 0o777,  dir_fd = None)
 
# # os.walk(path, topdown=True, onerror=None, followlinks=False)
#         # shutil.move(files, r"C:\Users\user\OneDrive\Documents\GitHub\File-Organizer")
# for path, dir, files in os.walk(source_folder):
#     if files:
#         for file in files:
#             if file.endswith((".mp3",  ".wav", ".aac", )):
#                 if not os.path.isfile(music_folder + file):
#                     os.rename(path + '\\' + file, music_folder + file)
#             if file.endswith((".mp4", ".mov", ".wmv", ".avi", ".avchd", ".flv", ".f4v", ".swf", ".mkv", ".webm")):
#                 if not os.path.isfile(videos_folder + file):
#                     os.rename(path + '\\' + file, videos_folder + file)
#             if file.endswith((".jpeg", ".jpg", ".png", ".gif", ".tiff", ".bmp", ".raw")):
#                 if not os.path.isfile(pictures_folder + file):
#                     os.rename(path + '\\' + file, pictures_folder + file)
# #print hello world

import sys
import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog

class FileOrganizerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Organizer")
        self.layout = QVBoxLayout()
        self.label = QLabel("Select Source Folder")
        self.button = QPushButton("Organize Files")
          # self.button = QPushButton("Organize Files")
        # self.button.setStyleSheet("background-color:rgb(0,0,0)"
        #                           "border-radius:10px;"
        #                           "background-color:rgb(255,36,0);"
        #                           "font: 100 10pt Nirmala UI;")
        # self.button.setStyleSheet("background-color:rgb(0,0,0)")
        # self.button.setStyleSheet("border-radius:10px;")
        # self.button.setStyleSheet("font: 100 10pt Nirmala UI;")
        self.button.setStyleSheet("border :3px solid blue;"
                                   "border-top-left-radius :35px;"
                                   " border-top-right-radius : 20px; "
                                   "border-bottom-left-radius : 50px; "
                                   "border-bottom-right-radius : 10px")
        self.button.resize(100, 100)
        self.button.clicked.connect(self.organize_files)
       
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
    def organize_files(self):
        source_folder = QFileDialog.getExistingDirectory(self, "Select Source Folder")
        if source_folder:
            target_folder = os.path.join(source_folder, "Organized Files")
            os.makedirs(target_folder, exist_ok=True)
            music_folder = os.path.join(target_folder, "Music")
            pictures_folder = os.path.join(target_folder, "Pictures")
            videos_folder = os.path.join(target_folder, "Videos")
            os.makedirs(music_folder, exist_ok=True)
            os.makedirs(pictures_folder, exist_ok=True)
            os.makedirs(videos_folder, exist_ok=True)

            for path, dir, files in os.walk(source_folder):
                if files:
                    for file in files:
                        if file.endswith((".mp3",  ".wav", ".aac")):
                            if not os.path.isfile(os.path.join(music_folder, file)):
                                os.rename(os.path.join(path, file), os.path.join(music_folder, file))
                        elif file.endswith((".jpeg", ".jpg", ".png", ".gif", ".tiff", ".bmp", ".raw")):
                            if not os.path.isfile(os.path.join(pictures_folder, file)):
                                os.rename(os.path.join(path, file), os.path.join(pictures_folder, file))
                        elif file.endswith((".mp4", ".mov", ".wmv", ".avi", ".avchd", ".flv", ".f4v", ".swf", ".mkv", ".webm")):
                            if not os.path.isfile(os.path.join(videos_folder, file)):
                                os.rename(os.path.join(path, file), os.path.join(videos_folder, file))

            self.label.setText("Files organized successfully!")

                
                


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileOrganizerApp()
    window.show()
    sys.exit(app.exec_())