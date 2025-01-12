import copy
import json
from pathlib import Path
from typing import List

from models import Video
from utils import create_new_video, find_update_index, print_message, pretty_print


def list_all_videos(videos: List[Video]) -> None:
    print("\nList of all your videos\n")
    for index, video_entry in enumerate(videos, start=1):
        print(f"""{index}.  -----------------------------------
        video_id: {video_entry['video_id']}
        title: {video_entry['title']}
        views: {video_entry['views']}
        channel: {video_entry['channel']}
    """)


def add_video(videos: List[Video]):
    try:
        copied_videos = copy.deepcopy(videos)
        new_video = create_new_video()
        copied_videos.append(new_video)
        save_videos(copied_videos)
    except Exception as error:
        print("An error occurred:", error)
    else:
        print("\n\tVideo added successfully\n")


def update_video(videos: List[Video]):
    try:
        list_all_videos(videos)

        user_update_index = find_update_index(videos)

        if user_update_index == -1:
            return

        updated_video = create_new_video()

        videos[user_update_index].update(updated_video)

        save_videos(videos)
    except Exception as error:
        print("An error occurred:", error)
    else:
        print("\n\tVideo updated successfully\n")


def delete_video(videos: List[Video]):
    try:
        user_delete_index = int(input("Enter the video number to delete: "))
        if user_delete_index < 0 or user_delete_index >= len(videos):
            print("\n\tYou entered invalid video number.")
            return
        updated_videos = [video_entry for index, video_entry in enumerate(videos) if index != user_delete_index]
        save_videos(updated_videos)
    except Exception as error:
        print("An error occurred:", error)
    else:
        print_message("Video deleted successfully")


videos_file_path = Path("./videos.json").resolve()


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
