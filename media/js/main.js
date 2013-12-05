function onMouseOverMenuItem() {
    this.style.backgroundColor = "#F1F1F1";
    this.style.cursor = "pointer";
}

function onMouseOutMenuItem() {
    if (this != clickedMenuItem) {
        this.style.backgroundColor = "#FFFFFF";
    }
}

function onClickMenuItem() {
    setClickedMenuItemStyle(this);
    clickedMenuItem = this;
    contentURL = this.getAttribute("data-href");
    sessionStorage.setItem("content.url", contentURL);
    sessionStorage.setItem("menuitem.clicked", this.getAttribute("id"));
    setData("content", "/customers");
}

function bindMenuAction() {
    var menuItems = document.getElementById("menu").childNodes;
    var node;
    for (var i = 0; i < menuItems.length; i++) {
        if ((node = menuItems.item(i)).nodeType = Node.ELEMENT_NODE) {
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
    xhr.onreadystatechange = function() {
        if (this.readyState == this.DONE) {
	    if (this.status == 200) {
		document.getElementById(container).innerHTML = this.response;
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
    menuItemElement.style.borderLeftColor = "red";
    menuItemElement.style.backgroundColor = "#F1F1F1";
}
