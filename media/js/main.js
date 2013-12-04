var clickedMenuItem;

function onMouseOverMenuItem() {
    this.style.backgroundColor = "#F1F1F1";
    this.style.cursor = "pointer";
}

function onMouseOutMenuItem() {
    this.style.backgroundColor = "#FFFFFF";
}

function onClickMenuItem() {
    if (clickedMenuItem) {
	clickedMenuItem.style.borderLeftColor = "";
    }
    this.style.borderLeftColor = "red";
    clickedMenuItem = this;

    alert(this.attributes["data-href"].value);
}

function menuStyle() {
    var menu = document.getElementById("menu");
    var menuItems = menu.childNodes;
    var node;
    for (var i = 0; i < menuItems.length; i++) {
        if ((node = menuItems.item(i)).nodeType = Node.ELEMENT_NODE) {
	    node.onmouseover = onMouseOverMenuItem;
            node.onmouseout = onMouseOutMenuItem;
	    node.onclick = onClickMenuItem;
	}
    }
}

menuStyle();
