from youtube_manager_db.main import list_videos_from_db, add_video_to_db, update_video_in_db, delete_video_in_db
from youtube_manager_file_system.utils import display_user_options


def main():
    exit_app = False

    while not exit_app:
        display_user_options()

        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                list_videos_from_db()
            case "2":
                add_video_to_db()
            case "3":
                update_video_in_db()
            case "4":
                delete_video_in_db()
            case "5":
                print("Exiting...")
                exit_app = True

if __name__ == "__main__":
    main()
