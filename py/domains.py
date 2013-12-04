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
        self.start_time = None
        self.end_time = None

    def to_doc(self):
        doc = {}
        doc["id"] = self.id
        doc["title"] = self.title
        doc["name"] = self.name
        doc["age"] = self.age
        doc["phone"] = self.phone
        doc["email"] = self.email
        doc["address"] = self.address
        doc["start_time"] = self.start_time
        doc["end_time"] = self.end_time

        return doc

    def spec(self):
        result = {}

        if id:
            result["id"] = self.id
        if title:
            result["title"] = {"$regex": "/" + self.title + "/"}
        if name:
            result["name"] = {"$regex": "/" + self.name + "/"}
        if email:
            result["email"] = {"$regex": "/" + self.email + "/"}

        return result

# 用户
class User:
    pass

# 电话记录
class CallRecord:
    pass
