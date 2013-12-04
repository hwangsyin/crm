url = "10.1.240.58:27017/crm";
db = connect(url);

db.customer.remove();

db.customer.insert({id: 1, title: "李先生", 
    phone_number: [{number: "18610231124"}, {number: "18610231125"}], 
    name: "李明扬", email: "morrislee@gmail.com", age: 36, 
    address: "香港中环", start_time: new Date(), end_time: null});

db.customer.insert({id: 2, title: "余先生", 
    phone_number: [{number: "18610231126"}, {number: "18610231127"}], 
    name: "余英伟", email: "wilsonyu@gmail.com", age: 35, 
    address: "香港九龙", start_time: new Date(), end_time: null});

db.customer.insert({id: 3, title: "陆小姐", 
    phone_number: [{number: "18610231128"}, {number: "18610231129"}], 
    name: "陆思凝", email: "sheila@gmail.com", age: 34, 
    address: "香港九龙", start_time: new Date(), end_time: null});

db.customer.insert({id: 4, title: "沈小姐", 
    phone_number: [{number: "18610231130"}, {number: "18610231131"}], 
    name: "沈悦勤", email: "eugene@gmail.com", age: 33, 
    address: "香港中环", start_time: new Date(), end_time: null});

db.customer.ensureIndex({id: true});
