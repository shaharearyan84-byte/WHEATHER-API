function updateClock(){

    const now = new Date();

    document.getElementById("clock").innerHTML =
    "🕒 " + now.toLocaleTimeString();
}

setInterval(updateClock,1000);

updateClock();

const button = document.querySelector("button");

if(button){

    button.addEventListener("click",()=>{

        button.innerHTML="⏳ Loading...";

        setTimeout(()=>{

            button.innerHTML="Search";

        },2000);
    });
}
