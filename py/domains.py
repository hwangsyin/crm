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

    def __init__(self, customer_doc):
        if not customer_doc:
            return None
        try:
            self.id = customer_doc["id"]
            self.title = customer_doc["title"]
            self.name = customer_doc["name"]
            self.age = customer_doc["age"]
            self.email = customer_doc["email"]
            self.address = customer_doc["address"]
        except KeyError:
            pass

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
