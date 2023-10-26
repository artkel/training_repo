class FileSharer:
    """
    Uploads file into the cloud.
    """

    def __init__(self, filepath, api_key='A2aESpcX9QJGDyGEbeArIz'):
        self.api_key = api_key
        self.filepath = filepath

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url