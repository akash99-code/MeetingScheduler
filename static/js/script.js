function goto(link){
    window.open(link);
}

function prayer(arr){
    let day = new Date().getDay();
    if(day==0)
        alert('get back to sleep bro, its `Sunday` ');  
    else{
        l = arr[day]
        if(l!="")
            window.open(l);
        else 
            alert('no link')
    }
}