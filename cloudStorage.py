from os import truncate
import dropbox
    
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to): 
        dbx = dropbox.Dropbox(self.access_token)


        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():
    access_token = 'sl.Ayz6lvn02b89YqrX8rBgjglURdpClouQGuwZ6Iflh3_W_LxxV4eVthRDwdbr4I2NixpOtm15CeBVKBcG8yVY-T9flJIG0DChP9dsmJZ283ujQk_a3oiR_FPF0UnwcmoY2TPoPKQ'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer")
    file_to = input("enter the full path to enter into dropbox")

    transferData.upload_file(file_from, file_to)
    print("file has been moved")


main()