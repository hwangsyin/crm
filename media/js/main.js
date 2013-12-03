function onMouseOverMenuItem() {
    this.style.backgroundColor = "red";
}

function onMouseOutMenuItem() {
    this.style.backgroundColor = "#FFFFFF";
}

var menuE = document.getElementById("menu");
var menuItems = menuE.childNodes;
alert(menuItems.length);
