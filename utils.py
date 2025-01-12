from models import Video


def get_video_details_from_user() -> Video:
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
