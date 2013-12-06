{% autoescape None %}
<div class="customer-list" id="item-list">
    {% if customer_list %}
        {% for customer in customer_list %}
        <div class="customer" id="{{customer.id}}" data-href="/customers/{{ customer.id }}">
            <span class="customer-field cf-select"><input type="checkbox" id="customer-checkbox-{{ customer.id }}"/></span><span class="customer-field cf-title">{{ customer.title }}</span><span class="customer-field cf-name">{{ customer.name }}</span><span class="customer-field cf-phone">{{ customer.html_phone_1() }}</span><span class="customer-field cf-type">{{ customer.type.name }}</span><span class="customer-field cf-email">{{ customer.email }}</span><span class="customer-field cf-stime">{{ customer.start_time.strftime("%Y-%m-%d %H:%M") }}</span>
        </div>
        {% end %}
    {% else %}
        没有满足条件的客户
    {%  end %}
</div>
