import os
import shutil  # this libraries help be you to be able to deal more with operating system and libraries.

# counting the files 
images, codes , videos , archives , docs , apps  = 0 , 0 , 0 , 0 , 0 , 0


# 1- select the place that i want to handle.
current_dir = os.path.dirname(os.path.realpath(__file__)) # to get the current file


# 2- creating a loop for each and ever file.
count = 0
for filename in os.listdir(current_dir):

# 3- finding the conditions of the files.
#     organizing images files into images folder
    if filename.endswith(("png" , "jpg", "gif", "bmp","jpeg","tiff","tif","webp","svg","raw","ico", "heic")):# make sure of parentheses.
        if not os.path.exists("Images"): # if there is no file called Images create it
            os.mkdir("Images")
        shutil.copy(filename, "Images")
        os.remove(filename)
        images += 1

    # organizing videos files into videos folder
    if filename.endswith(("mp4" , "avi", "mkv", "mov","wmv","flv","webm","3gp","mpeg","ogg")):
        if not os.path.exists("videos"):
            os.mkdir("Videos")
        shutil.copy(filename, "Videos")
        os.remove(filename)
        videos += 1

    # organizing docs files into docs folder
    if filename.endswith(("docx", "doc", "pdf", "txt", "rtf", "odt", "xlsx", "xls", "pptx", "ppt")):
        if not os.path.exists("docs"):
            os.mkdir("docs")
        shutil.copy(filename, "docs")
        os.remove(filename)
        docs += 1

    # organizing Apps files into Apps folder
    if filename.endswith(("exe")):
        if not os.path.exists("Apps"):
            os.mkdir("Apps")
        shutil.copy(filename, "Apps")
        os.remove(filename)
        apps += 1

    # organizing archives files into archives folder
    if filename.endswith(("zip", " rar", "tar")):
         if not os.path.exists("archives"):
            os.mkdir("archives")
         shutil.copy(filename, "archives")
         os.remove(filename)
         archives += 1

    # organizing codes files into codes folder
    if filename.endswith(("html", "py", "css","db")):
        if not os.path.exists("codes"):
            os.mkdir("codes")
        shutil.copy(filename, "codes")
        os.remove(filename)
        codes += 1


print(f"{images} images have been organized")
print(f"{videos} videos have been organized")
print(f"{archives} archives have been organized")
print(f"{docs} docs have been organized")
print(f"{apps} apps have been organized")
print(f"{codes} codes have been organized")
print("all files have been organized successfully")