# Import the zipfile module
import zipfile


#Using the zipfile module add actors.csv and chores.csv to a zip file called my_stuff.zip
def create_zip_file():
    # Create a ZipFile object
    with zipfile.ZipFile('my_stuff.zip', 'w') as zipf:
        # Add the files to the zip file
        zipf.write('actors.csv')
        zipf.write('chores.csv')

# Call the function to create the zip file  
create_zip_file()

