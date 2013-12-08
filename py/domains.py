# 客户
class Customer:
    id = None
    title = None
    phone = []
    name = None
    age = None
    email = None
    address = None
    type = None
    enable = None
    start_time = None
    end_time = None

    def __init__(self, customer_doc):
        if not customer_doc:
            return

        try:
            self.id = customer_doc["id"]
        except KeyError:
            self.id = ""
        try:
            self.title = customer_doc["title"]
        except KeyError:
            self.title = ""
        try:
            self.name = customer_doc["name"]
        except KeyError:
            self.name = ""
        try:
            self.age = customer_doc["age"]
        except KeyError:
            self.age = ""
        try:
            self.email = customer_doc["email"]
        except KeyError:
            self.email = ""
        try:
            self.address = customer_doc["address"]
        except KeyError:
            self.address =""
        try: 
            self.phone = customer_doc["phone"]
        except KeyError:
            self.phone = []
        try:
            self.start_time = customer_doc["start_time"]
        except KeyError:
            self.start_time = None
        try:
            self.end_time = customer_doc["end_time"]
        except KeyError:
            self.end_time = None
        try:
            self.enable = customer_doc["enable"]
        except KeyError:
            self.enable = None
        try:
            self.type = CustomerType(customer_doc["type"])
        except KeyError:
            self.type = None

    def doc(self):
        result = {}
        result["id"] = self.id
        result["title"] = self.title
        result["phone"] = self.phone
        result["name"] = self.name
        result["email"] = self.email
        result["address"] = self.address
        result["age"] = self.age
        result["start_time"] = self.start_time
        result["end_time"] = self.end_time
        result["enable"] = self.enable
        result["type"] = self.type.key

        return result

    def phone_str_html(self):
        if not self.phone:
            return ""
        else:
            p_str = []
            length = len(self.phone)
            for i in range(length):
                p_str.append(self.phone[i])
                if i < length - 1:
                    p_str.append(",&nbsp;")
            return "".join(p_str)

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
    id = None
    key = None
    name = None
    display_name = None
    enable = None
    description = None

    def __init__(self, customer_type_doc):
        if not customer_type_doc:
            return
        try:
            id = customer_type_doc["id"]
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
    id = None
    name = None
    gender = None
    phone = None
    email = None
    join_time = None
    quit_time = None

# 会话
class Session:
    # 系统 ID (字符串)
    id = None
    # 会话内容
    content = None
    # 开始时间
    start_time = None
    # 结束时间
    end_time = None
    # 客户
    customer = None
    # 业务代表
    agent = None
    # 会话类型
    type = None
    # 业务代表所在位置
    agent_place = None

    def __init__(self, session_doc = None):
        if not session_doc:
            return None
        
        try:
            self.id = session_doc["id"]
        except KeyError:
            pass
        
        try:
            self.content = session_doc["content"]
        except KeyError:
            pass
        
        try:
            self.start_time = session_doc["start_time"]
        except KeyError:
            pass
        
        try:
            self.end_time = session_doc["end_time"]
        except KeyError:
            pass
        
        try:
            self.customer = Customer(None)
            self.customer.id = session_doc["customer_id"]
        except KeyError:
            pass
        
        try:
            self.agent = User()
            self.agent.id = session_doc["agent_id"]
        except KeyError:
            pass
        
        try:
            self.type = session_doc["type"]
        except KeyError:
            pass
        
        try:
            self.agent_place = session_doc["agent_place"]
        except KeyError:
            pass
