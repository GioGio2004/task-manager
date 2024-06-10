# from speech_to_text import text, subject

import os

class Readeandwrite():
     
    def __init__(self, text, subject):
        self.text = subject
        self.text = text
        self.filename = f"taskfolder/{subject}.txt"


    # write into a file and create
    def write(self):
        content = text
        # Open the file in write mode and write the content to it
        with open(self.filename, "w") as file:
            file.write(content)
        
        print(f"{self.filename} has been created with the specified content.")

    # read from file 
    def read(self):
        with open(self.filename, 'r') as file:
            file_content = file.read()
            print(file_content)


    # make changes within file 
    def change(self):
        # Specify the name of the file
        filename = self.filename

        # Step 1: Read the existing content of the file
        with open(filename, "r") as file:
            content = file.read()

        print("Original Content:")
        print(content)
        new_text = "i am saba and i love programming "
        new_content = content.replace(self.text, new_text)

        print("Modified Content:")
        print(new_content)

        with open(filename, "w") as file:
            file.write(new_content)
        print(f"{filename} has been updated with the modified content.")

    # delete file 
    def delete(self):

        filename = self.filename

        # Check if the file exists before attempting to delete it
        if os.path.exists(filename):
            os.remove(filename)
            print(f"{filename} has been deleted.")
        else:
            print(f"{filename} does not exist.")


text = "hello, my name is saba and i am glad to be here"
subject = "saba"

# reader = Readeandwrite(text, subject)
# reader.delete()
# reader.write()
# reader.change()
# reader.read()







