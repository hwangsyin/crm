// 客户
var customers = [
	{"id": NumberLong("1"), "title": "李先生", 
		"phone": [{"number": "18610231124"}, {"number": "18610231125"}], 
		"name": "李明扬", "email": "morrislee@gmail.com", "age": 36, 
		"address": "香港中环", "start_time": new Date(2012, 12, 31), "end_time": null,
		"enable": true, "type": "1"},
	{"id": NumberLong("2"), "title": "余先生", 
		"phone": [{"number": "18610231126"}, {"number": "18610231127"}], 
		"name": "余英伟", "email": "wilsonyu@gmail.com", "age": 35, 
		"address": "香港九龙", "start_time": new Date(2012, 12, 30), "end_time": null,
		"enable": true, "type": "2"},
	{"id": NumberLong("3"), "title": "陆小姐", 
		"phone": [{"number": "18610231128"}, {"number": "18610231129"}], 
		"name": "陆思凝", "email": "sheila@gmail.com", "age": 34, 
		"address": "香港九龙", "start_time": new Date(2012, 12, 29), "end_time": null,
		"enable": true, "type": "3"},
	{"id": NumberLong("4"), "title": "沈小姐", 
		"phone": [{"number": "18610231130"}, {"number": "18610231131"}], 
		"name": "沈悦勤", "email": "eugene@gmail.com", "age": 33, 
		"address": "香港中环", "start_time": new Date(2012, 12, 28), "end_time": null,
		"enable": true, "type": "1"}
];

db.customer.remove();
db.customer.insert(customers);
db.customer.ensureIndex({"id": true});

// 客户类型
var customerTypes = [
	{"id": NumberLong("1"), "key": "1", "name": "1类", "display_name": "1", 
		"description": "1类客户", "enable": true},
	{"id": NumberLong("2"), "key": "2", "name": "2类", "display_name": "2", 
		"description": "2类客户", "enable": true},
	{"id": NumberLong("3"), "key": "3", "name": "3类", "display_name": "3", 
		"description": "3类客户", "enable": true}
];

db.customer_type.remove();
db.customer_type.insert(customerTypes);
db.customer_type.ensureIndex({"id": true});
db.customer_type.ensureIndex({"key": true});

// 会话
var sessions = [
	{"id": "", }
];