"""A video player class."""

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos.

        1.Get list of videos_keys
        2.loop through videos_key and return formatted.

        """

        print("Here's a list of all available videos:")
        keys_videos = list(self._video_library._videos.keys())
        keys_videos.sort()
        for key in keys_videos:
            current_video = self._video_library.get_video(key)
            all_tags = " ".join(current_video.tags)
            all_title = current_video.title
            all_id = current_video.video_id
            print("{} ({}) [{}]".format(all_title, all_id, all_tags))

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        1.Get list of all keys
        2.if keys_id = video_id then set to variable (current_video and current_title)
        print() Playing video: video_title) else Cannot play video:Video does not exist
        3. whilst, video is playing - print Stopping video: (prev_video) Playing video (new_video)
        4.if same video_id  

        """
        keys_videos = list(self._video_library._videos.keys())
        if(video_id in keys_videos):
            current_video = self._video_library.get_video(video_id)
            current_title = current_video.title
            current_playing = self._video_library.playing_video
            print("Playing video: {}".format(current_title))
            print("Current video:{}".format(current_playing))
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video.
        1.check for current_video 
        2.if there is current_video - print("Stopping video:" <video_id>)
        3.if there is no current_videp  - print("Cannot stop video: No video is currently playing")
        """

        print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""

        print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
