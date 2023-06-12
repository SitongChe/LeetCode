import os

def generate_md_file(folder_path, output_file):
    # Open the output file in write mode
    with open(output_file, 'w') as md_file:
        # Write the header
        md_file.write("# Folder Contents\n\n")
        
        # Iterate over the files and subdirectories in the folder
        for root, dirs, files in os.walk(folder_path):
            files.sort()
            
            # Write the files in the current directory
            for file_name in files:
                if file_name.endswith(".py"):
                    file_path = os.path.join(os.path.basename(root), file_name)
                    md_file.write("- [{}]({})\n".format(file_name, file_path))
            
            # Write a newline to separate directories
            md_file.write("\n")

# Provide the folder path and output file name
folder_path = "/Users/chesitong/Documents/GitHub/leetcode/"
output_file = "folder_contents.md"

# Generate the Markdown file
generate_md_file(folder_path, output_file)

print("Markdown file '{}' generated successfully.".format(output_file))
