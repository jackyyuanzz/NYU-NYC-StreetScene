import requests
import os
import argparse

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download&confirm=1"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)
    
def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None
    
def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                

VID_IDS = {
 '78' : '1DbJzdzG17wryno0fy5Gvuif-NdMU9GpE',
 '79' : '1EPH9j66bxLWBCmZZlDUQG5nhY-R2FZ6K',
 '80' : '1xnvMaeJf6xgZ2-_pAVX1z6eHNpwulv_4',
 '81' : '1nBx7gHlZxyackh7HM-ydjBTz7wwHOdj7',
 '82' : '1-Zx41GjVOWYyZZO5FtdArEa4yTQPVG9I',
 '83' : '18VkLXzrb0uEAqLY0x40Yvh30iYzYv5BS',
 '84' : '16DMvZULUsb9jgJTFUSvUzI7IJHX2zB1V',
 '85' : '1TqZQgzDF9jJLtGxY4KBYX3SjX22FO_SO',
 '86' : '1eXNmCvS88qkim6l-oEauI-3SjqHXFsta'
 }
 
Bounding_Box_ID = '1Yxqcq4BOXMqkfugbzFn6mhnYskUOotVI'
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_id', type=int, default=None, help='Download a single video of this id')
    parser.add_argument('--save_dir', type=str, default="NYU_StreetScene", help='Directory to download the data to, create in current dir if not exist')
    parser.add_argument('--bbox_only', action='store_true')
    
    opt = parser.parse_args()
    
    os.makedirs(opt.save_dir, exist_ok=True)
    
    if opt.bbox_only:
        print('Downloading Lables ...')
        download_file_from_google_drive(Bounding_Box_ID, opt.save_dir+'/bounding_box_labels.zip')
        exit()
    if opt.video_id == None:
        print('Download Starting for All Video Files...')
        for i in range(78, 87):
            file_id = VID_IDS[str(i)]
            download_file_from_google_drive(file_id, opt.save_dir+'/'+'video{}.svo'.format(str(i)))
            print('Downloading Video {} ...'.format(str(i)))
    elif opt.video_id != None:
        print('Downloading Video {} ...'.format(str(opt.video_id)))
        file_id = VID_IDS[str(opt.video_id)]
        download_file_from_google_drive(file_id, opt.save_dir+'/'+'video{}.svo'.format(str(opt.video_id)))
            
    print('Downloading Lables ...')
    download_file_from_google_drive(Bounding_Box_ID, opt.save_dir+'/bounding_box_labels.zip')
        
    
