from browser import document, alert

# bind event 'click' on button to function echo
@document["mybutton"].bind("click")
def echo(ev):
    alert("Было введено:" + document["zone"].value)