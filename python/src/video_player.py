"""A video player class."""

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.excecuting_video = -1
        self.listPause = [0]*len(self._video_library.get_all_videos())
        self.listID = sorted(self._video_library._videos2.keys())
        self.listNames = []
        self.listNamesID = []
        self.listNamesTAG = []
        for key, [value1, value2, value3] in sorted(self._video_library._videos2.items()):
            self.listNames.append(value1)
            self.listNamesID.append(value2)
            self.listNamesTAG.append(value3)


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        num_videos = len(self._video_library.get_all_videos())

        print("Here's a list of all available videos:")
        for key, [value1, value2, value3] in sorted(self._video_library._videos2.items()):
            print(value1, ' (', value2 , ') [',  value3, ']', sep='')

    def play_video(self, video_id):
        IDvid = [i for i, x in enumerate(self.listID) if x == video_id]

        if IDvid == []:
            print("Cannot play video: Video does not exist")
        else:
            IDvid = IDvid[0]

            if self.excecuting_video >=0:
                print("Stopping video:", self.listNames[self.excecuting_video] )
                self.listPause[self.excecuting_video] = 0

            print("Playing video:", self.listNames[IDvid])
            self.excecuting_video = IDvid


    def stop_video(self):
        """Stops the current video."""

        if self.excecuting_video == -1:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video:", self.listNames[self.excecuting_video])
            self.listPause[self.excecuting_video] = 0
            self.excecuting_video = -1


    def play_random_video(self):
        """Plays a random video from the video library."""
        import random

        IDvid = random.randint(0, len(self._video_library.get_all_videos())-1)

        if self.excecuting_video >= 0:
            print("Stopping video:", self.listNames[self.excecuting_video])

        print("Playing video:", self.listNames[IDvid])
        self.excecuting_video = IDvid

    def pause_video(self):
        """Pauses the current video."""

        if self.excecuting_video == -1:
            print("Cannot pause video: No video is currently playing")
        elif self.listPause[self.excecuting_video]==1:
            print("Video already paused:", self.listNames[self.excecuting_video])
        else:
            print("Pausing video:", self.listNames[self.excecuting_video])
            self.listPause[self.excecuting_video] = 1


    def continue_video(self):
        """Resumes playing the current video."""

        if self.excecuting_video == -1:
            print("Cannot continue video: No video is currently playing")
        elif self.listPause[self.excecuting_video]==0:
            print("Cannot continue video: Video is not paused")
        else:
            print("Continuing video:", self.listNames[self.excecuting_video])
            self.listPause[self.excecuting_video] = 0

    def show_playing(self):
        """Displays video currently playing."""
        if self.excecuting_video == -1:
            print("No video is currently playing")
        elif self.listPause[self.excecuting_video] == 0:
            print("Currently playing: ", self.listNames[self.excecuting_video],
                  ' (', self.listNamesID[self.excecuting_video], ') [', self.listNamesTAG[self.excecuting_video], ']', sep='')
        else:
            print("Currently playing: ", self.listNames[self.excecuting_video],
                  ' (', self.listNamesID[self.excecuting_video], ') [', self.listNamesTAG[self.excecuting_video], "] - PAUSED", sep='')


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
