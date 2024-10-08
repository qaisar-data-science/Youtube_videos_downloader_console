import pytube

while True:
    a = input("Video Url (or type 'exit' to quit): ")
    
    if a.lower() == 'exit':
        break  # Exit the loop if the user types 'exit'
    
    if not a:
        print("Please enter a valid video URL")
    else:
        try:
            fetch = pytube.YouTube(a)
            video_stream = fetch.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
            video_stream.download()
            print("Download Finished")
        except Exception as e:
            print(f"An error occurred: {e}")

exit_input = input("Press Enter to exit.")