function setIdDelete(id, nombre, url){
    document.getElementById('deleteConfirm').href = url;
    document.getElementById('datoEliminado').textContent = nombre;
}

function onLoadModal(modalId){
    var html = '<div id="modalBack" class="modal-backdrop fade show" onclick="dismiss(modalBack)"></div>';
    document.body.insertAdjacentHTML('beforeend', html);
    var modal = document.getElementById(modalId);
    modal.classList.add('show');
    modal.style = 'display: block;'
}

function dismissDiv(div){
    document.getElementById(div).remove();
}

function dismissModal(modalId){
    modal = document.getElementById(modalId);
    modal.classList.remove('show');
    modal.style = 'display: none;'
    dismissDiv('modalBack');
}

function setPrecioTotal(){
    cantidad = document.getElementById('id_quantity').value;
    precio = document.getElementById('id_unitary_price').value;
    document.getElementById('id_total').value = cantidad * precio;
}