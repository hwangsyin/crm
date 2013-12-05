# 客户
class Customer:
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
            self.phone = [ number["number"] for number in customer_doc["phone"] ] if customer_doc["phone"] else ""
            self.start_time = customer_doc["start_time"]
            self.type = CustomerType(customer_doc["type"])
        except KeyError:
            pass

    def spec(self):
        if not self:
            return None

        result = {}

        if self.id:
            result["id"] = self.id
        if self.title:
            result["title"] = {"$regex": "/" + self.title + "/"}
        if self.name:
            result["name"] = {"$regex": "/" + self.name + "/"}
        if self.email:
            result["email"] = {"$regex": "/" + self.email + "/"}

        return result

    def html_phone(self):
        if self.phone:
            result = ["电话:<br/>"]
            length = len(self.phone)
            for i in range(length):
                result.append(self.phone[i])
                if i < length - 1:
                    result.append("<br/>")
            result = "".join(result)
        else:
            result = ""

        return result
    def html_phone_1(self):
        if self.phone:
            return self.phone[0]
        else:
            return ""

# 客户类型
class CustomerType:
    def __init__(self, customer_type_doc):
        if not customer_type_doc:
            return None
        try:
            self.id = customer_type_doc["id"]
            self.key = customer_type_doc["key"]
            self.name = customer_type_doc["name"]
            self.display_name = customer_type_doc["display_name"]
            self.description = customer_type_doc["description"]
            self.enable = customer_type_doc["enable"]
        except KeyError:
            pass

    def repr_json(self):
        if not self:
            return "{}"
        else:
            from string import Template
            t = Template('{"id": $id, "key": "$key", "name": "$name", "display_name": "$display_name", \
                    "description": "$description", "enable": $enable}')
            return t.substitute(id = self.id, key = self.key, name = self.key, \
                    display_name = self.display_name, description = self.description, enable = self.enable)

# 用户
class User:
    pass

# 会话
class Session:
    def __init__(self, session_doc = None):
        if not session_doc:
            return None
        
        # 系统 ID (字符串)
        try:
            self.id = session_doc["id"]
        except KeyError:
            pass

        # 会话内容
        try:
            self.content = session_doc["content"]
        except KeyError:
            pass

        # 开始时间
        try:
            self.start_time = session_doc["start_time"]
        except KeyError:
            pass

        # 结束时间
        try:
            self.end_time = session_doc["end_time"]
        except KeyError:
            pass

        # 客户
        try:
            self.customer_id = session_doc["customer_id"]
        except KeyError:
            pass

        # 业务代表
        try:
            self.agent_id = session_doc["agent_id"]
        except KeyError:
            pass

        # 会话类型
        try:
            self.type = session_doc["type"]
        except KeyError:
            pass

        # 业务代表所在位置
        try:
            self.agent_place = session_doc["agent_place"]
        except KeyError:
            pass
