document.addEventListener('DOMContentLoaded', function() {
  var answerElements = document.querySelectorAll('.answers-answer');

  answerElements.forEach(function(element) {
    element.addEventListener('click', function() {
      // Удаляем класс 'clicked' у всех элементов
      answerElements.forEach(function(el) {
        el.classList.remove('clicked');
      });

      // Присваиваем класс 'clicked' элементу, по которому был клик
      element.classList.add('clicked');
    });
  });
});
