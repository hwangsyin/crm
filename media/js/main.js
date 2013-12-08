function onMouseOverMenuItem() {
    this.style.backgroundColor = "#F1F1F1";
    this.style.cursor = "pointer";
}

function onMouseOverMenuItemButton() {
    this.style.backgroundColor = "#9F0B10";
}

function onMouseDownMenuItemButton() {
    this.style.border = "1px solid #D3D3D3";
}

function onMouseUpMenuItemButton() {
    this.style.border = "";
}

function onMouseOutMenuItem() {
    this.style.backgroundColor = "#FFFFFF";
}

function onMouseOutMenuItemButton() {
    this.style.backgroundColor = "#DD4B39";
}

function onClickMenuItemButton() {
    setData(this.getAttribute("data-container"), this.getAttribute("data-href"), this.getAttribute("data-callback"));
}

function onMouseOverCustomer(element) {
    $(element).addClass("c-mo");
}

function onMouseOutCustomer(element) {
    $(element).removeClass("c-mo");
}

function onClickCustomer(element) {
    setData("content", element.getAttribute("data-href"), null);
}

function onClickMenuItem() {
    setClickedMenuItemStyle(this);
    clickedMenuItem = this;
    contentURL = this.getAttribute("data-href");
    sessionStorage.setItem("content.url", contentURL);
    sessionStorage.setItem("menuitem.clicked", this.getAttribute("id"));
    setData(this.getAttribute("data-container"), contentURL, this.getAttribute("data-callback"));
}

function bindMenuAction() {
    var menuItems = $("#menu")[0].childNodes;
    var node;
    var type;
    var onmouseoverHandler;
    var onmouseoutHandler;
    var onclickHandler;
    for (var i = 0; i < menuItems.length; i++) {
        if ((node = menuItems.item(i)).nodeType == Node.ELEMENT_NODE) {
            type = node.getAttribute("data-type");
            if (type == "text") {
                onmouseoverHandler = onMouseOverMenuItem;
                onmouseoutHandler = onMouseOutMenuItem;
                onclickHandler = onClickMenuItem;
            } else if (type == "button") {
                onmouseoverHandler = onMouseOverMenuItemButton;
                onmouseoutHandler = onMouseOutMenuItemButton;
                onclickHandler = onClickMenuItemButton;
                
                node.onmousedown = onMouseDownMenuItemButton;
                node.onmouseup = onMouseUpMenuItemButton;
            }

            node.onmouseover = onmouseoverHandler;
            node.onmouseout = onmouseoutHandler;
            node.onclick = onclickHandler;
        }
    }
}

function loadContent() {
    var clickedMenuItemId = sessionStorage.getItem("menuitem.clicked");
    if (clickedMenuItemId) {
        clickedMenuItem = $("#" + clickedMenuItemId)[0];
	    if (clickedMenuItem) {
	        setClickedMenuItemStyle(clickedMenuItem);
		    setData(clickedMenuItem.getAttribute("data-container"), 
                    clickedMenuItem.getAttribute("data-href"), clickedMenuItem.getAttribute("data-callback"));
        }
    }
}

function setData(container, url, callbackName) {
    var xhr = new XMLHttpRequest();
    var customer_list_html;
    xhr.onreadystatechange = function() {
        if (this.readyState == this.DONE && this.status == 200) {
            $("#" + container).html(this.responseText);
            if (callbackName) {
                window[callbackName]();
            }
	    }
    }
    xhr.open("GET", url);
    xhr.send();
}

function setClickedMenuItemStyle(menuItemElement) {
    if (clickedMenuItem) {
        clickedMenuItem.style.borderLeftColor = "";
        clickedMenuItem.style.backgroundColor = "#FFFFFF";
    }
    menuItemElement.style.borderLeftColor = "#DD4B39";
}

function onLoadCustomerList() {
}

function onLoadSessionList() {
}

function onLoadAddCustomerUI() {

}

function onLoadAddSessionUI() {

}

function addCustomer(element) {
    var form = document.forms["customer"];
    var data = {
        title: form["title"].value,
        name: form["name"].value,
        phone: form["phone"].value,
        email: form["email"].value,
        age: form["age"].value,
        address: form["address"].value,
        type: form["type"].value,
        enable: form["enable"].value
    };

    $.ajax(form.action, {
        type: form.method,
        "data": data,
        success: function(response, textStatus, jqXHR) {
            $("#content").html(response);
        }
    });
}
