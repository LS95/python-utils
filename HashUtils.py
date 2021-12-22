'''
哈希算法、编码等
'''
import hashlib
import uuid
from hashlib import md5
import hmac
import base64


################################################
def get_md5(*args):
    """
    @summary: 获取唯一的32位md5
    ---------
    @param *args: 参与联合去重的值
    ---------
    @result: 7c8684bcbdfcea6697650aa53d7b1405
    """

    m = hashlib.md5()
    for arg in args:
        m.update(str(arg).encode())

    return m.hexdigest()


def get_sha1(*args):
    """
    @summary: 获取唯一的40位值， 用于获取唯一的id
    ---------
    @param *args: 参与联合去重的值
    ---------
    @result: ba4868b3f277c8e387b55d9e3d0be7c045cdd89e
    """

    sha1 = hashlib.sha1()
    for arg in args:
        sha1.update(str(arg).encode())
    return sha1.hexdigest()  # 40位


def get_base64encode(arg):
    """
    @summary: 获取唯一的base64编码值
    ---------
    ---------
    @result: 字符串
    """
    if not isinstance(arg, bytes):
        arg = bytes(arg, encoding="utf-8")
    result = str(base64.b64encode(arg), encoding="utf-8")
    return result


def get_base64decode(arg):
    """
    @summary: 获取唯一的base64编码值
    ---------
    ---------
    @result: 字符串
    """
    result = base64.b64decode(arg)
    return result


def get_hmac_sha256(secret, message):
    """
    @summary: 数字证书签名算法是："HMAC-SHA256"
              参考：https://www.jokecamp.com/blog/examples-of-creating-base64-hashes-using-hmac-sha256-in-different-languages/
    ---------
    @param secret: 秘钥
    @param message: 消息
    ---------
    @result: 签名输出类型是："base64"
    """

    message = bytes(message, "utf-8")
    secret = bytes(secret, "utf-8")

    signature = base64.b64encode(
        hmac.new(secret, message, digestmod=hashlib.sha256).digest()
    ).decode("utf8")
    return signature


def get_uuid(key1="", key2=""):
    """
    @summary: 计算uuid值
    可用于将两个字符串组成唯一的值。如可将域名和新闻标题组成uuid，形成联合索引
    ---------
    @param key1:str
    @param key2:str
    ---------
    @result:
    """

    uuid_object = ""

    if not key1 and not key2:
        uuid_object = uuid.uuid1()
    else:
        hash = md5(bytes(key1, "utf-8") + bytes(key2, "utf-8")).digest()
        uuid_object = uuid.UUID(bytes=hash[:16], version=3)

    return str(uuid_object)


def test():
    print(get_uuid())
    print(get_md5("admin"))
    a = b'admin'
    print(type(a))
    a = get_base64encode(a)
    print(a)
    res = get_base64decode(a)
    print(res)
    aa = 'admin'
    print(type(aa))
    aa = get_base64encode(aa)
    res = get_base64decode(aa)
    print(res)
    print(get_uuid())
    print(get_hmac_sha256("admin", "password"))


if __name__ == '__main__':
    test()
