function onMouseOverMenuItem() {
    this.style.backgroundColor = "#F1F1F1";
    this.style.cursor = "pointer";
}

function onMouseOutMenuItem() {
    if (this != clickedMenuItem) {
        this.style.backgroundColor = "#FFFFFF";
    }
}

function onMouseOverItem() {
    this.style.cursor = "pointer";
    this.style.backgroundColor = "#E0EAF1";
}

function onMouseOutItem() {
    this.style.backgroundColor = "#FFFFFF";
}

function onClickItem() {
    var itemId = this.getAttribute("id");
    var checked = document.getElementById("customer-checkbox-" + itemId).checked;
    setData("content", this.getAttribute("data-href"));
}

function onClickMenuItem() {
    setClickedMenuItemStyle(this);
    clickedMenuItem = this;
    contentURL = this.getAttribute("data-href");
    sessionStorage.setItem("content.url", contentURL);
    sessionStorage.setItem("menuitem.clicked", this.getAttribute("id"));
    setData("content", contentURL);
}

function bindMenuAction() {
    var menuItems = document.getElementById("menu").childNodes;
    var node;
    for (var i = 0; i < menuItems.length; i++) {
        if ((node = menuItems.item(i)).nodeType == Node.ELEMENT_NODE) {
	    node.onmouseover = onMouseOverMenuItem;
        node.onmouseout = onMouseOutMenuItem;
	    node.onclick = onClickMenuItem;
	}
    }
}

function loadContent() {
    var clickedMenuItemId = sessionStorage.getItem("menuitem.clicked");
    if (clickedMenuItemId != null) {
        clickedMenuItem = document.getElementById(clickedMenuItemId);
	if (clickedMenuItem != null) {
            var contentURL = sessionStorage.getItem("content.url");
	    if (contentURL != null) {
	        setClickedMenuItemStyle(clickedMenuItem);
		setData("content", contentURL);
	    } 
        }
    }
}

function setData(container, url) {
    var xhr = new XMLHttpRequest();
    var customer_list_html;
    xhr.onreadystatechange = function() {
        if (this.readyState == this.DONE && this.status == 200) {
            document.getElementById(container).innerHTML = this.responseText;
            setItemListStyle("item-list");
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
    menuItemElement.style.borderLeftColor = "red";
    menuItemElement.style.backgroundColor = "#F1F1F1";
}

function setItemListStyle(containerId) {
    if (containerId == null) {
        return;
    }
    var childNodes = document.getElementById(containerId).childNodes;
    if (childNodes == null || childNodes.length == 0) {
        return;
    }
    var node;
    for (var i = 0; i < childNodes.length; i++) {
        node = childNodes.item(i);
        if (node.nodeType == Node.ELEMENT_NODE) {
            node.onmouseover = onMouseOverItem;
            node.onmouseout = onMouseOutItem;
            node.onclick = onClickItem;
        }
    }
}
