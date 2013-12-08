<div>
    <div>添加会话</div>
    <form nam="session" action="/sessions" method="POST">
        <div>
            <label>客户:&nbsp;</label><input type="text" name="customer_id" value="输入客户姓名或电话号码以搜索" />
        </div>
        <div>
            <label>业务代表:&nbsp;</label><input type="text" name="agent_id" value="1"/>
        </div>
        <div>
            <label>位置:&nbsp;</label><input type="text" name="agent_place" value="中关村支行"/>
        </div>
        <div>
            <label>呼出号码:&nbsp;</label><input type="text" name="agent_phone" value="01066278356"/>
        </div>
        <div>
            <label>类型:&nbsp;</label>
            <select name="type">
                <option value="1">电话</option>
                <option value="2">短信</option>
            </select>
        </div>
        <div>
            <label>开始时间:&nbsp;</label><input type="text" name="start_time"/>
        </div>
        <div>
            <label>结束时间:&nbsp;</label><input type="text" name="end_time"/>
        </div>
        <div>
            <label>内容:&nbsp;</label><input type="text" name="content"/>
        </div>
        <div>
            <input type="button" value="添加"/>
        </div>
    </form>
</div>
