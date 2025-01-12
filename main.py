from utils import display_user_options
from youtube.main import list_all_videos, add_video, update_video, delete_video, load_videos


def main():
    exit_app = False

    while not exit_app:
        loaded_videos = load_videos()
        display_user_options()

        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                list_all_videos(loaded_videos)
            case "2":
                add_video(loaded_videos)
            case "3":
                update_video(loaded_videos)
            case "4":
                delete_video(loaded_videos)
            case "5":
                print("Exiting...")
                exit_app = True


if __name__ == "__main__":
    main()
