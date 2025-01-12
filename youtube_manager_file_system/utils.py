from youtube_manager_file_system.models import Video


def create_new_video() -> Video:
    try:
        video_id = input("\tEnter the Video ID: ")
        title = input("\tEnter the Title: ")
        views = int(input("\tEnter the Views: "))
        channel = input("\tEnter the Channel: ")
    except ValueError:
        print("\n\tInvalid Input")
    else:
        return {
            "video_id": video_id,
            "title": title,
            "views": views,
            "channel": channel
        }


def find_update_index(videos):
    user_update_index = int(input("Enter the video number you want to update: ")) - 1

    if user_update_index < 0 or user_update_index > len(videos):
        print("Invalid number. Exiting....")
        return -1

    return user_update_index

def display_user_options():
    print("""---------- YOUTUBE MANAGER ----------

    1. List all videos
    2. Add a video
    3. Update a video
    4. Delete a video
    5. Exit the application
    """)

def add_newline_and_tab(func):
    def wrapper(*args, **kwargs):
        return f"\n\t {func(*args, **kwargs)}"
    return wrapper

@add_newline_and_tab
def print_message(message):
    return message
