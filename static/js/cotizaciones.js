function mostrarTabla(tab) {
    if (tab === 'pendientes') {
        document.getElementById('tabla-pendientes').style.display = 'block';
        document.getElementById('tabla-completadas').style.display = 'none';

        document.getElementById('pendientes-tab').classList.add('option-active');
        document.getElementById('completadas-tab').classList.remove('option-active');
    } else if (tab === 'completadas') {
        document.getElementById('tabla-pendientes').style.display = 'none';
        document.getElementById('tabla-completadas').style.display = 'block';
        
        document.getElementById('pendientes-tab').classList.remove('option-active');
        document.getElementById('completadas-tab').classList.add('option-active');
    }
}