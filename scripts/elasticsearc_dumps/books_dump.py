import base64


def getbase64(filename):
    return base64.b64encode(open(filename,'rb').read())

def create_data_dump():
    SAMPLE_QUERY = ["potter", "sharma", "amish", "pie"]

if __name__ == '__main__':
    print(getbase64('../goodreadsAPI/file.pdf'))
