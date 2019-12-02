 function mostraralerta(){
       var elementos =document.getElementsByClassName('editar_precio');
       var precio;
       for(var i=0;i<5;i++){
            precio=document.getElementsByClassName('texto2')[i];
            precio.style.display = "none";
            elementos[i].style.display = "inline";
       }
       }
    function hacerclic(){
        elementos = document.getElementsByClassName('boton4');
        elementos.addEventListener('click', mostraralerta, false);
       }
    window.addEventListener('load',hacerclic, false);