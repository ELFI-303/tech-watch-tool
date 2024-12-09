var visible = false;

function zoomElement(element){
    let div = document.createElement('div');
    div.innerHTML = element.innerHTML;
    div.id = "zoomArticle"
    div.style.position = 'absolute';
    div.style.fontSize = '20px';
    div.style.backgroundColor = 'white';
    div.style.width = 'fit-content';
    div.style.maxHeight = 'fit-content';
    div.style.maxHeight = '90vh';
    div.style.overflowY = 'auto';
    div.style.zIndex = 20;
    div.style.top = '50%';
    div.style.left = '50%';
    div.style.transform = 'translate(-50%, -50%)';
    div.style.padding = '20px';
    div.style.borderRadius = '10px';
    document.body.appendChild(div);
    document.querySelectorAll("body > div").forEach((element) => {
        if (element != div && !div.contains(element)){
            element.style.filter = 'blur(10px)';
        }
    })
    visible = true
}

document.addEventListener('click', (event) => {
    if ((event.target.className).includes('projcard-description') && !visible) {
        element = event.target;
        zoomElement(element);
    } else if ((event.target.parentNode.className).includes('projcard-description') && !visible) {
        element = event.target.parentNode;
        zoomElement(element);
    } else if ((event.target.parentNode.parentNode.className).includes('projcard-description')  && !visible) {
        element = event.target.parentNode.parentNode;
        zoomElement(element);
    } else if (visible) {
        var div = document.getElementById('zoomArticle');
        var childrens = div.children;
        var touched = false;
        for (child of childrens) { 
            if (event.target.parentNode.parentNode.parentNode.parentNode == child || event.target.parentNode.parentNode.parentNode == child || event.target.parentNode.parentNode == child || event.target.parentNode == child || event.target == child || event.target == div) {
                touched = true;
            }
        }
        if (!touched) {
            document.querySelectorAll("body > div:not(#zoomArticle)").forEach((element) => {
                element.style.filter = 'none';
            })
            document.body.removeChild(div);
            visible = false;
        }
    }
});