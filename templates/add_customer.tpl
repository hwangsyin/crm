<div class="customer-add">
    <div class="customer-add-title">添加客户</div>
    <form name="customer" class="ca-f" action="/customers" method="POST">
        <div>
            <label class="ca-f-l">称呼:&nbsp;</label><input type="text" name="title"/>
        </div>
        <div>
            <label class="ca-f-l">姓名:&nbsp;</label><input type="text" name="name"/>
        </div>
        <div>
            <label class="ca-f-l">电话:&nbsp;</label><input type="text" name="phone"/>
        </div>
        <div>
            <label class="ca-f-l">电子邮件:&nbsp;</label><input type="text" name="email"/>
        </div>
        <div>
            <label class="ca-f-l">年龄:&nbsp;</label><input type="text" name="age"/>
        </div>
        <div>
            <label class="ca-f-l">地址:&nbsp;</label><input type="text" name="address"/>
        </div>
        <div>
            <label class="ca-f-l">类型:&nbsp;</label>
            <select name="type">
                <option value="1">1类</option>
                <option value="2">2类</option>
                <option value="3">3类</option>
            </select>
        </div>
        <div>
            <label class="ca-f-l">启(禁)用:&nbsp;</label>
            <select name="enable">
                <option value="1">启用</option>
                <option value="0">禁用</option>
            </select>
        </div>
        <div>
            <input type="button" value="添加" onclick="addCustomer()"/>
        </div>
    </form>
</div>
