document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('tabla-pendientes').style.display = 'none';
    document.getElementById('tabla-completadas').style.display = 'block';
    document.getElementById('pendientes-tab').classList.remove('option-active');
    document.getElementById('completadas-tab').classList.add('option-active');
});

