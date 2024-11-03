var leftArrow1 = document.getElementById("left-arrow-1");
var leftArrow2 = document.getElementById("left-arrow-2");
var rightArrow1 = document.getElementById("right-arrow-1");
var rightArrow2 = document.getElementById("right-arrow-2");
var picturePicker1 = document.getElementById("picture-picker-1");
var picturePicker2 = document.getElementById("picture-picker-2");
var hero = document.getElementById("hero");
    function change(){
        hero.style.backgroundImage="url('/media/flower-setting.jpg')"
        hero.style
        leftArrow1.style.display="none"
        leftArrow2.style.display="block"
        rightArrow2.style.display="block"
        rightArrow1.style.display="none"
        picturePicker1.innerHTML='<i class="fa-regular fa-circle"></i>'
        picturePicker2.innerHTML='<i class="fa-solid fa-circle"></i>'
    }

    function change2(){
        hero.style.backgroundImage="url('/media/orchid-pink.jpg')"
        leftArrow2.style.display="none"
        leftArrow1.style.display="block"
        rightArrow1.style.display="block"
        rightArrow2.style.display="none"
        picturePicker2.innerHTML='<i class="fa-regular fa-circle"></i>'
        picturePicker1.innerHTML='<i class="fa-solid fa-circle"></i>'
    }
    
    leftArrow2.addEventListener('click', change2);
    leftArrow1.addEventListener('click', change);
    rightArrow1.addEventListener('click', change);
    rightArrow2.addEventListener('click', change2);
    picturePicker2.addEventListener('click', change);
    picturePicker1.addEventListener('click', change2);