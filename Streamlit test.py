import streamlit as st
import pandas as pd

# YouTube Dowloader
"""
YouTube Downloader
"""
@st.cache_data(show_spinner=False)
# Download Single Video
def File_Download (Link , Path):
    from pytube import YouTube
    url = Link
    video = YouTube(url)
    video_streams = video.streams.filter(file_extension = 'mp4').get_by_itag(22)
    video_streams.download(output_path = Path)

# Download Playlist Video
def Playlist_Download (Link , Path):
    from pytube import Playlist
    playlist_url = Link
    playlist = Playlist(playlist_url)
    for video in playlist.videos:
        stream = video.streams.get_highest_resolution()
        stream.download(Path)


def main():
    Link = st.text_input("Link")
    Path = st.text_input("Path")
    Usr_inpt = st.selectbox("Select" , ["-","Single_Video" , "Playlist"])
    st.button('Start Download')

    while Link or Path == "":
        if Usr_inpt == "Single_Video":
            st.button('Start Download' , on_click=File_Download (Link , Path))
        elif Usr_inpt == "Playlist":
            st.button('Start Download' , on_click=Playlist_Download (Link , Path))
        else:
            pass

if __name__ == "__main__":
    main()

