import requests
from Builder import GetAndDelHeadBuilder, UploadHeadBuilder, Director


director = Director()
file1 = "/kotik1.jpg"
auth_head = {'Authorization': 'Bearer Xk2Cp8jusrcAAAAAAAAAAZZz1krSeboLRi6zD35SxgaqywsGDfiGPX2a6eX7p6-L'}

def test_upload_file():
    head1build = UploadHeadBuilder()
    director.setBuilder(head1build)
    head1 = director.getHeaders()
    my_headers = head1.createJSN()
    headers = {**auth_head, **my_headers}
    req = requests.post("https://content.dropboxapi.com/2/files/upload", headers=headers, data=file1)
    assert "/webapi26_testing"+file1 in req.text
    result = (req.json()['id'])
    return result


def test_get_data():
    head2build = GetAndDelHeadBuilder()
    director.setBuilder(head2build)
    head2 = director.getHeaders()
    my_headers = head2.createJSN()
    headers = {**auth_head, **my_headers}
    data1 = {"path": "/webapi26_testing"+file1}
    req1 = requests.post("https://api.dropboxapi.com/2/files/get_metadata", headers=headers, json=data1)
    result = (req1.json()['id'])
    data2 = {
        "file": str(result),
        "actions": []
    }
    assert "/webapi26_testing"+file1 in requests.post("https://api.dropboxapi.com/2/sharing/get_file_metadata", headers=headers, json=data2).text


def test_del_file():
    head2build = GetAndDelHeadBuilder()
    director.setBuilder(head2build)
    head2 = director.getHeaders()
    my_headers = head2.createJSN()
    headers = {**auth_head, **my_headers}
    data3 = {
        "path": "/webapi26_testing"+file1,
    }
    assert "/webapi26_testing"+file1 in requests.post("https://api.dropboxapi.com/2/files/delete_v2", headers=headers, json=data3).text