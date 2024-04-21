var modal = document.getElementById('modal');
var responseTitle = document.getElementById('response-title');
var responseDescription = document.getElementById('response-description');
var closeBtn = document.getElementById('close');

function openRespondersList(postId, responderId, title, description) {
  document.getElementById('response-title').innerText = title;
  document.getElementById('response-description').innerText = description;
  
  // Показать модальное окно
  document.getElementById('modal').style.display = 'block';
  
  // Обработчик события для кнопки "Закрыть"
  document.getElementById('close').addEventListener('click', function() {
      // Скрыть модальное окно при нажатии на кнопку "Закрыть"
      document.getElementById('modal').style.display = 'none';
  });
}
