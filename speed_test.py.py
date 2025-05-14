import speedtest

def Internet_speed_detector():
    st=speedtest.Speedtest()
    print("Finding the best server...")
    st.get_best_server()
    print("Testing download speed...")
    download_speed=st.download()/ 1024 / 1024
    print("Testing upload speed...")
    upload_speed=st.upload()/ 1024 / 1024
    print(f"\nDownload speed:{download_speed: .2f}Mbps")
    print(f"Upload speed:{upload_speed: .2f}Mbps")

if __name__=="__main__": Internet_speed_detector()

