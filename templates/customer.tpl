<div class="customer-info">
    {% autoescape None %}
    {% if customer %}
    <p class="customer-info-field">
        <label>系统 ID:&nbsp;&nbsp;</label>
        <span>{{ customer.id }}</span>
    </p>
    <p class="customer-info-field">
        <label>称呼:&nbsp;&nbsp;</label>
        <span>{{ customer.title }}</span>
    </p>
    <p class="customer-info-field">
        <label>姓名:&nbsp;&nbsp;</label>
        <span>{{ customer.name }}</span>
    </p>
    <p class="customer-info-field">
        <label>电话:&nbsp;&nbsp;</label>
        <span>{{ customer.phone_str_html() }}</span>
    </p>
    <p class="customer-info-field">
        <label>Email:&nbsp;&nbsp;</label>
        <span>{{ customer.email }}</span>
    </p>
    <p class="customer-info-field">
        <label>年龄:&nbsp;&nbsp;</label>
        <span>{{ customer.age }}</span>
    </p>
    <p class="customer-info-field">
        <label>地址:&nbsp;&nbsp;</label>
        <span>{{ customer.address }}</span>
    </p>
    <p class="customer-info-field">
        <label>加入时间:&nbsp;&nbsp;</label>
        <span>{{ customer.start_time.strftime("%Y-%m-%d") if customer.start_time else ""}}</span>
    </p>
    <p class="customer-info-field">
        <label>退出时间:&nbsp;&nbsp;</label>
        <span>{{ customer.end_time.strftime("%Y-%m-%d") if customer.end_time else "" }}</span>
    </p>
    <p class="customer-info-field">
        <label>有（无）效:&nbsp;&nbsp;</label>
        <span>
            {% if customer.enable == False %}
                无效
            {% elif customer.enable == True %}
                有效
            {% end %}
        </span>
    </p>
    <p class="customer-info-field">
        <label>客户类型:&nbsp;&nbsp;</label>
        <span>{{ customer.type.display_name if customer.type else "" }}</span>
    </p>
    {% else %}
    <p class="customer-info-field">查不到该客户的信息</p>
    {% end %}
</div>
