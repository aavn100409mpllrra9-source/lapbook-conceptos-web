document.addEventListener('DOMContentLoaded', () => {
  const lapbookMain = document.getElementById('lapbook-main');
  const toggleBtn = document.getElementById('toggle-lapbook-btn');

  // 1. Control de apertura de las solapas exteriores
  toggleBtn.addEventListener('click', () => {
    lapbookMain.classList.toggle('open');
    if (lapbookMain.classList.contains('open')) {
      toggleBtn.textContent = 'Cerrar Lapbook';
    } else {
      toggleBtn.textContent = 'Abrir / Cerrar Lapbook';
    }
  });

  document.querySelectorAll('.lapbook-cover').forEach(cover => {
    cover.addEventListener('click', () => {
      lapbookMain.classList.add('open');
      toggleBtn.textContent = 'Cerrar Lapbook';
    });
  });

  // 2. Volteo manual en movil/click para Tarjetas 3D HTML
  document.querySelectorAll('.flip-card').forEach(card => {
    card.addEventListener('click', () => {
      card.classList.toggle('flipped');
    });
  });

  // 3. Interacción Acordeón de Etiquetas
  document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', () => {
      const content = header.nextElementSibling;
      const item = header.parentElement;
      item.classList.toggle('active');
      content.style.display = content.style.display === 'block' ? 'none' : 'block';
    });
  });

  // 4. Interacción Tiras CSS
  document.querySelectorAll('.strip-header').forEach(header => {
    header.addEventListener('click', () => {
      const details = header.nextElementSibling;
      header.classList.toggle('active');
      details.style.display = details.style.display === 'block' ? 'none' : 'block';
    });
  });

  // 5. Interacción Jinja
  document.querySelectorAll('.jinja-header').forEach(header => {
    header.addEventListener('click', () => {
      const body = header.nextElementSibling;
      body.style.display = body.style.display === 'block' ? 'none' : 'block';
    });
  });

  // 6. Interacción Sobre SQL
  document.querySelectorAll('.envelope-flap').forEach(flap => {
    flap.addEventListener('click', () => {
      const content = flap.nextElementSibling;
      content.style.display = content.style.display === 'block' ? 'none' : 'block';
    });
  });

  // 7. Interacción JavaScript Cards
  document.querySelectorAll('.js-card-header').forEach(header => {
    header.addEventListener('click', () => {
      const body = header.nextElementSibling;
      header.classList.toggle('active');
      body.style.display = body.style.display === 'block' ? 'none' : 'block';
    });
  });
});