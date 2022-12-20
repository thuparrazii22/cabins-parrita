function confirmarEliminacion(id){
    Swal.fire({
      title: '¿Esta Seguro?',
      text: "No Podras Deshacer Esta Acción!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Sí, eliminar!',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href = "/eliminar_proyecto/"+id+"/";
      }
    })
  }