# 客户
class Customer:
    def __init__(self):
        self.id = None
        self.title = None
        self.name = None
        self.age = None
        self.phone = None
        self.email = None
        self.address = None

    def to_doc(self):
        doc = {}
        doc["id"] = self.id
        doc["title"] = self.title
        doc["name"] = self.name
        doc["age"] = self.age
        doc["phone"] = self.phone
        doc["email"] = self.email
        doc["address"] = self.address

        return doc

# 用户
class User:
    pass

# 电话记录
class CallRecord:
    pass
