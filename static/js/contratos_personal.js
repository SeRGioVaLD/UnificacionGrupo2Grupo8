function mostrarTabla(tab) {
    if (tab === 'crear') {
        document.getElementById('tabla-crear').style.display = 'block';
        document.getElementById('tabla-pendientes').style.display = 'none';
        document.getElementById('tabla-registrados').style.display = 'none';

        document.getElementById('crear-tab').classList.add('option-active');
        document.getElementById('pendientes-tab').classList.remove('option-active');
        document.getElementById('registrados-tab').classList.remove('option-active');
    } else if (tab === 'pendientes') {
        document.getElementById('tabla-crear').style.display = 'none';
        document.getElementById('tabla-pendientes').style.display = 'block';
        document.getElementById('tabla-registrados').style.display = 'none';

        document.getElementById('crear-tab').classList.remove('option-active');
        document.getElementById('pendientes-tab').classList.add('option-active');
        document.getElementById('registrados-tab').classList.remove('option-active');
    }else if (tab === 'registrados') {
        document.getElementById('tabla-crear').style.display = 'none';
        document.getElementById('tabla-pendientes').style.display = 'none';
        document.getElementById('tabla-registrados').style.display = 'block';
        
        document.getElementById('crear-tab').classList.remove('option-active');
        document.getElementById('pendientes-tab').classList.remove('option-active');
        document.getElementById('registrados-tab').classList.add('option-active');
    }
}