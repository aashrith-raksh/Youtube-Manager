from youtube_manager_db.db import init_db, close_db
from youtube_manager_file_system.utils import print_message

conn, cur = init_db()


def list_videos_from_db():
    try:
        cur.execute("SELECT * FROM YOUTUBE")

        rows = cur.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print_message("No videos found in the database.")

    except Exception as e:
        print_message(e)


def add_video_to_db():
    try:
        title = input("\tEnter the Title: ")
        views = int(input("\tEnter the Views: "))
        channel = input("\tEnter the Channel: ")

        cur.execute('''
        INSERT INTO YOUTUBE 
        (title, views, channel)
        VALUES (?, ?, ?)
        ''', (title, views, channel))

        conn.commit()

    except Exception as e:
        print_message("An error occured while adding video to database\n")
        print_message(e)
    else:
        print_message("Successfully added video to database")


def update_video_in_db():
    try:
        video_id = input("\tEnter the Video ID to update: ")

        updates = []
        values = []

        title_update = input("Do you want to update video title? (Y/N):")
        if title_update == "Y":
            new_title = input("\tEnter the New Title: ")
            updates.append("title = ?")
            values.append(new_title)

        views_update = input("Do you want to update video view count? (Y/N):")
        if views_update == "Y":
            new_views_count = input("\tEnter the New Video View Count: ")
            updates.append("views = ?")
            values.append(new_views_count)

        channel_update = input("Do you want to update video channel? (Y/N):")
        if channel_update == "Y":
            new_channel = input("\tEnter the New Video Channel: ")
            updates.append("channel = ?")
            values.append(new_channel)

        query = f"UPDATE YOUTUBE SET {', '.join(updates)} WHERE video_id = ?"
        values.append(video_id)

        cur.execute(query, values)
        conn.commit()

    except Exception as e:
        print_message(e)

    else:
        print_message("Successfully updated video in database")


def delete_video_in_db():
    try:
        video_id = input("\tEnter the Video ID to delete: ")

        cur.execute('''
        DELETE FROM YOUTUBE WHERE video_id = ?
        ''', (video_id,))

    except Exception as e:
        print_message(e)
    else:
        print_message("Successfully deleted video in database")


def exit_app():
    close_db(conn, cur)
