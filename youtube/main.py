import json
from pathlib import Path
from typing import List

from models import Video
from utils import get_video_details_from_user



def list_all_videos(videos:List[Video]) -> None:
    print("\nList of all your videos\n")
    for index, video_entry in enumerate(videos, start=1):
        print(f"""{index}.  -----------------------------------
        video_id: {video_entry['video_id']}
        title: {video_entry['title']}
        views: {video_entry['views']}
        channel: {video_entry['channel']}
    """)


def add_video(videos:List[Video]):
    new_video = get_video_details_from_user()
    videos.append(new_video)
    print("\n\tNew video added\n")
    save_videos(videos)


def update_video(videos:List[Video]):
    pass


def delete_video(videos:List[Video]):
    pass


def display_user_options():
    print("""---------- YOUTUBE MANAGER ----------

    1. List all videos
    2. Add a video
    3. Update a video
    4. Delete a video
    5. Exit the application
    """)


videos_file_path = Path("videos.json").resolve()


def load_videos():
    try:
        with open(videos_file_path, "r") as f:
            json_data = json.load(f)
            return json_data
    except FileNotFoundError as err:
        print("File not found.")
        print(err)
        return []


def save_videos(videos):
    try:
        with open(videos_file_path, "w") as f:
            json.dump(videos, f, indent=4)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    videos = load_videos()
    print(f"""
    type of videos: {type(videos)}
    vidoes: {videos}
    videos_file_path: {videos_file_path}
""")

    # List of multiple JSON entries (dictionaries)
    #     data = [
    #         {"name": "Alice", "age": 25, "is_student": False},
    #         {"name": "Bob", "age": 30, "is_student": True},
    #         {"name": "Charlie", "age": 22, "is_student": True}
    #     ]
    #
    #     # Saving multiple JSON entries to a file
    #     with open("multiple_entries.json", "w") as file:
    #         json.dump(data, file, indent=4)  # Writes all entries to the file in JSON format
