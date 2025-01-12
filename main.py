from youtube.main import display_user_options, load_videos
from youtube.main import list_all_videos, add_video, update_video, delete_video


def main():
    exit_app = False
    videos = load_videos()

    while not exit_app:
        display_user_options()

        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                exit_app = True



if __name__ == "__main__":
    main()
