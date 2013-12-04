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
    if (clickedMenuItem) {
	clickedMenuItem.style.borderLeftColor = "";
	clickedMenuItem.style.backgroundColor = "#FFFFFF";
    }
    this.style.borderLeftColor = "red";
    this.style.backgroundColor = "#F1F1F1";
    clickedMenuItem = this;
    contentURL = this.getAttribute("data-href");
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
