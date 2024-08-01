def main():
    # Prompt the user for the file name
    file_name = input("File name: ").strip().lower()

    # Determine the media type based on the file extension
    media_type = get_media_type(file_name)

    # Output the media type
    print(media_type)


def get_media_type(file_name):
    # Dictionary for file extensions to media types
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }

    # Iterate over the dictionary to find the media type
    for extension, media_type in media_types.items():
        if file_name.endswith(extension):
            return media_type

    # Default media type if no match is found
    return "application/octet-stream"


main()
